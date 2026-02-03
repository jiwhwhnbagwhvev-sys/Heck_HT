# ==========================================
#  HT-RED ANALYZER PRO
#  File : data_loader.py
#  Fungsi : Input & load data HT
# ==========================================

import os
import time
from rich.console import Console

console = Console()

def slow(text, delay=0.02):
    for c in text:
        console.print(c, end="", style="red")
        time.sleep(delay)
    print()

def input_manual():
    data = []
    slow("\n>> Mode Input Manual Aktif\n")

    while True:
        row = input("HT-DATA> ")
        if row.lower() == "done":
            slow(">> Input selesai.\n")
            break

        if "," not in row:
            console.print("Format salah! gunakan: username,negara", style="bold red")
            continue

        try:
            user, negara = row.split(",", 1)
            data.append((user.strip(), negara.strip()))
            console.print("Data ditambahkan ✔", style="green")
        except:
            console.print("Gagal memproses data!", style="red")

    return data


def load_from_file(filename):
    data = []
    slow(f"\n>> Membuka file: {filename}\n")

    if not os.path.exists(filename):
        console.print("File tidak ditemukan!", style="bold red")
        return data

    with open(filename, "r") as f:
        for line in f:
            if "," in line:
                u, n = line.strip().split(",", 1)
                data.append((u.strip(), n.strip()))

    slow(">> File berhasil dimuat!\n")
    return data
