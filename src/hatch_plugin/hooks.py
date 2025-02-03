from hatchling.plugin import hookimpl
from hatch_minify.plugin import MinifyBuildHook
from hatch.command.build import BuildCommand
import click

class CustomBuildCommand(BuildCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument("package_name", nargs='?', help="Name of the package to build")

    def handle(self, args):
        if args.package_name:
            # Store the package name in the environment or config
            self.env.config.setdefault('build', {})['package_name'] = args.package_name
        super().handle(args)

@hookimpl
def hatch_register_build_hook():
    return MinifyBuildHook

@hookimpl
def hatch_register_commands():
    return [CustomBuildCommand]