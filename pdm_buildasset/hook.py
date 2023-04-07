from . buildassets import build_assets
from pdm.project import Project

def run_build_assets(project: Project, hooks, **kwargs: any) -> None:
    """Run build hook."""

    if not project.pyproject.settings.get("build-asset"):
        return

    config = project.pyproject.settings.get("build-asset")
    if not "disable_hook" in config:
        config["disable_hook"] = False

    if not config["disable_hook"]:
        build_assets(project)