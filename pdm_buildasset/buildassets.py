import os
import shutil
import subprocess
from pdm.project import Project

def build_assets(project: Project) -> None:
    cwd = os.getcwd()

    builds_config = project.pyproject.settings.setdefault("build-asset", {})
    builds_config.pop("disable_hook")
    for asset_name, config in builds_config.items():
        with project.core.ui.open_spinner(f"Building {asset_name} asset..."):
            os.chdir(os.path.join(cwd, config["directory"]))

            if "env" in config:
                for key, value in config["env"].items():
                    os.environ[key] = value

            if "dest_dir" in config:
                if not "clean_dest" in config:
                    config["clean_dest"] = True

                if not "create_dest" in config:
                    config["create_dest"] = True

                if config["clean_dest"]:
                    try:  # Start with a clean build directory
                        shutil.rmtree(config["dest_dir"])
                    except FileNotFoundError:
                        pass

                if config["create_dest"]:
                    try:  # Create the build directory
                        os.makedirs(config["dest_dir"])
                    except FileExistsError:
                        pass

            try:
                #TODO: Debug Logging
                exitcode = subprocess.check_call(config["command"].split(), shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            except (FileNotFoundError):
                project.core.ui.echo(f"{asset_name} asset build failed with FileNotFoundError", style="error")
                exitcode = -1
            except (subprocess.CalledProcessError, OSError):
                project.core.ui.echo(f"{asset_name} asset build failed with CalledProcessError", style="error")
                exitcode = -1

            os.chdir(cwd)

        if exitcode == 0:
            project.core.ui.echo(f"{asset_name} asset built successfully", style="success")
        else:
            project.core.ui.echo(f"{asset_name} asset build failed with exit code {exitcode}", style="error")

    os.chdir(cwd)