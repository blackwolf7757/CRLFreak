# 🧨 CRLFreak – CRLF Injection Scanner

![CRLFreak Logo](https://your-logo-url.com/logo.png) <!-- Replace with your actual logo URL -->

**CRLFreak** is a lightweight, dependency-free Python tool designed for ethical penetration testers to detect **CRLF injection vulnerabilities** across web applications. It crawls a target domain, extracts URLs and parameters, and injects a curated set of payloads to identify header manipulation, response splitting, and log poisoning risks.

---
_____________________________________________________________________________________________________________________________

## 🚀 Features

- 🔍 Crawls all internal links from a target URL
- 🧪 Injects multiple impactful CRLF payloads
- 📡 Tests query parameters for header injection
- 🧾 Detects reflected headers like `Set-Cookie`, `Location`, `X-Injection-Test`
- 🛠️ No external dependencies – pure Python standard library
- 🧠 Designed for ethical testing in authorized environments

---
_____________________________________________________________________________________________________________________________

## 🧪 Payloads Used
_____________________________________________________________________________________________________________________________

```plaintext
%0d%0aSet-Cookie:crlf=1
%0a%0dSet-Cookie:crlf=1
%0d%0aX-Injection-Test:1
%0d%0aContent-Length:0
%0d%0aLocation:evil.com
%0d%0aRefresh:0;url=http://evil.com
%0d%0aAccess-Control-Allow-Origin:*
%0d%0aX-Forwarded-For:evil.com
````
_____________________________________________________________________________________________________________________________

📦 Installation
No installation required. Just clone the repo and run:
git clone https://github.com/yourusername/crlfreak.git
cd crlfreak
python3 crlf_scanner.py
_____________________________________________________________________________________________________________________________

🧭 Usage

$ python3 crlf_scanner.py
Enter target URL: https://example.com

The tool will:
1) Crawl all internal links from the target
2) Extract query parameters
3) Inject CRLF payloads
4) Report any reflected headers or anomalies

_____________________________________________________________________________________________________________________________
⚖️ Ethical Usage

This tool is intended for authorized security assessments only. Do not use CRLFreak on systems without explicit permission. Unauthorized scanning is illegal and unethical.
