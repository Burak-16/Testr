from colorama import Fore, Style
import time
print("--------------TOKEN---PANEL--------------")
with open("tokens.txt", "r") as f:
    al = f.read().split("\n")
    #print(len(al))
    if len(al) <= 1:
        if len(al[0]) <= 10:
            print(f"{Fore.RED}[!] tokens.txt yok")
            exit()
        else:
            print(f"{Fore.GREEN}[i] 1 adet tokens.txt")
    else:
        print(f"{Fore.GREEN}[i] {len(al)} tokens var tokens.txt")

print(f"{Fore.RED}------------------------------------------")