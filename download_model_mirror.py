import requests
import os
from tqdm import tqdm

# ✅ Mirror URL yahan daalo jahan se tum model files fetch karna chahte ho
HOST = "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main"

# ✅ Model files list (minimum required)
FILES = [
    "v1-5-pruned-emaonly.safetensors",
    "model_index.json",
    "scheduler/scheduler_config.json",
    "text_encoder/config.json",
    "text_encoder/model.safetensors",
    "tokenizer/tokenizer_config.json",
    "tokenizer/vocab.json",
    "tokenizer/merges.txt",
    "unet/config.json",
    "unet/diffusion_pytorch_model.safetensors",
    "vae/config.json",
    "vae/diffusion_pytorch_model.safetensors",
    "safety_checker/config.json",
    "safety_checker/model.safetensors",
    "feature_extractor/preprocessor_config.json"
]

# ✅ Target folder — your custom Hugging Face model cache path
target = r"C:\Users\Admin\.cache\huggingface\hub\models--runwayml--stable-diffusion-v1-5\snapshots\451f4fe16113bff5a5d2269ed5ad43b0592e9a14"

os.makedirs(target, exist_ok=True)

def download(path):
    local_path = os.path.join(target, path)
    dir_path = os.path.dirname(local_path)
    os.makedirs(dir_path, exist_ok=True)

    url = f"{HOST}/{path}"
    r = requests.get(url, stream=True)
    total = int(r.headers.get('content-length', 0))

    with open(local_path, 'wb') as f, tqdm(
        desc=path, total=total, unit='iB', unit_scale=True
    ) as bar:
        for data in r.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)

for path in FILES:
    try:
        download(path)
    except Exception as e:
        print(f"❌ Failed to download {path}: {e}")
