import tkinter as tk
from settings import *
import customtkinter as ctk


# test
class WaterTimer(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # * layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform=1)

        # * widgets
        Buttons(self).grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        TimerLabel(self).grid(
            row=0, rowspan=2, column=0, sticky="nsew", padx=10, pady=10
        )

        # run the mainloop
        self.mainloop()


class TimerLabel(ctk.CTkLabel):
    def __init__(self, master):
        super().__init__(
            master,
            text="20:00",
            font=("Arial", 50),
            fg_color=COLORS["dark-grey"]["fg"],
            corner_radius=STYLING["CornerRadius"],
            text_color=TEXT_COLORS["dark-red"],
        )


class Buttons(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # * layout
        #TODO: 1 zu 2
        self.columnconfigure(0, weight=1, uniform=2)
        self.columnconfigure(1, weight=2, uniform=3)
        self.columnconfigure(2, weight=1, uniform=2)
        self.rowconfigure(0, weight=1, uniform=2)

        # * label
        self.time_label = ctk.CTkLabel(
            self,
            text="20:00",
            font=("Arial", 20),
            fg_color=COLORS["dark-grey"]["fg"],
            corner_radius=STYLING["CornerRadius"],
        )
        self.time_label.grid(row=0, column=1, sticky="nsew", pady=10)

        # * buttons
        self.plus_button = ctk.CTkButton(
            self,
            text="+",
            font=("Arial", 20),
            fg_color=COLORS["orange"]["fg"],
            hover_color=COLORS["orange"]["hover"],
            corner_radius=STYLING["CornerRadius"],
        )
        self.plus_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=20)

        self.minus_button = ctk.CTkButton(
            self,
            text="-",
            font=("Arial", 20),
            fg_color=COLORS["orange"]["fg"],
            hover_color=COLORS["orange"]["hover"],
            corner_radius=STYLING["CornerRadius"],
        )
        self.minus_button.grid(row=0, column=2, sticky="nsew", pady=10, padx=20)


app = WaterTimer("Water Timer", (500, 500))
