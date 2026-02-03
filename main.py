# ==========================================
#  HT-RED ANALYZER PRO
#  File : main.py
#  Fungsi : Core system
# ==========================================

from banner import show_banner
from menu import show_menu
from data_loader import input_manual, load_from_file
from analyzer import analyze
from utils import contoh_format, pause, info

def main():
    while True:
        show_banner()
        show_menu()
        pilih = input("HT> ")

        if pilih == "1":
            data = input_manual()
            analyze(data)
            pause()

        elif pilih == "2":
            file = input("Nama file (contoh: data.txt): ")
            data = load_from_file(file)
            analyze(data)
            pause()

        elif pilih == "3":
            contoh_format()
            pause()

        elif pilih == "4":
            info()
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
