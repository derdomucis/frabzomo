import os
import sys
import time

from itertools import cycle
from time import sleep
from rich.console import Console
                                               
os.system("clear")
print("\n\n")
print("[+] Reactalize starting...")
time.sleep(2)
os.system("clear")
print("\n\n")
print("     _________                             ")
print("    / ======= \                            ")
print("   / __________\                           ")
print("  | ___________ |                          ")
print("  | | -       | |                          ")
print("  | |         | |                          ")
print("  | |_________| |________________________  ")
print("  \=____________/   ❖ ＭＥＲＮＩＳ ❖      | ")
print("  / ''''''''''' \                        /  ")
print(" / ::::::::::::: \                  =D-'   ")
print("(_________________)                        ")
print("\n")
time.sleep(1)
print("------------------------------------------\n")
print("[*] UYARI")
print("\n")
print("[+] Enter dedikten sonra yukleme baslicak. yukleme bitince Reading... diye bir bolum gelicek burda ekrana sakin dokunma. Reading... yazisi gidinceye kadar ekran kalsin.")
print("[+] Kullanici aratmak icin su CTRL + q ayni anda bas. ve su sekilde arat ornek:")
print("\n")
print("'MERT', 'BUDAK', '03.12.2002'")
print("\n")
print(" AD      SOYAD       TARİH   ")
print("\n[+] Sadece adi da yazabilirsin. Hangi bilgileri biliyorsaniz.")
print("\n")
start = input("[!] Press enter to start...")
os.system("clear")
time.sleep(1)

print("\n\n")
print("     _________                             ")
print("    / ======= \                            ")
print("   / __________\                           ")
print("  | ___________ |                          ")
print("  | | -       | |                          ")
print("  | |         | |                          ")
print("  | |_________| |________________________  ")
print("  \=____________/   ❖ ＭＥＲＮＩＳ ❖      | ")
print("  / ''''''''''' \                        /  ")
print(" / ::::::::::::: \                  =D-'   ")
print("(_________________)                        ")
print("\n")         
print("Ａ Ｎ Ｅ Ｚ Ａ Ｔ Ｒ Ａ")
print("\n")
console = Console()
tasks = [f"BOOTSTRAP {n}" for n in range(1, 11)]

with console.status("[bold green]BOOTSTRAP...") as status:
    while tasks:
        BOOTSTRAP = tasks.pop(0)                      
        sleep(1)
        console.log(f"{BOOTSTRAP} complete")
os.system("nano mernis.txt")
