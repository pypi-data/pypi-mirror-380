import gradio as gr

from tts_webui.utils.list_dir_models import unload_model_button

from .tts import tts_decorated


def megatts3_ui():
    gr.Markdown("## MegaTTS3 (Alpha)")
    with gr.Row():
        with gr.Column():
            gr.Markdown("Note - the reference npy file is not optional. NPY files can be downloaded from the [MegaTTS3 GitHub](https://github.com/bytedance/MegaTTS3).")
            target_text_input = gr.Textbox(
                label="Target Text", placeholder="Enter the text...", lines=3
            )
            reference_audio_input = gr.Audio(
                type="filepath", label="Reference Audio (.wav)"
            )
            latent_file_input = gr.File(type="filepath", label="Latent File (.npy)")
            with gr.Row():
                inference_steps_input = gr.Number(
                    label="Inference Timesteps", value=32, minimum=1, maximum=100
                )
                intelligibility_weight_input = gr.Number(
                    label="Intelligibility Weight",
                    value=1.4,
                    minimum=0.1,
                    maximum=5.0,
                )
                similarity_weight_input = gr.Number(
                    label="Similarity Weight", value=3.0, minimum=0.1, maximum=10.0
                )
            unload_model_button("megatts3")
        with gr.Column():
            synth_audio_output = gr.Audio(label="Synthesized Audio")
            btn_generate = gr.Button("Generate Speech", variant="primary")

    btn_generate.click(
        fn=tts_decorated,
        inputs=[
            reference_audio_input,
            latent_file_input,
            target_text_input,
            inference_steps_input,
            intelligibility_weight_input,
            similarity_weight_input,
        ],
        outputs=[synth_audio_output],
        show_progress=True,
    )
