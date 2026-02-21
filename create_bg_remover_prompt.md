# Role: Lead AI Interaction Designer & Architect
# Task: Develop the "bg-remover" GUI utility.

Context: Island Mode via `uv`. 
Objective: Create the absolute simplest, cleanest local GUI for background removal.

[Product Design Constraints (Crucial)]:
1.  **Project Identity**: 
    - The tool is named `bg-remover`.
    - GUI Title: "bg-remover | Instant & Local".
    - Keep the interface incredibly clean. No cluttered instructions.

2.  **The "Zero-Click" Workflow**:
    - Use Gradio's `gr.Interface` or `gr.Blocks`.
    - layout: A side-by-side comparison row.
    - **Reactive Interaction**: The processing must trigger IMMEDIATELY upon image upload. Do NOT include a "Submit" or "Run" button. The act of uploading is the trigger.

3.  **Input/Output UX**:
    - Left (Input): An Image component allowing drag-and-drop. Label: "Original Image".
    - Right (Output): An Image component showing the result. Label: "Background Removed".
    - **Download**: Ensure the output image component has a built-in download button (standard in Gradio image outputs).

[Technical Constraints (Island Mode)]:
1.  **Absolute Isolation**: 
    - In `main.py`, BEFORE importing `rembg`, you MUST set: `os.environ["U2NET_HOME"] = os.path.abspath("./.ai_models")`.
    - This keeps the ~170MB model file inside the project folder.

2.  **Dependencies**:
    - `uv add rembg pillow gradio onnxruntime`.

[Automation Flow]:
1. Initialize environment.
2. Install dependencies.
3. Generate the minimalist `main.py`.
4. Auto-Launch: `demo.launch(inbrowser=True, prevent_thread_lock=True)`.

Execute now. Build the simplest possible tool that does the job.