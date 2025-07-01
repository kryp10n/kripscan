# KRIPTRACE

`kriptrace` is a Python-based IP and domain reconnaissance tool that runs in an interactive terminal interface.  
It gathers information such as location, ISP, organization, ASN, and live website status for a given IP address or domain name.

The tool uses the [ip-api.com](http://ip-api.com) API to fetch geolocation and network metadata.

![kriptrace](screenshots/linux-demo.png)

---

## Features

- Accepts both **IP addresses** and **domain names**
- Retrieves:
  - City, region, and country
  - ISP and organization
  - ASN (Autonomous System Number)
- Checks whether a domain’s website is **live**
- Compatible with **Windows** and **Linux** terminals

---

## Installation

```bash
git clone https://github.com/kryp10n/kriptrace.git
cd kriptrace
pip install -r requirements.txt
```

> **Kali Linux users:**  
> If you see an error like:
>
> ```
> error: externally-managed-environment
> This environment is externally managed...
> ```
>
> You are running in a restricted system-managed environment.  
> Use a virtual environment to bypass it:

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

Follow the on-screen prompts and enter either an IP or domain name.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

Made by [kryp10n](https://github.com/kryp10n)
