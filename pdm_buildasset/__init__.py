from pdm.core import Core

def main(core: Core):
    from pdm.signals import pre_build

    from . hook import run_build_assets
    pre_build.connect(run_build_assets)

    from . command import BuildAssetCommand
    core.register_command(BuildAssetCommand)
