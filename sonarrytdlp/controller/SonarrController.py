from typing import List

from sonarr import SeriesResource

from sonarrytdlp.service.SonarrService import SonarrService
from injector import inject


class SonarrController:
    sonarr_service: SonarrService

    @inject
    def __init__(self, sonarr_service: SonarrService):
        self.sonarr_service = sonarr_service

    def get_series(self) -> List[SeriesResource]:
        return self.sonarr_service.get_series()

    def get_series_episodes(self, id: int):
        return self.sonarr_service.get_series_episodes(id)
