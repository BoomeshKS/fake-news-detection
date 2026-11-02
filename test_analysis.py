import os

def authenticate_user(username, password):
    # 1. Hardcoded Secret (Security Risk)
    api_key = "sk-live-93821039812039812"
    
    # 2. SQL Injection Vulnerability (High Risk)
    query = f"SELECT * FROM accounts WHERE user = '{username}' AND pass = '{password}'"
    
    # 3. Definite Null/None Crash (Bug)
    records = None
    return records.strip()