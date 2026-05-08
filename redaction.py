import re

def mask_ip(ip):
    parts = ip.split(".")
    if len(parts) == 4:
        return f"{parts[0]}.{parts[1]}.{parts[2]}.xxx"
    return ip

def redact_sensitive_data(text):
    text = re.sub(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+', '[REDACTED_EMAIL]', text)

    text = re.sub(r'password=[^& ]+', 'password=[REDACTED]', text)

    text = re.sub(r'token=[^& ]+', 'token=[REDACTED]', text)

    text = re.sub(r'Authorization:.*', 'Authorization: [REDACTED]', text)

    text = re.sub(r'Cookie:.*', 'Cookie: [REDACTED]', text)

    return text
