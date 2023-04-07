import argparse
from pdm.project import Project
from pdm.cli.commands.base import BaseCommand

from . buildassets import build_assets

class BuildAssetCommand(BaseCommand):
    name = "build-asset"

    def handle(self, project: Project, options: argparse.Namespace) -> None:
        if not project.pyproject.settings.get("build-asset"):
            project.core.ui.echo("No build-asset configuration found", style="warning")
            return

        build_assets(project)