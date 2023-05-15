from typing import Optional, Tuple, Union
import customtkinter as CTk
from PIL import Image
from tkinter import filedialog

class header_frame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=("gray78", "gray28"))
        self.logo = CTk.CTkImage(dark_image=Image.open("logo\pudge.png"), size=(400, 150))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

class source_frame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=("gray78", "gray28"))
        self.source_button=CTk.CTkButton(self, text="...", width=50, height=50, command=self.source_button_action)
        self.source_button.grid(row=0, column=0)
        self.source_txt_lbl=CTk.CTkLabel(self, text="", fg_color="white")
        self.source_txt_lbl.grid(row=0, column=1)

    def source_button_action(self):
        filepath=filedialog.askopenfilename()
        



class interface(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Recognitor")
        self.geometry("1200x950")

        self.header=header_frame(self)
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.source=source_frame(self)
        self.source.grid(row=0, column=1)

if __name__ == '__main__':
    app = interface()
    app.mainloop()