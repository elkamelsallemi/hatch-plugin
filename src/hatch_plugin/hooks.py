from hatchling.plugin import hookimpl

from hatch_plugin.plugin import MinifyBuildHook


@hookimpl
def hatch_register_build_hook():
    return MinifyBuildHook
