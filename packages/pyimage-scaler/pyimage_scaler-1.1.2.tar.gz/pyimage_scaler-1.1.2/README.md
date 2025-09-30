\# pyimage\_scaler



Resize images in Python with a unique package name.



\- Supports JPEG, PNG, BMP, GIF with Pillow (recommended).

\- Falls back to PPM/PGM/GIF with Tkinter if Pillow is not installed.



\## Usage



```python

from pyimage\_scaler import resize\_image



resize\_image("input.jpg", "output.jpg", 300, 300)


```python

from pyimage_scaler import resize_image


resize_image("input.png", "output.png", 3840, 3840)


---



\### ✅ Usage

```python

from pyimage\_scaler import resize\_image



resize\_image("my\_photo.png", "my\_photo\_resized.png", 400, 400)



