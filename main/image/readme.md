# Image Format Converter

A lightweight and modern desktop application built with **Python** and **CustomTkinter** for converting images between different formats.

---

## 🚀 Features

- Convert images to multiple formats:
  - WEBP
  - PNG
  - JPG
  - JPEG
  - BMP
- Clean and modern dark UI
- File browser for selecting input images
- Save As dialog for choosing output location
- Automatic output filename suggestion
- Error handling with user-friendly messages
- Lightweight build (no AI dependencies)

---

## 🛠 Requirements

- Python 3.9+
- Pillow
- customtkinter

Install dependencies:

```bash
pip install pillow customtkinter
```

---

## ▶️ Run the Application

```bash
python image_converter.py
```

---

## 📦 Build Windows Executable (Portable)

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --noconsole --name image_converter image_converter.py
```

The executable file will be created in the `dist` folder.

---

## 📁 Project Structure

```
main.py
image_converter.py
README.md
```

---

## 💡 Notes

- When converting to JPG/JPEG, images with transparency are automatically converted to RGB.
- The application is fully portable when built with PyInstaller.
- No internet connection required.

---

## 📜 License

This project is provided for educational and personal use.

---

### Python Programmer: Amirhossein Moradi
