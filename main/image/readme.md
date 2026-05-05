
# WebP Converter PRO

WebP Converter PRO is a modern, lightweight, and portable Windows application built with **CustomTkinter**. It allows users to:

- Convert images to **WebP** format
- Remove background and replace it with white
- Drag & Drop images directly into the app
- Track progress with a built‑in **Progress Bar**
- Select output location using **Save As dialog**
- Export a portable EXE using PyInstaller

---

## Features

### ✔ Convert to WebP
Easily convert supported image formats such as JPG, PNG, BMP, TIFF, and more.

### ✔ White Background Mode
Remove transparent or complex backgrounds and replace them with pure white.

### ✔ Drag & Drop Support
Drop an image file into the application window to load it instantly.

### ✔ Save As Dialog
Choose where to store the final WebP output.

### ✔ Progress Bar
Visual feedback during conversion and background removal.

### ✔ Portable Build
Compile the application with PyInstaller and run it on any Windows machine.

---

## Installation
Install required dependencies:

```bash
pip install pillow customtkinter rembg tkinterdnd2
```

---

## Build Portable EXE
Use PyInstaller:

```bash
pyinstaller --noconsole --onefile --add-data "rembg;rembg" main.py
```

With custom icon:

```bash
pyinstaller --noconsole --onefile --icon=icon.ico --add-data "rembg;rembg" main.py
```

The EXE will be available in the `dist/` directory.

---

## Supported Formats
- JPG / JPEG
- PNG
- BMP
- TIFF
- WebP

---

## Developer
Python Developer: **Amirhossein Moradi**

