import sys
from pathlib import Path
from unittest.mock import MagicMock
import pytest

sys.path.append(str(Path(__file__).parent.parent))

from main import AuthLogin, AuthRegister

def test_auth_register_data():
    """ทดสอบฟังก์ชัน register_data ว่าดึงค่าจาก UI IDs ได้ถูกต้อง"""
    screen = AuthRegister()
    
    # จำลอง (Mock) IDs ของ Kivy TextInput
    screen.ids = {
        'name_input_reg': MagicMock(text="John Doe"),
        'email_input_reg': MagicMock(text="john@example.com"),
        'pass_input_reg': MagicMock(text="123456"),
        'conpass_input_reg': MagicMock(text="123456")
    }
    
    # รันฟังก์ชัน (ถ้าไม่มี exception ถือว่าผ่าน)
    try:
        screen.register_data()
        assert True
    except Exception as e:
        pytest.fail(f"register_data raised an exception: {e}")

def test_auth_login_data():
    """ทดสอบฟังก์ชัน login_data"""
    screen = AuthLogin()
    
    screen.ids = {
        'email_input_login': MagicMock(text="john@example.com"),
        'pass_input_login': MagicMock(text="123456")
    }
    
    try:
        screen.login_data()
        assert True
    except Exception as e:
        pytest.fail(f"login_data raised an exception: {e}")
