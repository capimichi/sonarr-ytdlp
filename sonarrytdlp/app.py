import gradio as gr

from sonarrytdlp.container.DefaultContainer import DefaultContainer
from sonarrytdlp.view.MainView import MainView

default_container: DefaultContainer = DefaultContainer.getInstance()

with gr.Blocks() as app:
    main_view: MainView = default_container.get(MainView)

app.launch()