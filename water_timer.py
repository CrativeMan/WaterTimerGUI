import tkinter as tk
from settings import *
import customtkinter as ctk
from water_calc_functions import *


class WaterTimer(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # * data
        self.running = False
        self.time_int_var = tk.IntVar(value=0)
        self.time_text_var = tk.StringVar(value=f"{self.time_int_var.get()}:00")

        # * tracing
        self.time_int_var.trace("w", self.update_time_text)

        # * layout
        self.button_font = ("Arial", 20)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform=1)

        # * widgets
        TimerLabel(self, self.time_text_var).grid(
            row=0,
            rowspan=2,
            column=0,
            sticky="nsew",
            padx=STYLING["Gap"],
            pady=STYLING["Gap"],
        )
        EntryFrame(self, self.button_font, self.time_int_var, self.time_text_var).grid(
            row=2, column=0, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"]
        )
        ControlFrame(self, self.button_font, self.running).grid(
            row=3, column=0, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"]
        )

        # run the mainloop
        self.mainloop()

    def update_time_text(self, *args):
        self.time_text_var.set(f"{self.time_int_var.get()}:00")


class TimerLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(
            parent,
            textvariable=text,
            font=("Arial", 50),
            fg_color=COLORS["dark-grey"]["fg"],
            corner_radius=STYLING["CornerRadius"],
            text_color=COLORS["dark-red"]["text"],
        )


class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, font, int_var, text_var):
        super().__init__(parent)

        # * layout
        self.columnconfigure(0, weight=1, uniform=2)
        self.columnconfigure(1, weight=2, uniform=2)
        self.columnconfigure(2, weight=1, uniform=2)
        self.rowconfigure(0, weight=1, uniform=2)

        # * label
        self.time_label = ctk.CTkLabel(
            self,
            textvariable=text_var,
            font=font,
            fg_color=COLORS["dark-grey"]["fg"],
            text_color=COLORS["dark-red"]["text"],
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
            command=lambda: self.add_time(int_var),
        )
        self.plus_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=20)

        self.minus_button = ctk.CTkButton(
            self,
            text="-",
            font=("Arial", 20),
            fg_color=COLORS["orange"]["fg"],
            hover_color=COLORS["orange"]["hover"],
            corner_radius=STYLING["CornerRadius"],
            command=lambda: self.subtract_time(int_var),
        )
        self.minus_button.grid(row=0, column=2, sticky="nsew", pady=10, padx=20)

    def add_time(self, int_var):
        int_var.set(int_var.get() + 1)
        print(int_var.get())

    def subtract_time(self, int_var):
        if int_var.get() > 0:
            int_var.set(int_var.get() - 1)
            print(int_var.get())


class ControlFrame(ctk.CTkFrame):
    def __init__(self, parent, font, running):
        super().__init__(parent)

        # * data
        self.running = running

        # * layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=3, uniform=3)
        self.columnconfigure(0, weight=1, uniform=3)

        # * buttons
        self.start_button = ctk.CTkButton(
            self,
            text="Start",
            font=font,
            fg_color=COLORS["dark-red"]["fg"],
            hover_color=COLORS["dark-red"]["hover"],
            text_color_disabled=COLORS["dark-red"]["disabled"],
            corner_radius=STYLING["CornerRadius"],
            command=lambda: self.start_countdown(running),
        )
        self.start_button.grid(
            row=0, column=0, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"]
        )

        self.stop_button = ctk.CTkButton(
            self,
            text="Stop",
            font=font,
            fg_color=COLORS["dark-red"]["fg"],
            hover_color=COLORS["dark-red"]["hover"],
            corner_radius=STYLING["CornerRadius"],
            command=lambda: print("stop"),
        )
        self.stop_button.grid(
            row=0, column=1, sticky="nsew", padx=STYLING["Gap"], pady=STYLING["Gap"]
        )

    # * functions
    def start_countdown(self, running):
        if running:
            StartCountDown()
            self.start_button.configure(state="disabled")
        else:
            print("Timer started")
            running = True


app = WaterTimer("Water Timer", (500, 500))
