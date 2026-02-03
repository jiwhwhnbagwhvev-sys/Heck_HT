# ==========================================
#  HT-RED ANALYZER PRO
#  File : menu.py
#  Fungsi : Tampilan menu utama
# ==========================================

import time
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def loading(text, delay=0.05):
    for c in text:
        console.print(c, end="", style="red")
        time.sleep(delay)
    print()

def show_menu():
    loading(">> Loading Main Menu...\n", 0.02)
    time.sleep(0.2)

    table = Table(title="CONTROL PANEL", box=box.DOUBLE_EDGE, border_style="red")

    table.add_column("No", style="bold red", justify="center")
    table.add_column("Fitur", style="white")
    table.add_column("Deskripsi", style="cyan")

    table.add_row("1", "Cek ID HT", "Analisa data hashtag")
    table.add_row("2", "Load File", "Baca data dari file")
    table.add_row("3", "Contoh", "Lihat format data")
    table.add_row("4", "Keluar", "Exit system")

    console.print(table)
    console.print("\nPilih menu dengan angka...\n", style="red bold")
