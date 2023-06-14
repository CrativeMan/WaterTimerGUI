import tkinter as tk
from settings import *
import customtkinter as ctk


class WaterTimer(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # * layout
        self.button_font = ("Arial", 20)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform=1)

        # * widgets
        TimerLabel(self).grid(row=0, rowspan=2, column=0, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"])
        EntryFrame(self, self.button_font).grid(row=2, column=0, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"])
        ControlFrame(self, self.button_font).grid(row=3, column=0, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"])

        # run the mainloop
        self.mainloop()


class TimerLabel(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="20:00",
            font=("Arial", 50),
            fg_color=COLORS["dark-grey"]["fg"],
            corner_radius=STYLING["CornerRadius"],
            text_color=COLORS["dark-red"]["text"],
        )


class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, font):
        super().__init__(parent)

        # * layout
        self.columnconfigure(0, weight=1, uniform=2)
        self.columnconfigure(1, weight=2, uniform=2)
        self.columnconfigure(2, weight=1, uniform=2)
        self.rowconfigure(0, weight=1, uniform=2)

        # * label
        self.time_label = ctk.CTkLabel(
            self,
            text="20:00",
            font=font,
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


class ControlFrame(ctk.CTkFrame):
    def __init__(self, parent, font):
        super().__init__(parent)

        # * layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=3, uniform=3)
        self.columnconfigure(0, weight=1, uniform=3)

        # * buttons
        self.start_butoon = ctk.CTkButton(
            self, 
            text="Start",
            font=font,
            fg_color=COLORS["dark-red"]["fg"],
            hover_color=COLORS["dark-red"]["hover"],
            corner_radius=STYLING["CornerRadius"],
            command=lambda: print("start"),
        )
        self.start_butoon.grid(row=0, column=0, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"])

        self.stop_butoon = ctk.CTkButton(
            self, 
            text="Stop",
            font=font,
            fg_color=COLORS["dark-red"]["fg"],
            hover_color=COLORS["dark-red"]["hover"],
            corner_radius=STYLING["CornerRadius"],
            command=lambda: print("stop"),)
        self.stop_butoon.grid(row=0, column=1, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"])

app = WaterTimer("Water Timer", (500, 500))
