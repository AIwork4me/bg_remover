"""
bg-remover | Instant & Local
A minimalist, zero-click background removal tool.
"""

import os

# Island Mode: Keep AI models inside project folder
os.environ["U2NET_HOME"] = os.path.abspath("./.ai_models")

import gradio as gr
from rembg import remove


def process(image):
    """Remove background from image instantly."""
    if image is None:
        return None
    return remove(image)


# Build UI
with gr.Blocks(
    title="bg-remover | Instant & Local",
    theme=gr.themes.Soft(),
) as demo:
    gr.Markdown("# bg-remover | Instant & Local")
    gr.Markdown("*Upload an image, background removed automatically. Zero clicks.*")

    with gr.Row():
        input_img = gr.Image(
            label="Original Image",
            type="pil",
            sources=["upload", "webcam", "clipboard"],
        )
        output_img = gr.Image(
            label="Background Removed",
            type="pil",
            format="png",
        )

    # Zero-click: process on upload
    input_img.change(fn=process, inputs=input_img, outputs=output_img)

if __name__ == "__main__":
    demo.launch(inbrowser=True)
