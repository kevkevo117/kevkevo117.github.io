#Kevin Gonzalez Projects 


# 💸 Price Tracker App 

A work in progress full-stack web app that lets users track product prices and get notified via Discord when prices drop below a specified discount threshold.

---

## 🧠 Features

- ✅ Add any product URL and set your desired discount percentage
- ✅ Scrapes the page to extract name, site, and price
- ✅ Periodic (hourly) price checks in the background
- ✅ Sends alerts to your **Discord server** via webhook
- ✅ Web dashboard to view tracked items
- ✅ “Add to Cart” link redirects to the store

---

## 🛠 Technologies Used

- **Python + Flask** (web server)
- **BeautifulSoup** (scraping)
- **SQLite** (lightweight database)
- **JavaScript** (frontend fetch + interactivity)
- **Discord Webhooks** (notifications)

---

[Usage Guide: Dashboard Template](usage-guide.md)

---

# 🕵️ Digital Forensics Project: Windows System Compromise Investigation

## 🧠 Brief Project Overview

This project presents a forensic analysis of a compromised Windows system. It replicates a scenario in which an internal workstation exhibited signs of unusual behavior and potential compromise. The investigation followed the forensic process of evidence preservation, analysis, interpretation, and reporting.

---

## 🔧 Main Tools Used

- **Autopsy**: Used for analyzing file system artifacts and building a timeline of user and system activity.
- **FTK Imager**: For creating and mounting forensic disk images.
- **Volatility Framework**: Memory dump analysis to detect signs of malware and anomalous behavior.
- **Wireshark**: Network packet analysis to identify suspicious or malicious traffic.

---

## 🔍 Key Findings

- **Suspicious EXE File**: A malicious executable was found in the Downloads folder, not whitelisted by the system.
- **Deleted Files Recovered**: Several deleted files were found containing suspicious PowerShell scripts.
- **Suspicious Registry Changes**: Evidence of startup persistence and unauthorized registry edits.
- **Network Traffic**: Wireshark logs indicated beaconing activity to an external IP, consistent with C2 behavior.

---

## 💡 Recommendations

- Reimage affected systems and block known malicious IPs.
- Update antivirus definitions and perform a network-wide malware sweep.
- Apply user access controls and disable PowerShell for non-administrators.
- Regularly audit workstation logs and system startup entries.

---

## 📄 Full Report

[Click here to view the full PDF report in Google Docs](https://docs.google.com/document/d/1oPtdPgLX7t0ZilJpxZvbXmD-jCJgctxd2UcIq0iF7zE/edit?usp=sharing)

---

# 🛡️ Penetration Test Report: Kevin Gonzalez (Simulated Black Box Assessment)

## 🧠A Brief Project Overview

This project represents a simulated black-box penetration test targeting the fictional organization “KevoCorp.” The engagement followed the five standard phases of ethical hacking: reconnaissance, scanning, enumeration, exploitation, and post-exploitation. It was conducted to evaluate the company’s security posture and deliver actionable mitigation strategies.

---

## 🔧 Tools Used

- **Nmap**: For network scanning, port enumeration, and service identification.
- **Nikto**: To discover misconfigurations and outdated web services.
- **Burp Suite**: For intercepting and manipulating web traffic and testing input validation.
- **Metasploit**: To automate exploitation of discovered vulnerabilities.
- **Hydra**: For brute-force attacks against login interfaces.

---

## 🔎 Key Findings

- **Open Ports Discovered**: 21 (FTP), 22 (SSH), 80 (HTTP)
- **FTP Anonymous Login Enabled**: Allowed access to internal documentation.
- **Outdated Apache Web Server**: Vulnerable to known exploits.
- **No Input Validation on Web Form**: Enabled potential XSS or command injection.
- **Weak SSH Credentials**: Successfully brute-forced with Hydra.

---

## 💡 Recommendations

- Disable anonymous FTP access.
- Patch and update Apache to the latest stable version.
- Implement strong input validation and sanitization.
- Enforce strong password policies and lockout mechanisms.
- Conduct regular vulnerability scans and security awareness training.

---

## 📄 Full Report

[Click here to view the full PDF report in Google Docs](https://docs.google.com/document/d/1oPtdPgLX7t0ZilJpxZvbXmD-jCJgctxd2UcIq0iF7zE/edit?usp=drive_link)

---
