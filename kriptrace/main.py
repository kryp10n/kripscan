import argparse
import requests

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,query,country,regionName,city,isp,org,as"
    res = requests.get(url).json()
    return res

def display_info(info):
    if info['status'] != 'success':
        print(f"[!] Error: {info['message']}")
        return
    print(f"IP: {info['query']}")
    print(f"Location: {info['city']}, {info['regionName']}, {info['country']}")
    print(f"ISP: {info['isp']}")
    print(f"Org: {info['org']}")
    print(f"ASN: {info['as']}")

def main():
    parser = argparse.ArgumentParser(description="kriptrace - IP intelligence tool by kryp10n")
    parser.add_argument('-i', '--ip', required=True, help='IP address or domain to trace')
    parser.add_argument('--json', action='store_true', help='Print raw JSON output')
    args = parser.parse_args()

    info = get_ip_info(args.ip)
    if args.json:
        print(info)
    else:
        display_info(info)
