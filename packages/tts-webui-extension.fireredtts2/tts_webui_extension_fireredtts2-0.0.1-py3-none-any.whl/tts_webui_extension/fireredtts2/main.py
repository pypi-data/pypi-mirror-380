import gradio as gr

from .dialogue_ui import dialogue_ui
from .tts_ui import tts_ui


# UI rendering
def fireredtts2_ui():
    gr.Markdown(
        """
    # FireRedTTS2
    VRAM Requirement 14GB+, Space Requirement 20GB+
    """
    )
    with gr.Tabs():
        with gr.Tab("Monologue"):
            tts_ui()
        with gr.Tab("Dialogue"):
            dialogue_ui()


def extension__tts_generation_webui():
    fireredtts2_ui()

    return {
        "package_name": "tts_webui_extension.fireredtts2",
        "name": "FireRedTTS2",
        "requirements": "git+https://github.com/rsxdalv/tts_webui_extension.fireredtts2@main",
        "description": "A template extension for TTS Generation WebUI",
        "extension_type": "interface",
        "extension_class": "text-to-speech",
        "author": "FireRedTeam",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/rsxdalv/tts_webui_extension.fireredtts2",
        "extension_website": "https://github.com/rsxdalv/tts_webui_extension.fireredtts2",
        "extension_platform_version": "0.0.1",
    }


if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        with gr.Tab("Fireredtts2", id="fireredtts2"):
            fireredtts2_ui()

    demo.launch(
        server_port=7772,  # Change this port if needed
    )
