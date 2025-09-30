import argparse
import shutil
from pathlib import Path

from .base_module import BaseModule
from ..config import Config
from ..error_handler import ValidationError, logger


class AppModule(BaseModule):
    def __init__(self, config: Config) -> None:
        self.config = config

    def get_command(self) -> str:
        return "apps"

    def add_parser(self, subparsers: argparse._SubParsersAction) -> None:
        app_parser = subparsers.add_parser(
            self.get_command(), help="Manage micro-applications"
        )

        # Create subparsers for app commands
        app_subparsers = app_parser.add_subparsers(dest="app_command", required=True)

        # app init
        init_parser = app_subparsers.add_parser(
            "init", help="Create a new micro-app from template"
        )
        init_parser.add_argument(
            "-d",
            "--directory",
            type=str,
            default=".",
            help="Directory to create the micro-app in (default: current directory)",
        )
        init_parser.set_defaults(func=self._init_app)

        # app deploy
        deploy_parser = app_subparsers.add_parser(
            "deploy", help="Deploy micro-app (same as assistants synchronize)"
        )
        deploy_parser.add_argument(
            "-f",
            "--file",
            type=str,
            default="assistants.json",
            help="Path to assistants.json file (default: assistants.json)",
        )
        deploy_parser.add_argument(
            "--force", action="store_true", help="Force overwrite assistant files"
        )
        deploy_parser.set_defaults(func=self._deploy_app)

    def execute(self, args: argparse.Namespace) -> None:
        """Execute the app command."""
        args.func(args)

    def _init_app(self, args: argparse.Namespace) -> None:
        """Initialize a new micro-app from template."""
        # Get app name from user input
        app_name = input("Enter app name: ").strip()
        if not app_name:
            raise ValidationError("App name cannot be empty")

        # Create target directory if it doesn't exist
        target_dir = Path(args.directory)
        target_dir.mkdir(exist_ok=True)

        # Create assistant template with micro-app configuration
        self._create_micro_app_assistant_template(app_name, target_dir)

        # Copy the custom micro-app function to functions folder
        self._copy_micro_app_function(target_dir)

        # Copy the micro-app content to micro-app folder
        self._copy_micro_app_content(target_dir)

        # Copy avatar file
        self._copy_avatar_file(target_dir)

        logger.info(f"Created micro-app '{app_name}' in '{target_dir}'")

    def _create_micro_app_assistant_template(
        self, app_name: str, target_dir: Path
    ) -> None:
        """Create assistant template for micro-app."""
        # Load micro-app assistant template
        template_path = (
            Path(__file__).parent.parent.parent
            / "data"
            / "assistants"
            / "micro-app"
            / "assistants_template.json"
        )
        if not template_path.exists():
            raise ValidationError("Micro-app assistant template file not found")

        with open(template_path, "r") as f:
            content = f.read()

        # Replace placeholders in the template
        assistant_id = app_name.lower().replace(" ", "_").replace("-", "_")
        content = content.replace("{ASSISTANT_NAME}", app_name)
        content = content.replace("{ASSISTANT_IDENTIFIER}", assistant_id)

        # Write to target directory as assistants.json
        output_file = target_dir / "assistants.json"
        with open(output_file, "w") as f:
            f.write(content)

        logger.info(f"Created assistant config: {output_file}")

    def _copy_micro_app_function(self, target_dir: Path) -> None:
        """Copy the custom micro-app function to functions folder."""
        functions_dir = target_dir / "functions"
        functions_dir.mkdir(exist_ok=True)

        # Copy the specific micro-app function
        function_source = (
            Path(__file__).parent.parent.parent
            / "data"
            / "functions"
            / "custom_function_working_with_micro_app.py"
        )
        if not function_source.exists():
            logger.warning(f"Micro-app function template not found: {function_source}")
            return

        function_dest = functions_dir / "custom_function_working_with_micro_app.py"
        shutil.copy2(function_source, function_dest)
        logger.info(f"Created function: {function_dest}")

        # Copy essential function files
        functions_template_dir = (
            Path(__file__).parent.parent.parent / "data" / "functions"
        )
        essential_files = ["__init__.py", "requirements.txt", ".pkgignore"]
        for file in essential_files:
            src = functions_template_dir / file
            dest = functions_dir / file
            if src.exists() and not dest.exists():
                shutil.copy2(src, dest)

    def _copy_micro_app_content(self, target_dir: Path) -> None:
        """Copy the micro-app content to micro-app folder."""
        micro_app_dir = target_dir / "micro-app"

        # Copy entire micro-app template directory
        micro_app_source = Path(__file__).parent.parent.parent / "data" / "micro-app"
        if not micro_app_source.exists():
            logger.warning(
                f"Micro-app template directory not found: {micro_app_source}"
            )
            return

        shutil.copytree(micro_app_source, micro_app_dir)
        logger.info(f"Created micro-app: {micro_app_dir}")

    def _copy_avatar_file(self, target_dir: Path) -> None:
        """Copy avatar file to target directory."""
        assistants_data_path = (
            Path(__file__).parent.parent.parent / "data" / "assistants"
        )
        avatar_src = assistants_data_path / "avatar.jpeg"
        avatar_dest = target_dir / "avatar.jpeg"

        if avatar_src.exists() and not avatar_dest.exists():
            shutil.copy2(avatar_src, avatar_dest)
            logger.info(f"Created avatar: {avatar_dest}")
        elif not avatar_src.exists():
            logger.warning(f"Avatar template file not found: {avatar_src}")

    def _deploy_app(self, args: argparse.Namespace) -> None:
        """Deploy micro-app using assistants synchronize."""
        # Import and use existing sync functionality
        from .sync_module import SyncModule
        from .pkg_module import PkgModule

        pkg_module = PkgModule(config=self.config)
        sync_module = SyncModule(config=self.config, pkg_module=pkg_module)

        # Create args compatible with existing sync module
        sync_args = argparse.Namespace()
        sync_args.config = args.file
        sync_args.force = getattr(args, "force", False)

        sync_module.execute(sync_args)
