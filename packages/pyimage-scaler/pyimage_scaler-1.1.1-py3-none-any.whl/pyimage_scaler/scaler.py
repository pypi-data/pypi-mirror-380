import os

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def resize_image(input_path: str, output_path: str, width: int, height: int):

    """
    Resize an image to the specified width and height.
    Supports JPEG, PNG, BMP, GIF with Pillow.
    Falls back to limited formats without Pillow (PPM/PGM/GIF).
    """

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if PIL_AVAILABLE:
        img = Image.open(input_path)
        resized = img.resize((width, height), Image.Resampling.LANCZOS)
        resized.save(output_path)
        print(f"[pyimage_scaler] Image saved to {output_path} ({width}x{height})")
    else:
        # Tkinter fallback for limited formats (PPM/PGM/GIF)
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        from tkinter import PhotoImage
        img = PhotoImage(file=input_path)
        img = img.subsample(max(1, img.width()//width), max(1, img.height()//height))
        img.write(output_path)
        print(f"[pyimage_scaler] Image saved to {output_path} (Tkinter fallback)")