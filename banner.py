# ==========================================
#  HT-RED ANALYZER PRO
#  File : banner.py
#  Fungsi : Tampilan logo & header
#  Author : Andra Edition
# ==========================================

import os
import time
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

def slow_print(text, delay=0.01):
    for char in text:
        console.print(char, end="", style="red")
        time.sleep(delay)
    print()

def show_banner():
    os.system("clear")

    # ASCII besar
    big = pyfiglet.figlet_format("HT", font="slant")
    console.print(big, style="bold red")

    title = Text("HT-RED ANALYZER PRO", style="bold red")
    subtitle = Text("Hashtag Intelligence Terminal", style="white")

    panel = Panel(
        Align.center(title + "\n" + subtitle),
        border_style="red",
        width=60
    )

    console.print(panel)

    slow_print(">> Initializing Core Modules...")
    time.sleep(0.2)
    slow_print(">> Loading Security Layer...")
    time.sleep(0.2)
    slow_print(">> System Ready!\n")
