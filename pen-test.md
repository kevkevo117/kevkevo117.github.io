# 🛡️ Penetration Test Report: KevoCorp (Simulated Black Box Assessment)

## 🧠 Project Overview

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

## ✍️ Author

**Kevin Smith**  
Bachelor of Science in Cybersecurity, Augusta University  
Expected Graduation: December 2025