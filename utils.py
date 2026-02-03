# ==========================================
#  HT-RED ANALYZER PRO
#  File : utils.py
#  Fungsi : Utilitas tambahan
# ==========================================

import time
from rich.console import Console

console = Console()

def contoh_format():
    console.print("\nFORMAT DATA YANG BENAR:", style="bold red")
    time.sleep(0.2)
    console.print("username,negara", style="white")
    console.print("rio,Indonesia", style="white")
    console.print("alex,USA", style="white")
    console.print("juan,Spain\n", style="white")
    time.sleep(0.2)

def pause():
    input("\nTekan Enter untuk kembali...")

def info():
    console.print("\nHT-RED ANALYZER PRO", style="bold red")
    console.print("Tool analisa hashtag dari data manual/file", style="white")
    console.print("Mode aman & legal", style="green")
