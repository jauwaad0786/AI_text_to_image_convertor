import streamlit as st
from generator import generate_image, sanitize_filename

st.title("🧠 Text to Image Generator")
prompt = st.text_input("Enter a text prompt:", "A futuristic city at sunset")
safe_mode = st.checkbox("Enable NSFW filter", value=True)

if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Generating image..."):
            image = generate_image(prompt, safe_mode=safe_mode)
            st.image(image, caption="Generated Image", use_column_width=True)
            filename = sanitize_filename(prompt) + ".png"
            image.save(filename)
            st.success(f"Image saved as: {filename}")
    else:
        st.warning("Please enter a prompt.")
