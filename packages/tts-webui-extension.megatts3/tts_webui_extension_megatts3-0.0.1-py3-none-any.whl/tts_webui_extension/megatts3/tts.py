from pathlib import Path
import torch
import os

from tts_webui.utils.manage_model_state import manage_model_state

from megatts3.infer_cli import MegaTTS3DiTInfer, convert_to_wav, cut_wav
from megatts3.download import download_checkpoints


@manage_model_state("megatts3")
def get_model(
    model_name="", repo_id="ByteDance/MegaTTS3", device=None, precision=torch.float16
):
    ckpt_dir = "./data/models/megatts3"
    if not Path(ckpt_dir).exists():
        download_checkpoints(
            local_dir=ckpt_dir,
            repo_id=repo_id,
        )

    return MegaTTS3DiTInfer(
        device=device,
        ckpt_root=ckpt_dir,
        precision=precision,
    )


def get_model_helper(repo_id, device, precision):
    return get_model(
        f"{repo_id} {precision} {device}",
        repo_id=repo_id,
        device=device,
        precision=precision,
    )


def tts(
    reference_audio_path,
    latent_npy_path,
    target_text,
    inference_steps,
    intelligibility_weight,
    similarity_weight,
):
    device = torch.device("cuda:0") if torch.cuda.is_available() else None
    model = get_model_helper("ByteDance/MegaTTS3", device, torch.float16)

    convert_to_wav(reference_audio_path)
    wav_path = os.path.splitext(reference_audio_path)[0] + ".wav"
    cut_wav(wav_path, max_len=28)
    with open(wav_path, "rb") as file:
        file_content = file.read()
    resource_context = model.preprocess(file_content, latent_file=latent_npy_path)
    return model.forward(
        resource_context,
        target_text,
        time_step=inference_steps,
        p_w=intelligibility_weight,
        t_w=similarity_weight,
    )


def tts_decorated(*args, **kwargs):
    return tts(*args, **kwargs)
