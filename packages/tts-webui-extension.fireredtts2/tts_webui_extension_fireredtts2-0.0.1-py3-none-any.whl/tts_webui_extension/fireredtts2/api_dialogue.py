import re
import gradio as gr
from typing import List, Literal

from .api import SAMPLE_RATE, get_model_helper


def api_dialogue():
    pass


def check_monologue_text(text: str, prefix: str = None) -> bool:
    text = text.strip()
    # Check speaker tags
    if prefix is not None and (not text.startswith(prefix)):
        return False
    # Remove prefix
    if prefix is not None:
        text = text.removeprefix(prefix)
    text = text.strip()
    # If empty?
    if len(text) == 0:
        return False
    return True


def check_dialogue_text(text_list: List[str]) -> bool:
    if len(text_list) == 0:
        return False
    for text in text_list:
        if not (
            check_monologue_text(text, "[S1]")
            or check_monologue_text(text, "[S2]")
            or check_monologue_text(text, "[S3]")
            or check_monologue_text(text, "[S4]")
        ):
            return False
    return True


def dialogue_synthesis_function(
    target_text: str,
    voice_mode: Literal[0, 1] = 0,  # 0 means voice clone
    spk1_prompt_text: str | None = "",
    spk1_prompt_audio: str | None = None,
    spk2_prompt_text: str | None = "",
    spk2_prompt_audio: str | None = None,
    spk3_prompt_text: str | None = "",
    spk3_prompt_audio: str | None = None,
    spk4_prompt_text: str | None = "",
    spk4_prompt_audio: str | None = None,
    device: Literal["cpu", "cuda", "mps"] = "cuda",
):
    # Voice clone mode, check prompt info
    if voice_mode == 0:
        # get number of speakers from target text
        num_speakers = max(
            [int(s) for s in re.findall(r"\[S([0-9])\]", target_text)] + [1]
        )

        prompt_has_value = [
            spk1_prompt_text != "",
            spk1_prompt_audio is not None,
            spk2_prompt_text != "" or num_speakers < 2,
            spk2_prompt_audio is not None or num_speakers < 2,
            spk3_prompt_text != "" or num_speakers < 3,
            spk3_prompt_audio is not None or num_speakers < 3,
            spk4_prompt_text != "" or num_speakers < 4,
            spk4_prompt_audio is not None or num_speakers < 4,
        ]
        if not all(prompt_has_value):
            gr.Warning(message="Incomplete speaker prompt info.")
            return None
        if not check_monologue_text(spk1_prompt_text, "[S1]"):
            gr.Warning(message="Invalid speaker 1 prompt text.")
            return None
        if not check_monologue_text(spk2_prompt_text, "[S2]"):
            gr.Warning(message="Invalid speaker 2 prompt text.")
            return None
    # Check dialogue text
    target_text_list: List[str] = re.findall(r"(\[S[0-9]\][^\[\]]*)", target_text)
    target_text_list = [text.strip() for text in target_text_list]
    if not check_dialogue_text(target_text_list):
        gr.Warning(message="Invalid dialogue text.")
        return None

    # Go synthesis
    progress_bar = gr.Progress(track_tqdm=True)
    prompt_wav_list = (
        None
        if voice_mode != 0
        else [
            spk1_prompt_audio,
            spk2_prompt_audio,
            spk3_prompt_audio,
            spk4_prompt_audio,
        ]
    )
    prompt_text_list = (
        None
        if voice_mode != 0
        else [spk1_prompt_text, spk2_prompt_text, spk3_prompt_text, spk4_prompt_text]
    )
    model = get_model_helper("dialogue", device)
    target_audio = model.generate_dialogue(
        text_list=target_text_list,
        prompt_wav_list=prompt_wav_list,
        prompt_text_list=prompt_text_list,
        temperature=0.9,
        topk=30,
    )
    return (SAMPLE_RATE, target_audio.squeeze(0).cpu().numpy())
