from flask import Flask, request, abort
import re
import requests

app = Flask(__name__)
BACKEND_URL = "http://localhost:5001"

ATTACK_PATTERNS = [
    (r"([';]+(--|\#|\/\*))", "SQL Injection"),
    (r"[;|&$`]", "Command Injection"),
    (r"<script>|<\/script>|javascript:", "XSS"),
    (r"\b(UNION|SELECT|INSERT|DROP|EXEC)\b", "SQL Keywords"),
    (r"(\brm\b|\bwget\b|\bcurl\b)", "Dangerous Commands"),
]

def detect_attack(value):
    for pattern, name in ATTACK_PATTERNS:
        if re.search(pattern, value, re.IGNORECASE):
            return name
    return None

@app.before_request
def waf_check():
    for source in [request.args, request.form]:
        for key, value in source.items():
            if attack_type := detect_attack(str(value)):
                app.logger.warning(f"Blocked {attack_type} in {key}={value}")
                abort(403, description=f"Blocked by WAF: {attack_type}")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    resp = requests.request(
        method=request.method,
        url=f"{BACKEND_URL}/{path}",
        headers={key: value for key, value in request.headers},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False
    )
    return (resp.content, resp.status_code, resp.headers.items())

if __name__ == '__main__':
    app.run(port=5000)