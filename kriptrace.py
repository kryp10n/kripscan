from colorama import Fore, Style, init
import pyfiglet
import requests
import socket

init(autoreset=True)

def print_banner():
    banner = pyfiglet.figlet_format("KRIPTRACE", font="big")
    print(Fore.RED + Style.BRIGHT + banner)
    print(Style.BRIGHT + Fore.WHITE + "      kriptrace[v1] by kryp10n\n")

def prompt_choice():
    print("Choose input type:")
    print("  [1] IP Address")
    print("  [2] URL / Domain\n")
    choice = input("> ").strip()
    while choice not in ["1", "2"]:
        print(Fore.YELLOW + "[!] Invalid choice. Please enter 1 or 2.")
        choice = input("> ").strip()
    return choice

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"[+] Resolved {domain} → {ip}\n")
        return ip
    except socket.gaierror:
        print(Fore.RED + f"[!] Failed to resolve domain: {domain}")
        return None

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        print(Fore.CYAN + f"IP: {data.get('ip', 'N/A')}")
        print(f"Location: {data.get('city', 'N/A')}, {data.get('region', 'N/A')}, {data.get('country', 'N/A')}")
        print(f"ISP: {data.get('org', 'N/A').split(' ', 1)[-1]}")
        print(f"Org: {data.get('org', 'N/A')}")
        print(f"ASN: {data.get('asn', {}).get('asn', 'N/A')} {data.get('asn', {}).get('name', '')}")
    except Exception:
        print(Fore.RED + "[!] Failed to retrieve IP information.")

def is_site_live(domain):
    urls = [f"http://{domain}", f"https://{domain}"]
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                print(Fore.GREEN + f"[+] Website status ({url}): Live")
                return
            else:
                print(Fore.YELLOW + f"[!] Website ({url}) responded with status code: {response.status_code}")
        except Exception:
            continue
    print(Fore.RED + "[!] Website status: Not reachable or parked")
    
def main():
    print_banner()
    choice = prompt_choice()

    if choice == "1":
        ip = input("Enter IP address:\n> ").strip()
        get_ip_info(ip)

    elif choice == "2":
        domain = input("Enter domain name:\n> ").strip()
        ip = resolve_domain(domain)
        if ip:
            get_ip_info(ip)
            is_site_live(domain)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Interrupted by user. Exiting..." + Style.RESET_ALL)
