# Project: bg_remover (Island Mode)

## Run Commands

```bash
# Set environment variables first
export UV_PYTHON_INSTALL_DIR="./.python_runtime"
export UV_CACHE_DIR="./.uv_cache"
export UV_PROJECT_ENVIRONMENT="./.venv"

# Run the application
uv run python main.py
```

## Dependency Management

```bash
# Add new dependency
uv add <package-name>

# Remove dependency
uv remove <package-name>

# Sync dependencies
uv sync
```

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `UV_PYTHON_INSTALL_DIR` | Local Python runtime location |
| `UV_CACHE_DIR` | Package cache location |
| `UV_PROJECT_ENVIRONMENT` | Virtual environment location |
| `U2NET_HOME` | AI model storage (set in main.py) |

## Architecture

```
main.py
├── U2NET_HOME setup (before rembg import)
├── process() function - background removal
└── Gradio Blocks UI
    ├── Input: gr.Image (upload/webcam/clipboard)
    └── Output: gr.Image (PNG with transparency)
```

## Zero-Click Implementation

The `.change()` event on `input_img` triggers processing automatically:

```python
input_img.change(fn=process, inputs=input_img, outputs=output_img)
```

No submit button needed.
