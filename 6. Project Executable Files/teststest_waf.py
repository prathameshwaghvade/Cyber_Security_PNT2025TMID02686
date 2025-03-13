# tests/test_waf.py
import pytest
from waf.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_waf_block_sql_injection(client):
    """Test that SQL injection is blocked by the WAF"""
    response = client.post('/login', data={'username': "' OR 1=1 --", 'password': "password"})
    assert response.status_code == 403  # Blocked due to SQL Injection
