"""Blender runner module for integrating with Blender's Python environment.

This module provides the interface for running the PalletDataGenerator
within Blender's Python environment.
"""

import importlib
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

# Add the package to sys.path if running in Blender
current_dir = Path(__file__).parent  # .../src/palletdatagenerator
src_dir = current_dir.parent  # .../src
project_root = src_dir.parent  # project root

# Ensure 'src' directory (containing the package) is on sys.path
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

# (Optional) also keep project root for relative resource access
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# If running from an activated virtual environment, add its site-packages so
# dependencies installed there are visible inside Blender's Python.
venv_path = os.environ.get("VIRTUAL_ENV")
if venv_path:
    candidate = (
        Path(venv_path)
        / "lib"
        / f"python{sys.version_info.major}.{sys.version_info.minor}"
        / "site-packages"
    )
    if candidate.exists() and str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

try:
    import bpy
    from mathutils import Vector

    BLENDER_AVAILABLE = True
except ImportError:
    BLENDER_AVAILABLE = False
    bpy = None
    Vector = None


def _pip_install(packages: list[str]) -> None:
    for pkg in packages:
        try:
            print(f"📦 Installing: {pkg}")
            # Use a visible install (not fully quiet) so user sees potential build errors
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", pkg],
                check=False,
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print(f"⚠️  Install stderr for {pkg}:\n{result.stderr.strip()[:500]}")
            else:
                print(f"✅ Installed {pkg}")
        except Exception as e:  # noqa: BLE001
            print(f"⚠️  Failed installing {pkg}: {e}")


try:
    if importlib.util.find_spec("palletdatagenerator") is None:
        project_pyproject = project_root / "pyproject.toml"
        if project_pyproject.exists():
            print("📦 Editable install of project into Blender env")
            _pip_install([f"-e{project_root}"])
        if importlib.util.find_spec("palletdatagenerator") is None:
            _pip_install(["palletdatagenerator"])

    deps_map = [
        ("yaml", "pyyaml"),
        ("PIL", "pillow"),
        ("numpy", "numpy"),
        ("pascal_voc_writer", "pascal-voc-writer"),
    ]
    missing_pkgs: list[str] = []
    for mod, pkg in deps_map:
        if importlib.util.find_spec(mod) is None:
            missing_pkgs.append(pkg)
    if missing_pkgs:
        # Install pillow first so later imports (analysis) work
        pkgs_sorted = sorted(missing_pkgs, key=lambda p: (p != "pillow", p))
        print(
            f"📦 Installing missing runtime deps inside Blender: {' '.join(pkgs_sorted)}"
        )
        _pip_install(pkgs_sorted)

    # Explicit pillow fallback target if still not importable (common on some mac builds)
    if importlib.util.find_spec("PIL") is None:
        fallback_dir = project_root / ".palletgen_blender_deps"
        try:
            print("⚠️  Pillow still missing; attempting target fallback install.")
            fallback_dir.mkdir(exist_ok=True)
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    "--no-cache-dir",
                    "--target",
                    str(fallback_dir),
                    "pillow",
                ],
                check=False,
            )
            if str(fallback_dir) not in sys.path:
                sys.path.insert(0, str(fallback_dir))
        except Exception as e:  # noqa: BLE001
            print(f"⚠️  Pillow fallback install failed: {e}")
        if importlib.util.find_spec("PIL") is None:
            print("❌ Pillow still not importable; analysis images will be skipped.")

    if importlib.util.find_spec("yaml") is None:
        print("⚠️  PyYAML missing; attempting --target fallback install.")
        fallback_dir = project_root / ".palletgen_blender_deps"
        try:
            fallback_dir.mkdir(exist_ok=True)
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--quiet",
                    "--no-cache-dir",
                    "--upgrade",
                    "--target",
                    str(fallback_dir),
                    "pyyaml",
                ],
                check=False,
            )
            if str(fallback_dir) not in sys.path:
                sys.path.insert(0, str(fallback_dir))
        except Exception as e:  # noqa: BLE001
            print(f"⚠️  Fallback PyYAML target install failed: {e}")
        if importlib.util.find_spec("yaml") is None:
            print(
                "❌ PyYAML still not importable after fallback. Run manually:"
                f" {sys.executable} -m pip install pyyaml"
            )
except Exception as e:  # noqa: BLE001
    print(f"⚠️  Auto-install sequence failed: {e}")


class BlenderEnvironmentManager:
    """Manages Blender environment setup and configuration."""

    def __init__(self):
        self.blender_available = BLENDER_AVAILABLE
        self.scene_validated = False

    def validate_blender_environment(self) -> bool:
        """Validate that Blender environment is properly set up.

        Returns:
            True if Blender environment is valid
        """
        if not self.blender_available:
            return False

        try:
            # Check basic Blender functionality
            scene = bpy.context.scene
            if not scene:
                return False

            # Check for required scene elements based on scene type
            self.scene_validated = self._validate_scene_objects()
            return self.scene_validated

        except Exception as e:
            print(f"⚠️  Blender environment validation failed: {e}")
            return False

    def _validate_scene_objects(self) -> bool:
        """Validate that required scene objects exist."""
        if not bpy.data.objects:
            print("⚠️  No objects found in scene")
            return False

        # Check for pallet objects
        pallet_objects = [
            obj for obj in bpy.data.objects if "pallet" in obj.name.lower()
        ]
        if not pallet_objects:
            print(
                "⚠️  No pallet objects found. Ensure objects are named with 'pallet' prefix"
            )

        # Check for box template objects
        box_templates = [
            obj
            for obj in bpy.data.objects
            if obj.name.startswith("box") and obj.name[-1].isdigit()
        ]
        if not box_templates:
            print(
                "⚠️  No box template objects found. Ensure objects are named 'box1', 'box2', etc."
            )

        return True

    def setup_blender_preferences(self, use_gpu: bool = True) -> None:
        """Setup Blender preferences for optimal rendering.

        Args:
            use_gpu: Whether to enable GPU rendering if available
        """
        if not self.blender_available:
            return

        try:
            # Set render engine
            bpy.context.scene.render.engine = "CYCLES"

            # GPU setup
            if use_gpu:
                preferences = bpy.context.preferences
                cycles_preferences = preferences.addons["cycles"].preferences

                # Enable GPU rendering
                cycles_preferences.refresh_devices()

                # Find available GPU devices
                gpu_devices = []
                for device in cycles_preferences.devices:
                    if device.type in {"CUDA", "OPENCL", "OPTIX", "METAL"}:
                        device.use = True
                        gpu_devices.append(device.name)

                if gpu_devices:
                    bpy.context.scene.cycles.device = "GPU"
                    print(f"🚀 GPU rendering enabled: {', '.join(gpu_devices)}")
                else:
                    print("⚠️  No GPU devices found, using CPU")
                    bpy.context.scene.cycles.device = "CPU"
            else:
                bpy.context.scene.cycles.device = "CPU"

        except Exception as e:
            print(f"⚠️  Failed to setup Blender preferences: {e}")

    def get_scene_info(self) -> dict[str, Any]:
        """Get information about the current Blender scene.

        Returns:
            Dictionary with scene information
        """
        if not self.blender_available:
            return {}

        try:
            scene = bpy.context.scene

            # Count objects by type
            pallet_count = len(
                [obj for obj in bpy.data.objects if "pallet" in obj.name.lower()]
            )
            box_count = len(
                [obj for obj in bpy.data.objects if obj.name.startswith("box")]
            )

            # Get scene dimensions
            all_objects = [obj for obj in bpy.data.objects if obj.type == "MESH"]
            if all_objects:
                # Calculate scene bounds
                min_coords = [float("inf")] * 3
                max_coords = [float("-inf")] * 3

                for obj in all_objects:
                    for vertex in obj.bound_box:
                        world_vertex = obj.matrix_world @ Vector(vertex)
                        for i in range(3):
                            min_coords[i] = min(min_coords[i], world_vertex[i])
                            max_coords[i] = max(max_coords[i], world_vertex[i])

                scene_dimensions = [max_coords[i] - min_coords[i] for i in range(3)]
            else:
                scene_dimensions = [0, 0, 0]

            return {
                "scene_name": scene.name,
                "total_objects": len(bpy.data.objects),
                "pallet_count": pallet_count,
                "box_count": box_count,
                "scene_dimensions": scene_dimensions,
                "render_engine": scene.render.engine,
                "resolution": [scene.render.resolution_x, scene.render.resolution_y],
                "frame_range": [scene.frame_start, scene.frame_end],
            }

        except Exception as e:
            print(f"⚠️  Failed to get scene info: {e}")
            return {}


def setup_background_images(background_dir: str) -> list[str]:
    """Setup random background images for rendering.

    Args:
        background_dir: Directory containing background images

    Returns:
        List of valid background image paths
    """
    if not BLENDER_AVAILABLE:
        return []

    background_path = Path(background_dir)
    if not background_path.exists():
        print(f"⚠️  Background directory not found: {background_dir}")
        return []

    # Supported image formats
    supported_formats = {".jpg", ".jpeg", ".png", ".exr", ".hdr", ".tiff", ".tga"}

    # Find all image files
    background_images = []
    for img_path in background_path.rglob("*"):
        if img_path.suffix.lower() in supported_formats:
            background_images.append(str(img_path))

    if not background_images:
        print(f"⚠️  No supported background images found in: {background_dir}")
        return []

    print(f"🖼️  Found {len(background_images)} background images")
    return background_images


def apply_random_background(background_images: list[str]) -> str | None:
    """Apply a random background image to the scene.

    Args:
        background_images: List of background image paths

    Returns:
        Path to the applied background image, or None if failed
    """
    if not BLENDER_AVAILABLE or not background_images:
        return None

    import random

    try:
        # Select random background
        selected_bg = random.choice(background_images)  # nosec B311

        # Load and apply background
        world = bpy.context.scene.world
        if not world:
            world = bpy.data.worlds.new("World")
            bpy.context.scene.world = world

        # Create environment texture
        world.use_nodes = True
        nodes = world.node_tree.nodes
        links = world.node_tree.links

        # Clear existing nodes
        nodes.clear()

        # Add environment texture nodes
        env_tex = nodes.new(type="ShaderNodeTexEnvironment")
        background = nodes.new(type="ShaderNodeBackground")
        output = nodes.new(type="ShaderNodeOutputWorld")

        # Load background image
        env_tex.image = bpy.data.images.load(selected_bg)

        # Connect nodes
        links.new(env_tex.outputs["Color"], background.inputs["Color"])
        links.new(background.outputs["Background"], output.inputs["Surface"])

        print(f"🖼️  Applied background: {Path(selected_bg).name}")
        return selected_bg

    except Exception as e:
        print(f"⚠️  Failed to apply background image: {e}")
        return None


def run_with_blender_args():
    """Main entry point when running with Blender.

    This function handles Blender-specific setup and then runs the CLI.
    """
    # Import here to avoid circular imports
    from palletdatagenerator.cli import main

    if not BLENDER_AVAILABLE:
        print("❌ This script must be run within Blender!")
        sys.exit(1)

    # Initialize environment manager
    env_manager = BlenderEnvironmentManager()

    # Validate environment
    if not env_manager.validate_blender_environment():
        print("❌ Blender environment validation failed!")
        print("💡 Ensure your scene has:")
        print("   • Objects named with 'pallet' prefix")
        print("   • Box template objects named 'box1', 'box2', etc.")
        sys.exit(1)

    # Get scene info
    scene_info = env_manager.get_scene_info()
    print("🎬 Blender Scene Information:")
    print(f"   Scene: {scene_info.get('scene_name', 'Unknown')}")
    print(f"   Objects: {scene_info.get('total_objects', 0)}")
    print(f"   Pallets: {scene_info.get('pallet_count', 0)}")
    print(f"   Boxes: {scene_info.get('box_count', 0)}")

    # Parse Blender arguments
    # When running with Blender, args after '--' are passed to the script
    try:
        script_args_start = sys.argv.index("--") + 1
        script_args = sys.argv[script_args_start:]
    except ValueError:
        # No '--' found, use default args
        script_args = ["generate", "--help"]

    print(f"🚀 Running with args: {' '.join(script_args)}")

    # Run the main CLI
    sys.exit(main(script_args))


if __name__ == "__main__":
    run_with_blender_args()
