# KRIPTRACE

kriptrace is a lightweight command-line tool that lets you trace and gather intel on IP addresses and domains.  
Built by [kryp10n](https://github.com/kryp10n) for cybersecurity and network forensics workflows.

---

## 🔧 Features
- IP geolocation (country, city, region)
- ISP, ASN, and organization info
- JSON/raw mode with --json flag
- Clean CLI with argument support

---

## 🛠️ Installation

git clone https://github.com/kryp10n/kriptrace.git
cd kriptrace
pip install -r requirements.txt

---

## 🚀 Usage

Basic IP trace:
python3 kriptrace.py -i 8.8.8.8

Output in JSON format:
python3 kriptrace.py -i 1.1.1.1 --json

---

## 🧾 Arguments

Flag           | Description                                     | Required
---------------|-------------------------------------------------|---------
-i, --ip       | Target IP address or domain to trace            | Yes
--json         | Output raw JSON instead of formatted output     | No

---

## 🔮 Planned Features

- --save to write output to a file
- Colored terminal output with colorama
- Domain resolution (e.g., kriptrace -i google.com)
- Threat score integration (AbuseIPDB, VirusTotal)
- Optional banner / ASCII intro

---

## 👤 Author

Built with intent and curiosity by [kryp10n](https://github.com/kryp10n)  
License: MIT

