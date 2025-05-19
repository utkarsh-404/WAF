from flask import Flask, render_template, request, redirect, url_for
from security import validate_input, safe_execute_ping

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Updated to accept GET and POST methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = validate_input(request.form.get('username', ''))
        password = validate_input(request.form.get('password', ''))
        return f"Login successful for {username}"
    return render_template('login.html')

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    result = None
    if request.method == 'POST':
        ip = validate_input(request.form.get('ip', ''))
        result = safe_execute_ping(ip)
    return render_template('ping.html', result=result)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  # Add debug mode