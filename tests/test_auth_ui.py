import os
from pathlib import Path
import sys
import pytest

sys.path.append(str(Path(__file__).parent.parent / "src"))

from auth_logic import register
from auth_ui import AuthFormUI, Button, TextField

TEST_FILE = "test_ui_users.json"


@pytest.fixture(autouse=True)
def cleanup():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


# --- 1. Test Text-field States (Default, Active, Error, Success, Disable) ---
def test_textfield_states_and_disable():
    field = TextField("Username")
    assert field.state == "Default"

    # พิมพ์ข้อความ -> Active
    assert field.set_value("my_user") is True
    assert field.state == "Active"

    # สั่ง Disable -> พิมพ์ไม่เข้า
    field.state = "Disable"
    assert field.set_value("new_user") is False
    assert field.value == "my_user"  # ค่าต้องเป็นค่าเดิม


# --- 2. Test Login UI Error and Success States ---
def test_login_ui_states():
    ui = AuthFormUI()
    register("existing_user", "correct_pass", db_file=TEST_FILE)

    # เคสกรอกรหัสผิด -> ช่อง Password ต้องขึ้น Error State
    ui.username_input.set_value("existing_user")
    ui.password_input.set_value("wrong_pass")
    assert ui.submit_login_ui(db_file=TEST_FILE) is False
    assert ui.password_input.state == "Error"
    assert ui.error_message == "Invalid password"

    # เคสกรอกรหัสถูก -> ช่อง Password ต้องขึ้น Success State
    ui.password_input.set_value("correct_pass")
    assert ui.submit_login_ui(db_file=TEST_FILE) is True
    assert ui.password_input.state == "Success"


# --- 3. Test Button Component (Primary, Secondary) ---
def test_button_component_types():
    ui = AuthFormUI()
    # ปุ่มหลักต้องเป็น Primary
    assert ui.submit_button.type == "Primary"


# --- 4. Test SSO Login Buttons (Google, Facebook, Apple) ---
def test_sso_login_buttons_included():
    ui = AuthFormUI()
    # ตรวจสอบปุ่ม SSO ทั้ง 3 แบรนด์ตาม Specification
    assert "Google" in ui.sso_buttons
    assert "Facebook" in ui.sso_buttons
    assert "Apple" in ui.sso_buttons

    for provider, btn in ui.sso_buttons.items():
        assert btn.enabled is True