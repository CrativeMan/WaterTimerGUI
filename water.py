import customtkinter as ctk
from settings import *
import time
import sys


class WaterTimer(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # * fonts
        self.timer_font = (
            FONT["timer-font"]["family"], 
            FONT["timer-font"]["size"], 
            FONT["timer-font"]["weight"],
        )

        self.main_font = (
            FONT["main-font"]["family"],
            FONT["main-font"]["size"],
            FONT["main-font"]["weight"],
        )

        # * data
        self.running = False
        self.time = 0

        # * widgets
        Widgets(
            parent=self, 
            timer_font=self.timer_font,
            main_font=self.main_font,
            running=self.running,
            time=self.time,
        ).pack(expand=True, fill=ctk.BOTH)

        # * run
        self.mainloop()

class Widgets(ctk.CTkFrame):
    def __init__(self, parent, timer_font, main_font, running, time):
        super().__init__(parent)
        # * layout
        self.rowconfigure((0,1,2,3),  weight=1, uniform=1)
        self.columnconfigure((0,1,2), weight=1, uniform=1)

        # * data
        self.running = running
        self.time = time

        # * widgets
        # timer label
        self.timer_label = ctk.CTkLabel(
            self,
            text="00:00:00",
            fg_color=COLORS["dark-grey"]["fg"],
            font=timer_font,
            corner_radius=STYLING["CornerRadius"],
        )
        self.timer_label.grid(
            row=0, 
            rowspan=2, 
            column=0, 
            columnspan=3,
            sticky="nsew",
            padx=STYLING["Gap"],
            pady=STYLING["Gap"]
        )

        # add/subtract time label
        self.add_subtract_time_label = ctk.CTkLabel(
            self,
            text="00:00",
            fg_color=COLORS["dark-grey"]["fg"],
            font=main_font,
            corner_radius=STYLING["CornerRadius"],
        )
        self.add_subtract_time_label.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=STYLING["Gap"],
            pady=STYLING["Gap"],
        )

        # add time button
        self.add_time_button = ctk.CTkButton(
            self,
            text="+1 min",
            fg_color=COLORS["orange"]["fg"],
            hover_color=COLORS["orange"]["hover"],
            font=main_font,
            corner_radius=STYLING["CornerRadius"],
            command=lambda: self.add_time(),
        )
        self.add_time_button.grid(
            row=2, 
            column=0, 
            sticky="nsew", 
            padx=STYLING["Gap"], 
            pady=STYLING["Gap"]
        )

        # subtract time button
        self.subtract_time_button = ctk.CTkButton(
            self,
            text="-1 min",
            fg_color=COLORS["orange"]["fg"],
            hover_color=COLORS["orange"]["hover"],
            font=main_font,
            corner_radius=STYLING["CornerRadius"],
            command=lambda: self.subtract_time(),
        )
        self.subtract_time_button.grid(
            row=2,
            column=2,
            sticky="nsew",
            padx=STYLING["Gap"],
            pady=STYLING["Gap"],
        )

        # start button
        self.start_button = ctk.CTkButton(
            self,
            text="Start",
            fg_color=COLORS["orange"]["fg"],
            hover_color=COLORS["orange"]["hover"],
            font=main_font,
            corner_radius=STYLING["CornerRadius"],
            command=lambda: self.start_countdown(),
        )
        self.start_button.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=STYLING["Gap"],
            pady=STYLING["Gap"],
        )

        # stop button
        self.stop_button = ctk.CTkButton(
            self,
            text="Stop/Quit",
            fg_color=COLORS["orange"]["fg"],
            hover_color=COLORS["orange"]["hover"],
            font=main_font,
            corner_radius=STYLING["CornerRadius"],
            command=lambda: self.stop_countdown_quit(),
        )
        self.stop_button.grid(
            row=3,
            column=2,
            sticky="nsew",
            padx=STYLING["Gap"],
            pady=STYLING["Gap"],
        )

    def start_countdown(self):
        if self.running == False:
            self.running = True
            self.timer_label.configure(text=time.strftime("%H:%M:%S"))
            self.start_button.configure(state=ctk.DISABLED)
        
    def stop_countdown_quit(self):
        if self.running == True:
            self.running = False
            self.timer_label.configure(text="00:00")
            self.start_button.configure(state=ctk.NORMAL)
        else:
            sys.exit()

    def add_time(self):
        if self.time < 60:
            self.time += 1
            self.timer_label.configure(text=f"{self.time}:00")
            self.add_subtract_time_label.configure(text=f"{self.time}:00")

    def subtract_time(self):
        if self.time > 0:
            self.time -= 1  
            self.timer_label.configure(text=f"{self.time}:00")
            self.add_subtract_time_label.configure(text=f"{self.time}:00")

water_timer = WaterTimer("Water timer", (500,500))