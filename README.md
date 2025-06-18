Projects of Kevin Gonzalez

## 🔐 Penetration Testing Report

This project simulates a black-box penetration test on the fictional company provided by the professor. It includes reconnaissance, scanning, enumeration, exploitation, and post-exploitation. The goal was to assess network and web application vulnerabilities, document the process, and provide mitigation strategies.

**🔧 Some Tools Used:**
- **Nmap** – Network discovery and port scanning
- **Nikto** – Web vulnerability scanner
- **Metasploit** – Exploitation framework
- **Burp Suite** – Web proxy and attack tool
- **Hydra** – Brute-force attack utility

📄 [View Full Report (Google Docs)](https://docs.google.com/document/d/1oPtdPgLX7t0ZilJpxZvbXmD-jCJgctxd2UcIq0iF7zE/edit?usp=drive_link)

👉 [View detailed project breakdown](./pen-test.md)


## 🕵️ Digital Forensics Analysis Report

This digital forensics project simulates a real-world investigation into a compromised Windows system. The analysis involved identifying malicious activity, examining user artifacts, recovering deleted files, and generating a formal forensic report.

**🔧 Tools Used:**
- **Autopsy** – For timeline analysis and artifact recovery
- **FTK Imager** – For creating forensic disk images
- **Volatility** – Memory analysis to detect malicious processes
- **Wireshark** – Packet inspection for suspicious traffic
- **Hayabusa** - Windows event log fast forensics timeline generator and threat hunting tool
- **KAPE** - A Kroll Artifact Parser/Extractor

📄 [View Full Report (Google Docs)](https://docs.google.com/document/d/1oPtdPgLX7t0ZilJpxZvbXmD-jCJgctxd2UcIq0iF7zE/edit?usp=sharing)

👉 [View detailed project breakdown](./forensics-analysis.md)


# 💬 Response Simulator

This is a simple Python project that simulates incoming messages and offers a selection of suggested replies. The user's chosen response is logged with a timestamp in a file called `response_log.txt`.

## 🚀 Features

- Simulates realistic incoming work messages.
- Provides 3 random suggested replies to choose from.
- Logs the chosen response with a timestamp.
- Easy to extend or modify message and response templates.

## 🛠️ How to Run

1. **Make sure you have Python 3 installed.**
2. Clone or download this repository.
3. Navigate to the project directory in your terminal.
4. Run the script:

```bash
python response_simulator.py
