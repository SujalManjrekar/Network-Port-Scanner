# 🔍 Python Network Port Scanner

A lightweight and multithreaded TCP network port scanner built with Python for cybersecurity learning, lab environments, and authorized security testing.

## 🚀 Features

- TCP port scanning
- Custom port ranges
- Multithreaded scanning for improved speed
- IP address and hostname support
- Basic service identification
- Connection timeout handling
- Simple command-line interface
- No external Python packages required

## 🛠️ Technologies Used

- Python 3
- Socket programming
- `ThreadPoolExecutor`

## 📋 Requirements

- Python 3.8 or newer
- No external dependencies

## ⚙️ Installation

Clone the repository:

```bash
https://github.com/SujalManjrekar/Network-Port-Scanner.git
cd python-network-port-scanner
```

Run the scanner:

```bash
python scanner.py
```

## 💻 Usage

The program will ask for:

1. Target IP address or hostname
2. Starting port
3. Ending port

Example:

```text
Enter target IP/hostname: 192.168.1.1
Enter starting port: 1
Enter ending port: 1000
```

Example output:

```text
Target IP: 192.168.1.1

Scanning: 192.168.1.1
Ports: 1-1000

[+] Port 22    OPEN  | Service: ssh
[+] Port 80    OPEN  | Service: http
[+] Port 443   OPEN  | Service: https

Scan completed.
```

## 🧠 How It Works

The scanner uses Python's `socket` module to attempt TCP connections to ports within the specified range.

If a connection succeeds, the port is reported as open.

`ThreadPoolExecutor` is used to scan multiple ports concurrently, making the scanner faster than a sequential implementation.

## 🔐 Ethical Use

This project is intended for:

- Educational purposes
- Cybersecurity learning
- Testing systems you own
- Authorized security assessments
- Cybersecurity lab environments

**Only scan systems and networks you own or have explicit permission to test.**

The author is not responsible for misuse of this software.

## 🔮 Future Improvements

- [ ] Command-line arguments using `argparse`
- [ ] Banner grabbing
- [ ] CSV report generation
- [ ] Scan statistics
- [ ] Logging
- [ ] Configurable timeout
- [ ] Improved service detection
- [ ] Export scan results to a file

## 👨‍💻 Author

**Sujal Manjrekar**

GitHub: https://github.com/SujalManjrekar

---

⭐ If you found this project useful, consider giving it a star!
