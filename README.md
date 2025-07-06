# 🖼️ AI Text-to-Image Convertor

Generate high-quality images from natural language prompts using state-of-the-art deep learning models like **Stable Diffusion** and **CLIP**. This Python-based tool supports CLI usage and modular extensions, with upcoming web UI support.

## 🚀 Features

- Natural language to image generation
- Safe mode with NSFW filtering
- Auto-generated file names based on prompt
- Lightweight command-line interface
- Upcoming Streamlit/Gradio-based web UI
- Clean, modular architecture for extensions

## ⚙️ Installation

```bash
git clone https://github.com/jauwaad0786/AI_text_to_image_convertor.git
cd ai_text2image

# Optional: Setup virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

##Usage
🔧 CLI Mode
Generate an image with default safety filtering:

python app.py --prompt "a cat riding a skateboard"
python app.py --prompt "your prompt here" --unsafe
##Web Interface (Coming Soon)
streamlit run app.py
# OR
python app.py --web

Example Prompts
“a futuristic city at sunset”

“an astronaut riding a horse on Mars”

“a bowl of fruit in the style of Van Gogh”

🖼️ Output
PNG image files saved in the project directory
✅ Testing
Run test cases to verify model outputs:
python -m pytest test_prompt_examples.py
📁 File Structure
ai_text2image/
├── app.py               # CLI & UI entry point
├── generator.py         # Core image generation
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── test_prompt_examples.py
└── model_local/         # Locally stored model components
🧠 Built With
Hugging Face Diffusers

CLIP

PyTorch

Python 3.8+

📌 Author: Jauwaad Bin Irshad 🎓 Final Year B.Tech CSE (AI & ML)
📧 [shaikhjauwaad@gmail.com]
Filenames automatically derived from prompts
