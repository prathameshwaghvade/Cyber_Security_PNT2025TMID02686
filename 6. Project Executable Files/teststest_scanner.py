# tests/test_scanner.py
import pytest
from vulnerability_scanner.nessus_scanner import NessusScanner

def test_nessus_scanner():
    scanner = NessusScanner("https://nessus.example.com", "admin", "password")
    scanner.login()
    assert scanner.session is not None  # Ensure login is successful

