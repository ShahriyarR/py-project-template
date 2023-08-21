import sys

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):

    update = False

    def __init__(self, environment):
        super().__init__(environment)
        environment.globals['sys'] = sys
        environment.globals['python_path'] = sys.executable
        environment.globals['python_version'] = f"{sys.version_info.major}.{sys.version_info.minor}"

    def hook(self, context):
        pass
