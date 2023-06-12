import tkinter as tk
import customtkinter as ctk


class WaterTimer(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        ctk.CTkLabel(self, text="Test").pack(expand=True, fill=tk.BOTH)

        self.mainloop()


app = WaterTimer("Water Timer", (500, 500))
