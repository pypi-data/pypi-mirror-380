import gradio as gr

from tts_webui.utils.list_dir_models import unload_model_button

from .api_dialogue import dialogue_synthesis_function


def dialogue_ui() -> gr.Blocks:
    # ======================== UI ========================
    with gr.Row():
        voice_mode_choice = gr.Radio(
            choices=["Voice Clone", "Random Voice"],
            value="Voice Clone",
            label="Voice Mode",
            type="index",
            interactive=True,
        )
    with gr.Row():
        # ==== Speaker1 Prompt ====
        with gr.Column(scale=1):
            with gr.Group(visible=True) as spk1_prompt_group:
                spk1_prompt_audio = gr.Audio(
                    label="Speaker 1 Prompt Audio",
                    type="filepath",
                    editable=False,
                    interactive=True,
                )  # Audio component returns tmp audio path
                spk1_prompt_text = gr.Textbox(
                    label="Speaker 1 Prompt Text",
                    placeholder="[S1] 说话人 1 参考文本",
                    lines=3,
                )
        # ==== Speaker2 Prompt ====
        with gr.Column(scale=1):
            with gr.Group(visible=True) as spk2_prompt_group:
                spk2_prompt_audio = gr.Audio(
                    label="Speaker 2 Prompt Audio",
                    type="filepath",
                    editable=False,
                    interactive=True,
                )
                spk2_prompt_text = gr.Textbox(
                    label="Speaker 2 Prompt Text",
                    placeholder="[S2] 说话人 2 参考文本",
                    lines=3,
                )
        # ==== Speaker3 Prompt ====
        with gr.Column(scale=1):
            with gr.Group(visible=True) as spk3_prompt_group:
                spk3_prompt_audio = gr.Audio(
                    label="Speaker 3 Prompt Audio",
                    type="filepath",
                    editable=False,
                    interactive=True,
                )
                spk3_prompt_text = gr.Textbox(
                    label="Speaker 3 Prompt Text",
                    placeholder="[S3] 说话人 3 参考文本",
                    lines=3,
                )
        # ==== Speaker4 Prompt ====
        with gr.Column(scale=1):
            with gr.Group(visible=True) as spk4_prompt_group:
                spk4_prompt_audio = gr.Audio(
                    label="Speaker 4 Prompt Audio",
                    type="filepath",
                    editable=False,
                    interactive=True,
                )
                spk4_prompt_text = gr.Textbox(
                    label="Speaker 4 Prompt Text",
                    placeholder="[S4] 说话人 4 参考文本",
                    lines=3,
                )
        # ==== Text input ====
        with gr.Column(scale=2):
            dialogue_text_input = gr.Textbox(
                label="Dialogue Text Input",
                placeholder="[S1] 说话人 1 文本[S2] 说话人 2 文本...",
                lines=18,
            )

    device = gr.Radio(choices=["cpu", "cuda", "mps"], value="cuda", label="Device")
    # Generate button
    generate_btn = gr.Button(value="Generate Audio", variant="primary", size="lg")
    unload_model_button("fireredtts2")

    # Long output audio
    generate_audio = gr.Audio(
        label="Generated Audio",
        interactive=False,
    )

    # ======================== Action ========================

    # Voice clone mode action
    def _change_prompt_input_visibility(voice_mode):
        enable = voice_mode == 0
        return [
            gr.update(visible=enable),
            gr.update(visible=enable),
            gr.update(visible=enable),
            gr.update(visible=enable),
        ]

    voice_mode_choice.change(
        fn=_change_prompt_input_visibility,
        inputs=[voice_mode_choice],
        outputs=[
            spk1_prompt_group,
            spk2_prompt_group,
            spk3_prompt_group,
            spk4_prompt_group,
        ],
    )
    generate_btn.click(
        fn=dialogue_synthesis_function,
        inputs=[
            dialogue_text_input,
            voice_mode_choice,
            spk1_prompt_text,
            spk1_prompt_audio,
            spk2_prompt_text,
            spk2_prompt_audio,
            spk3_prompt_text,
            spk3_prompt_audio,
            spk4_prompt_text,
            spk4_prompt_audio,
            device,
        ],
        outputs=[generate_audio],
    )
