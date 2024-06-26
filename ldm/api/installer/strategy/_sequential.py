from ...config import SequentialConfig
from ._strategy import InstallStrategy


class SequentialInstallStrategy(InstallStrategy[SequentialConfig]):
    def install(self, dependencies):
        self.logger.debug("Installing dependencies sequentially")
        for dependency in dependencies:
            self.logger.debug(f"Installing: {dependency.name}")
            dependency.install()
            self.logger.info(f"Installed: {dependency.name}")
