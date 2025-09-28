import os

from tts_webui.utils.manage_model_state import manage_model_state

SAMPLE_RATE = 24000


def download_model():
    if not os.path.exists("./data/models/fireredtts2"):
        os.makedirs("./data/models/fireredtts2", exist_ok=True)

        from huggingface_hub import snapshot_download

        snapshot_download(
            repo_id="FireRedTeam/FireRedTTS2",
            repo_type="model",
            local_dir="./data/models/fireredtts2",
            local_dir_use_symlinks=False,
        )


@manage_model_state("fireredtts2")
def get_model(model_name, gen_type, device):
    from fireredtts2.fireredtts2 import FireRedTTS2

    download_model()

    model = FireRedTTS2(
        pretrained_dir="./data/models/fireredtts2",
        gen_type=gen_type,
        device=device,
    )
    return model


def get_model_string(model_name, device):
    return f"{model_name} on {device}"


def get_model_helper(gen_type, device):
    return get_model(
        get_model_string(gen_type, device), gen_type=gen_type, device=device
    )


def tts(
    text,
    temperature=0.9,
    topk=30,
    prompt_wav=None,
    prompt_text=None,
    model_name="monologue",
    device="cuda",
    **kwargs,
):
    model = get_model_helper(model_name, device)
    audio = model.generate_monologue(
        text=text,
        prompt_text=prompt_text,
        prompt_wav=prompt_wav,
        temperature=temperature,
        topk=topk,
    )
    return (SAMPLE_RATE, audio.squeeze(0).cpu().numpy())


# @decorators
def tts_decorated(*args, **kwargs):
    return tts(*args, **kwargs)
