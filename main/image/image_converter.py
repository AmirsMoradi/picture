import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os

class ImageConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Image Format Converter")
        self.geometry("600x260")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.input_path = None
        self.lionelmessi()

    def lionelmessi(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        title_label = ctk.CTkLabel(main_frame, text="Image Format Converter", font=ctk.CTkFont(size=20, weight="bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="w")

        input_label = ctk.CTkLabel(main_frame, text="Input image:")
        input_label.grid(row=1, column=0, sticky="w")

        self.input_entry = ctk.CTkEntry(main_frame, width=360)
        self.input_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        browse_button = ctk.CTkButton(main_frame, text="Browse...", width=90, command=self.browse_image)
        browse_button.grid(row=1, column=2, pady=5, sticky="e")

        format_label = ctk.CTkLabel(main_frame, text="Output format:")
        format_label.grid(row=2, column=0, sticky="w", pady=(10, 0))

        self.format_combo = ctk.CTkComboBox(main_frame, values=["WEBP", "PNG", "JPG", "JPEG", "BMP"], state="readonly")
        self.format_combo.set("WEBP")
        self.format_combo.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")

        output_label = ctk.CTkLabel(main_frame, text="Output file:")
        output_label.grid(row=3, column=0, sticky="w", pady=(10, 0))

        self.output_entry = ctk.CTkEntry(main_frame, width=360)
        self.output_entry.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="we")

        saveas_button = ctk.CTkButton(main_frame, text="Save As...", width=90, command=self.choose_output_path)
        saveas_button.grid(row=3, column=2, pady=(10, 0), sticky="e")

        convert_button = ctk.CTkButton(main_frame, text="Convert", height=34, command=self.convert_image)
        convert_button.grid(row=4, column=0, columnspan=3, pady=(20, 0), sticky="we")

        self.status_label = ctk.CTkLabel(main_frame, text="", text_color="lightgray")
        self.status_label.grid(row=5, column=0, columnspan=3, pady=(10, 0), sticky="w")

        main_frame.grid_columnconfigure(1, weight=1)

    def browse_image(self):
        filetypes = [
            ("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff;*.webp"),
            ("All files", "*.*"),
        ]
        path = filedialog.askopenfilename(title="Select an image", filetypes=filetypes)
        if not path:
            return
        self.input_path = path
        self.input_entry.delete(0, "end")
        self.input_entry.insert(0, path)
        self.suggest_output_path()

    def suggest_output_path(self):
        if not self.input_path:
            return
        ext = self.format_combo.get().lower()
        base, _ = os.path.splitext(self.input_path)
        suggestion = f"{base}_converted.{ext}"
        self.output_entry.delete(0, "end")
        self.output_entry.insert(0, suggestion)

    def choose_output_path(self):
        if not self.input_path:
            messagebox.showwarning("Warning", "Please select an input image first.")
            return
        ext = self.format_combo.get().lower()
        def_ext = f".{ext}"
        filetypes = [(f"{ext.upper()} files", f"*.{ext}"), ("All files", "*.*")]
        path = filedialog.asksaveasfilename(defaultextension=def_ext, filetypes=filetypes, title="Save output image")
        if not path:
            return
        self.output_entry.delete(0, "end")
        self.output_entry.insert(0, path)

    def convert_image(self):
        in_path = self.input_entry.get().strip()
        out_path = self.output_entry.get().strip()
        fmt = self.format_combo.get().upper()

        if not in_path:
            messagebox.showwarning("Warning", "Please select an input image.")
            return
        if not os.path.isfile(in_path):
            messagebox.showerror("Error", "Input file does not exist.")
            return
        if not out_path:
            self.suggest_output_path()
            out_path = self.output_entry.get().strip()
            if not out_path:
                messagebox.showwarning("Warning", "Please choose an output path.")
                return

        try:
            self.status_label.configure(text="Converting...", text_color="yellow")
            self.update_idletasks()

            img = Image.open(in_path)
            if fmt in ["JPG", "JPEG"]:
                if img.mode in ("RGBA", "LA", "P"):
                    img = img.convert("RGB")
                img.save(out_path, format="JPEG", quality=95)
            else:
                img.save(out_path, format=fmt)

            self.status_label.configure(text=f"Done: {os.path.basename(out_path)}", text_color="lightgreen")
            messagebox.showinfo("Success", "Image converted successfully.")
        except Exception as e:
            self.status_label.configure(text="Conversion failed.", text_color="red")
            messagebox.showerror("Error", f"Failed to convert image:\n{e}")

if __name__ == "__main__":
    app = ImageConverterApp()
    app.mainloop()
