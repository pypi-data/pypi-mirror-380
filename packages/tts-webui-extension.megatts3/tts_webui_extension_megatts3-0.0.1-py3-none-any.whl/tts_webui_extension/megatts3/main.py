import gradio as gr
from .ui import megatts3_ui


def extension__tts_generation_webui():
    megatts3_ui()

    return {
        "package_name": "tts_webui_extension.megatts3",
        "name": "MegaTTS3 (Alpha)",
        "requirements": "git+https://github.com/rsxdalv/tts_webui_extension.megatts3@main",
        "description": "A template extension for TTS Generation WebUI",
        "extension_type": "interface",
        "extension_class": "text-to-speech",
        "author": "ByteDance",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/rsxdalv/tts_webui_extension.megatts3",
        "extension_website": "https://github.com/rsxdalv/tts_webui_extension.megatts3",
        "extension_platform_version": "0.0.1",
    }


if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        with gr.Tab("MegaTTS3 (Alpha)", id="megatts3"):
            megatts3_ui()

    demo.launch(
        server_port=7772,  # Change this port if needed
    )
