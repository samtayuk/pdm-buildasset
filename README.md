# pdm-buildasset

A PDM plugin to build external assets such as a react UI.

## Configuration

| Config item                            | Description                                                                                        | Default value       | Required |
|----------------------------------------|----------------------------------------------------------------------------------------------------|---------------------|----------|
| `build-asset.disable_hook`             | Disable assets being built during build command                                                    | `False`             | No       |
| `build-asset.{asset_name}.directory`   | Directory of where the asset resides relative to the project root                                  |                     | Yes      |
| `build-asset.{asset_name}.command`     | Command to build the asset                                                                         |                     | Yes      |
| `build-asset.{asset_name}.env`         | Dictionary of environment variables for the build command                                          | `{}`                | No       |
| `build-asset.{asset_name}.dest_dir`    | Destination directory of build asset                                                               |                     | No       |
| `build-asset.{asset_name}.clean_dest`  | Remove destination directory at start of build                                                     | `True`              | No       |
| `build-asset.{asset_name}.create_dest` | Create destination directory at start of build                                                     | `True`              | No       |

All configuration items use prefix `pdm.tool`, this is a viable configuration:

### Example configuration
```toml
[tool.pdm.build-asset]
disable_hook = false

[tool.pdm.build-asset.kiosk]
directory = "ui/kiosk"
command = "npm install && npm run build"
env = {BUILD_PATH = "../../frontend/kiosk"}
dest_dir = "frontend/kiosk"

[tool.pdm.build-asset.manage]
directory = "ui/manage"
command = "npm install && npm run build"
```

## Usage

This plugin enables PDM to build external assets during the normal build command.

* `pdm build` - Command builds assets then continues as normal
* `pdm build-asset` - Command builds assets only
