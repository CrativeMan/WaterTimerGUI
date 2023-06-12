import tkinter as tk
import customtkinter as ctk


class WaterTimer(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # create the widgets
        WaterTimerFrame(self).pack()

        # run the mainloop
        self.mainloop()


class WaterTimerFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # * layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform=1)

        # * widgets
        self.timer = ctk.CTkLabel(
            self, text="00:00:00", font=("Arial", 50), text_color="red"
        )
        self.timer.grid(row=0, rowspan=2, column=0, sticky="nsew")


app = WaterTimer("Water Timer", (500, 500))
