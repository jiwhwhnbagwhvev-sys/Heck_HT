from rich.console import Console
from rich.table import Table
from rich import box
import pyfiglet
import os

console = Console()

def logo():
    os.system("clear")
    text = pyfiglet.figlet_format("HT", font="slant")
    console.print(text, style="bold red")
    console.print("HT-RED ANALYZER\n", style="red bold")

def menu():
    console.print("[1] Cek ID HT")
    console.print("[2] Lihat contoh format data")
    console.print("[3] Keluar\n")

def contoh():
    console.print("\nFormat data:")
    console.print("username,negara")
    console.print("rio123,Indonesia")
    console.print("alex99,USA")
    console.print("juan88,Spain\n")

def cek_ht():
    data = []
    console.print("\nMasukkan data (ketik 'done' jika selesai)")
    while True:
        row = input("data: ")
        if row.lower() == "done":
            break
        try:
            user, negara = row.split(",")
            data.append((user.strip(), negara.strip()))
        except:
            console.print("Format salah! gunakan: username,negara", style="red")

    total = len(data)
    negara_count = {}

    for _, n in data:
        negara_count[n] = negara_count.get(n, 0) + 1

    table = Table(title="HASIL ANALISIS HT", box=box.ROUNDED)
    table.add_column("Negara", style="cyan")
    table.add_column("Jumlah", style="green")

    for n, j in negara_count.items():
        table.add_row(n, str(j))

    console.print("\nTotal Channel Masuk HT:", total, style="bold yellow")
    console.print(table)

def main():
    while True:
        logo()
        menu()
        pilih = input("Pilih: ")
        if pilih == "1":
            cek_ht()
            input("\nEnter untuk kembali...")
        elif pilih == "2":
            contoh()
            input("\nEnter untuk kembali...")
        elif pilih == "3":
            break
        else:
            console.print("Pilihan salah!", style="red")

if __name__ == "__main__":
    main()
