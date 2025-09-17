#!/usr/bin/env python3
"""
Test script for the Developer ChatBot API
Tests compatibility with the PHP consumer
"""

import requests
import json
from datetime import datetime

# API Configuration (matching PHP consumer)
BASE_URL = "http://127.0.0.1:8000"
AUTH_TOKEN = "EXPECTED_TOKEN"
ENDPOINT_MESSAGES = "/chat/messages"

def test_health_check():
    """Test the health check endpoint (for isAvailable() method)"""
    print("🏥 Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data['status']}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_chat_message(session="test-session", message="What programming languages does Leonard know?"):
    """Test the chat message endpoint (for submitMessage() method)"""
    print(f"💬 Testing chat message...")
    print(f"   Session: {session}")
    print(f"   Message: {message}")
    
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {AUTH_TOKEN}'
        }
        
        payload = {
            'session': session,
            'message': message
        }
        
        response = requests.post(
            f"{BASE_URL}{ENDPOINT_MESSAGES}",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat message successful!")
            print(f"   Response: {data['response'][:100]}...")
            print(f"   Session: {data['session']}")
            print(f"   Status: {data['status']}")
            return True
        else:
            print(f"❌ Chat message failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Chat message error: {e}")
        return False

def test_authentication():
    """Test authentication with invalid token"""
    print("🔐 Testing authentication...")
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer INVALID_TOKEN'
        }
        
        payload = {
            'session': 'test-session',
            'message': 'test message'
        }
        
        response = requests.post(
            f"{BASE_URL}{ENDPOINT_MESSAGES}",
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 401:
            print("✅ Authentication correctly rejected invalid token")
            return True
        else:
            print(f"❌ Authentication test failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Authentication test error: {e}")
        return False

def test_validation():
    """Test input validation"""
    print("✅ Testing input validation...")
    
    # Test empty message
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {AUTH_TOKEN}'
        }
        
        payload = {
            'session': 'test-session',
            'message': ''
        }
        
        response = requests.post(
            f"{BASE_URL}{ENDPOINT_MESSAGES}",
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 400:
            print("✅ Empty message correctly rejected")
        else:
            print(f"❌ Empty message validation failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Validation test error: {e}")

def main():
    """Run all tests"""
    print("🧪 Developer ChatBot API Test Suite")
    print("=" * 50)
    
    tests = [
        ("Health Check", test_health_check),
        ("Authentication", test_authentication),
        ("Input Validation", test_validation),
        ("Chat Message", test_chat_message),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Running: {test_name}")
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
        print("-" * 30)
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! API is ready for PHP consumer.")
    else:
        print("⚠️  Some tests failed. Check the API implementation.")

if __name__ == "__main__":
    main()
