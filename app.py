import argparse
from generator import generate_image, sanitize_filename
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="Text-to-Image Generator")
    parser.add_argument('--prompt', type=str, help='Text prompt for image generation')
    parser.add_argument('--web', action='store_true', help='Run web UI (Streamlit)')
    parser.add_argument('--unsafe', action='store_true', help='Disable NSFW filtering')
    args = parser.parse_args()

    if args.web:
        import ui  # Runs the Streamlit app
    elif args.prompt:
        try:
            print(f"Generating image for prompt: {args.prompt}")
            image = generate_image(args.prompt, safe_mode=not args.unsafe)
            filename = sanitize_filename(args.prompt) + ".png"
            image.save(filename)
            print(f"Image saved as {filename}")
        except Exception as e:
            print(f"Error generating image: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
