import json

from injector import inject

from sonarrytdlp.controller.SonarrController import SonarrController

import gradio as gr


class MainView():
    sonarr_controller: SonarrController

    @inject
    def __init__(self, sonarr_controller: SonarrController):
        self.sonarr_controller = sonarr_controller

        self._init_tab()

    def _init_tab(self):
        with gr.Tab("Series"):
            self._init_list()

    def _init_list(self):
        series = self.sonarr_controller.get_series()
        # series = series[:1]
        for serie in series:
            episodes = self.sonarr_controller.get_series_episodes(serie.id)
            with (gr.Group(serie.title)):
                gr.Label(serie.title)

                seasons = serie.seasons
                for season in seasons:
                    with gr.Group(season):
                        season_number = season.season_number
                        season_label = f"{serie.title} - Season {season_number}"
                        gr.Label(season_label)

                        for episode in episodes:
                            if (
                                    episode.season_number == season_number
                                    and episode.has_file == False
                            ):
                                episode_label = f"{serie.title} - Season {season_number} - Episode {episode.episode_number} - {episode.title}"
                                with gr.Row():
                                    episode_number = episode.episode_number
                                    episode_number_label = gr.Label(episode_number)
                                    episode_id_label = gr.Label(episode.id)
                                    with gr.Group():
                                        url_txt = gr.Textbox("", type="text", label="Episode Url")
                                        download_btn = gr.Button(
                                            value="Download",
                                            variant="primary",
                                        )
                                        download_btn.click(
                                            self._download_episode,
                                            inputs=[url_txt, episode_id_label]
                                        )

    def _download_episode(self, url, episode_id):
        print(f"Downloading {url} - {episode_id}")
