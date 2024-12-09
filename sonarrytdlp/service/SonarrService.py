from typing import List

from sonarr import SeriesResource

from sonarrytdlp.client.SonarrApiClient import SonarrApiClient
from injector import inject


class SonarrService:
    sonarr_api_client: SonarrApiClient

    @inject
    def __init__(self, sonarr_api_client: SonarrApiClient):
        self.sonarr_api_client = sonarr_api_client

    def get_series(self) -> List[SeriesResource]:
        return self.sonarr_api_client.get_series()

    def get_series_episodes(self, id: int):
        return self.sonarr_api_client.get_series_episodes(id)