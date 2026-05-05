import customtkinter as ctk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image
import os
import io
import rembg


class WebPConverter(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("WebP Converter PRO")
        self.geometry("620x420")
        self.resizable(False, False)
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.file_path = None
        self.lionelmessi()
        self.ronaldo()

    def lionelmessi(self):
        self.label_title = ctk.CTkLabel(self, text="WebP Converter PRO", font=("Arial", 22, "bold"))
        self.label_title.pack(pady=10)

        self.btn_select = ctk.CTkButton(self, text="Select Image", command=self.select_image, width=180)
        self.btn_select.pack(pady=8)

        self.combo_mode = ctk.CTkComboBox(self, values=["Only Convert to WebP", "Convert + White Background"], width=240)
        self.combo_mode.pack(pady=10)

        self.label_file = ctk.CTkLabel(self, text="", text_color="gray")
        self.label_file.pack(pady=5)

        self.progress = ctk.CTkProgressBar(self, width=350)
        self.progress.set(0)
        self.progress.pack(pady=15)

        self.btn_convert = ctk.CTkButton(self, text="Convert", command=self.convert_image, width=200)
        self.btn_convert.pack(pady=10)

    def ronaldo(self):
        self.drop_frame = ctk.CTkFrame(self, width=350, height=80, corner_radius=10)
        self.drop_frame.pack(pady=10)
        self.drop_frame.pack_propagate(False)

        self.drop_label = ctk.CTkLabel(self.drop_frame, text="Drag & Drop image here", text_color="gray")
        self.drop_label.pack(expand=True)

        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind("<<Drop>>", self.handle_drop)

    def handle_drop(self, event):
        path = event.data.replace("{", "").replace("}", "")
        if os.path.isfile(path):
            self.set_file(path)

    def select_image(self):
        file_types = [
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp *.tiff"),
            ("All Files", "*.*"),
        ]
        path = filedialog.askopenfilename(filetypes=file_types)
        if path:
            self.set_file(path)

    def set_file(self, path):
        self.file_path = path
        self.label_file.configure(text=f"Selected: {os.path.basename(path)}")

    def convert_image(self):
        if not self.file_path:
            messagebox.showwarning("Warning", "Please select an image first!")
            return

        mode = self.combo_mode.get()

        output_path = filedialog.asksaveasfilename(
            defaultextension=".webp",
            filetypes=[("WebP Image", "*.webp")],
            title="Save output file"
        )

        if not output_path:
            return

        try:
            self.progress.set(0.2)

            if mode == "Only Convert to WebP":
                img = Image.open(self.file_path)
                img.save(output_path, "webp", quality=95)
                self.progress.set(1.0)

            else:
                with open(self.file_path, "rb") as f:
                    data = f.read()

                removed_bytes = rembg.remove(data)
                self.progress.set(0.5)

                img_no_bg = Image.open(io.BytesIO(removed_bytes)).convert("RGBA")
                white_bg = Image.new("RGBA", img_no_bg.size, (255, 255, 255, 255))
                final_img = Image.alpha_composite(white_bg, img_no_bg)
                final_img.convert("RGB").save(output_path, "webp", quality=95)
                self.progress.set(1.0)

            messagebox.showinfo("Success", "Image converted successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.progress.set(0)


if __name__ == "__main__":
    app = WebPConverter()
    app.mainloop()
