import gradio as gr

from tts_webui.utils.list_dir_models import unload_model_button

from .api import tts_decorated


def tts_ui():
    with gr.Row():
        with gr.Column():
            text = gr.Textbox(
                label="Input Text", lines=4, placeholder="Enter text here..."
            )
            model_name = gr.Radio(
                choices=["monologue"], value="monologue", label="Model Type"
            )
            device = gr.Dropdown(
                choices=["cpu", "cuda", "mps"], value="cuda", label="Device"
            )
            temperature = gr.Slider(
                minimum=0.1, maximum=1.5, value=0.9, step=0.05, label="Temperature"
            )
            topk = gr.Slider(minimum=1, maximum=100, value=30, step=1, label="Top-K")
            generate_button = gr.Button("Generate Speech")
            unload_model_button("fireredtts2")

            speaker_prompt_audio = gr.Audio(
                label="Speaker Prompt Audio (Optional)",
                type="filepath",
                interactive=True,
            )
            speaker_prompt_text = gr.Textbox(
                label="Speaker Prompt Text (Optional)",
                lines=2,
                placeholder="[S1] Hello",
            )

        with gr.Column():
            audio_output = gr.Audio(label="Generated Audio", type="numpy")
    generate_button.click(
        fn=tts_decorated,
        inputs=[
            text,
            temperature,
            topk,
            speaker_prompt_audio,
            speaker_prompt_text,
            model_name,
            device,
        ],
        outputs=[audio_output],
        api_name="fireredtts2_generate",
    )
