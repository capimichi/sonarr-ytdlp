from typing import List

import sonarr
from sonarr import SeriesResource

from sonarrytdlp.variable.SonarrApiKeyVariable import SonarrApiKeyVariable
from sonarrytdlp.variable.SonarrBaseUrlVariable import SonarrBaseUrlVariable
from injector import inject
from sonarr.api_client import ApiClient


class SonarrApiClient:
    sonarr_base_url: SonarrBaseUrlVariable
    sonarr_api_key: SonarrApiKeyVariable

    @inject
    def __init__(self, sonarr_base_url: SonarrBaseUrlVariable, sonarr_api_key: SonarrApiKeyVariable):
        self.sonarr_base_url = sonarr_base_url
        self.sonarr_api_key = sonarr_api_key

    def get_api_client(self):

        configuration = sonarr.Configuration(
            host=self.sonarr_base_url,
        )
        configuration.api_key['apikey'] = self.sonarr_api_key

        api_client = ApiClient(configuration=configuration)

        return api_client

    def get_series(self) -> List[SeriesResource]:
        api_client = self.get_api_client()
        api_instance = sonarr.SeriesApi(api_client)

        try:
            api_response = api_instance.list_series()
            return api_response
        except Exception as e:
            print("Exception when calling SeriesApi->list_series: %s\n" % e)

    def get_series_episodes(self, series_id: int):
        api_client = self.get_api_client()
        api_instance = sonarr.EpisodeApi(api_client)

        try:
            api_response = api_instance.list_episode(series_id=series_id)
            return api_response
        except Exception as e:
            print("Exception when calling EpisodeApi->list_episodes: %s\n" % e)
