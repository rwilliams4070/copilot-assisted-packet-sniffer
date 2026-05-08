import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from redaction import mask_ip, redact_sensitive_data

def test_mask_ip():
    assert mask_ip("192.168.1.55") == "192.168.1.xxx"

def test_redact_email():
    text = "email=test@example.com"
    result = redact_sensitive_data(text)
    assert "[REDACTED_EMAIL]" in result

def test_redact_password():
    text = "password=secret123"
    result = redact_sensitive_data(text)
    assert "password=[REDACTED]" in result

def test_redact_token():
    text = "token=abc123"
    result = redact_sensitive_data(text)
    assert "token=[REDACTED]" in result
