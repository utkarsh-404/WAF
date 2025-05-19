# Web Application Firewall (WAF) Demonstration Project

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A practical demonstration of a Web Application Firewall protecting against common web vulnerabilities like SQL Injection, Command Injection, and XSS attacks.

![WAF Demo Screenshot](screenshot.png)

## Features

- Real-time request filtering
- Protection against:
  - SQL Injection
  - Command Injection
  - Cross-Site Scripting (XSS)
  - Path Traversal
- Interactive demo forms
- Secure backend implementation
- Responsive Search Bar

## Prerequisites

- Python 3.10+
- pip package manager
- Modern web browser

## Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/utkarsh-404/WAF
cd WAF
```

2. **Install dependencies**
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. **Run the application**
```bash
# Terminal 1 - Backend Server
python app.py

# Terminal 2 - WAF Proxy
python waf_proxy.py
```

4. **Access the application**
```text
Frontend: http://localhost:5000
Backend:  http://localhost:5001
```

## Testing Attacks

Try these payloads in the demo forms:

### SQL Injection
```sql
' OR 1=1 --
UNION SELECT username, password FROM users --
```

### Command Injection
```bash
; ls -la
127.0.0.1 && whoami
```

### XSS
```html
<script>alert(1)</script>
javascript:alert(document.cookie)
```

## Project Structure
```
├── app.py             # Secure backend application
├── waf_proxy.py       # WAF middleware
├── security.py        # Security utilities
├── requirements.txt   # Dependencies
├── static/            # CSS/JS assets
├── templates/         # HTML templates
└── README.md          # Documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Open a pull request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Security Note

This is a demonstration project only. Do not use with:
- Real user data
- Production systems
- Sensitive information
