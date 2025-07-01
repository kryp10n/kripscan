# KRIPTRACE

`kriptrace` is a Python-based IP and domain reconnaissance tool that runs in an interactive terminal interface.  
It gathers information such as location, ISP, organization, and ASN details for a given IP address or domain name.

The tool uses the [ip-api.com](http://ip-api.com) API to fetch geolocation and network metadata.

---

## Features

- Accepts both IP addresses and domain names
- Resolves domains to IP automatically
- Provides:
  - City, region, and country
  - ISP and organization
  - ASN (Autonomous System Number)
- Works on Windows and Linux terminals

---

## Preview

Linux terminal example:

![kriptrace demo](screenshots/linux-demo.png)

---

## Installation

```bash
git clone https://github.com/kryp10n/kriptrace.git
cd kriptrace
pip install -r requirements.txt
```

For Kali or system-managed Python:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

```bash
python kriptrace.py
```

Follow the on-screen prompts to enter an IP address or domain.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

Developed by [kryp10n](https://github.com/kryp10n)
