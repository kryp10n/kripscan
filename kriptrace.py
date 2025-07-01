#!/usr/bin/env python3
import sys
import socket
import requests
import pyfiglet
from colorama import init, Fore, Style
from kriptrace.main import get_ip_info, display_info

# Initialize colorama
init(autoreset=True)

def banner():
    art = pyfiglet.figlet_format("KRIPTRACE", font="big")
    print(Fore.CYAN + art)
    print(Fore.GREEN + "       by kryp10n\n")

def prompt_choice():
    print("Choose input type:")
    print(f"  {Fore.YELLOW}[1]{Style.RESET_ALL} IP Address")
    print(f"  {Fore.YELLOW}[2]{Style.RESET_ALL} URL / Domain\n")
    choice = input("> ").strip()
    if choice not in ("1", "2"):
        print(Fore.RED + "Invalid choice. Exiting.")
        sys.exit(1)
    return choice

def get_target(choice):
    if choice == "1":
        return input("Enter IP address:\n> ").strip()
    else:
        url = input("Enter domain name:\n> ").strip()
        try:
            ip = socket.gethostbyname(url)
            print(Fore.BLUE + f"[+] Resolved {url} → {ip}\n")
            return ip
        except socket.gaierror:
            print(Fore.RED + f"[-] Could not resolve domain: {url}")
            sys.exit(1)

def main():
    banner()
    choice = prompt_choice()
    target_ip = get_target(choice)
    info = get_ip_info(target_ip)
    display_info(info)

if __name__ == "__main__":
    main()
