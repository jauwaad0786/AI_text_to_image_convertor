from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import re

_pipe = None  # Global pipeline cache

def sanitize_filename(prompt: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', prompt.strip().lower())[:50]

def generate_image(prompt: str, safe_mode: bool = True) -> Image.Image:
    global _pipe
    if _pipe is None:
        _pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        )
        _pipe = _pipe.to("cuda" if torch.cuda.is_available() else "cpu")
        if not safe_mode:
            _pipe.safety_checker = None

    with torch.autocast("cuda" if torch.cuda.is_available() else "cpu"):
        result = _pipe(prompt, height=512, width=512)
        image = result.images[0]
        if safe_mode and hasattr(result, 'nsfw_content_detected') and result.nsfw_content_detected[0]:
            image = Image.new('RGB', (512, 512), color='white')
    return image
