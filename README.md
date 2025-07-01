# KRIPTRACE

`kriptrace` is an interactive terminal-based IP and domain reconnaissance tool, written in Python.  
It helps you gather geolocation, ISP, ASN, and organization data for any given IP or domain — with a clean terminal UI, ASCII art, and color prompts.

---

## 🚀 Features

- Interactive interface (no command-line flags)
- Supports IP or domain input
- Automatically resolves domains to IP
- Provides:
  - Location (city, region, country)
  - ISP & Organization info
  - ASN (Autonomous System Number)
- ASCII banner and color-coded output
- Works on Windows and Linux terminals

---

## 🖼️ Preview

Linux terminal example:

![kriptrace demo](screenshots/linux-demo.png)

---

## 🧑‍💻 Installation

```bash
git clone https://github.com/kryp10n/kriptrace.git
cd kriptrace
pip install -r requirements.txt
```

If you're on Kali or a managed Python environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 💡 Usage

```bash
python kriptrace.py
```

You'll see a banner and interactive prompts:

```
Choose input type:
[1] IP Address
[2] URL / Domain
```

Enter your target and view the results.

---

## 📦 Dependencies

- `requests`
- `pyfiglet`
- `colorama`

Install them via:

```bash
pip install -r requirements.txt
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

Made with terminal love by **[kryp10n](https://github.com/kryp10n)**.
