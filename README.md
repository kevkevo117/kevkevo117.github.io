#Kevin Gonzalez Projects 


# 💸 Price Tracker App

A full-stack web app that lets users track product prices and get notified via Discord when prices drop below a specified discount threshold.

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

## ✍️ Author

**Kevin Gonzalez**  
Bachelor of Science in Cybersecurity, Augusta University  
Expected Graduation: December 2025
