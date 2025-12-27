import requests
import os

BASE_URL = "http://localhost:8001/api"

def test_auth():
    # 1. Register
    email = "test@example.com"
    password = "password123"
    
    print(f"Attempting to register user: {email}")
    try:
        register_payload = {
            "email": email,
            "password": password,
            "full_name": "Test User",
            "phone": "09123456789"
        }
        response = requests.post(f"{BASE_URL}/auth/register", json=register_payload)
        
        if response.status_code == 200:
            print("Registration successful!")
            print(response.json())
        elif response.status_code == 400 and "already registered" in response.text:
             print("User already registered, proceeding to login.")
        else:
            print(f"Registration failed: {response.status_code} - {response.text}")
            # If registration failed (not because of duplicate), we might stop here
            # But let's try login anyway in case it was a duplicate
            
    except Exception as e:
        print(f"Registration exception: {e}")

    # 2. Login
    print(f"\nAttempting to login user: {email}")
    try:
        login_payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{BASE_URL}/auth/login", json=login_payload)
        
        if response.status_code == 200:
            print("Login successful!")
            print(response.json())
        else:
            print(f"Login failed: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Login exception: {e}")

if __name__ == "__main__":
    test_auth()
