import subprocess
import re

def validate_input(input_str):
    cleaned = re.sub(r"[;|&$`<>]", "", input_str)
    return cleaned[:100]

def safe_execute_ping(ip):
    if not re.match(r"^[a-zA-Z0-9\.\-]+$", ip):
        return "Invalid IP address"
    
    try:
        result = subprocess.run(
            ['ping', '-c', '4', ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"