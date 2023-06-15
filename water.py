import customtkinter as ctk
from settings import *
import time

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

        # * widgets
        Widgets(
            parent=self, 
            timer_font=self.timer_font,
        ).pack(expand=True, fill=ctk.BOTH)

        # * run
        self.mainloop()

class Widgets(ctk.CTkFrame):
    def __init__(self, parent, timer_font):
        super().__init__(parent)
        # * layout
        self.rowconfigure((0,1,2,3),  weight=1, uniform=1)
        self.columnconfigure(0, weight=1, uniform=1)

        # * widgets
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
            sticky="nsew",
            padx=STYLING["Gap"],
            pady=STYLING["Gap"]
        )

water_timer = WaterTimer("Water timer", (500,400))
