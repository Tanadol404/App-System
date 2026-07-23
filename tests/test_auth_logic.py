import os
from pathlib import Path
import sys
import pytest

sys.path.append(str(Path(__file__).parent.parent / "src"))

from auth_logic import login, register

TEST_FILE = "test_users.json"


@pytest.fixture(autouse=True)
def cleanup_test_file():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


# --- TEST 1: Register บันทึกลงไฟล์ + Login ผ่านด้วยข้อมูลนั้น ---
def test_register_saves_to_file_and_login_success():
    # 1. สมัครสมาชิก
    reg_status, reg_msg = register("customer1", "pass123", db_file=TEST_FILE)
    assert reg_status is True

    # 2. ต้องมีการสร้างไฟล์เก็บข้อมูลจริง
    assert os.path.exists(TEST_FILE) is True

    # 3. ลอง Login ด้วยข้อมูลที่เพิ่งสมัคร
    login_status, login_msg = login("customer1", "pass123", db_file=TEST_FILE)
    assert login_status is True
    assert login_msg == "Login successful"


# --- TEST 2: ไม่ Register User ซ้ำ ---
def test_register_duplicate_username_fails():
    register("customer1", "pass123", db_file=TEST_FILE)

    # สมัครด้วยชื่อเดิมซ้ำ
    status, msg = register("customer1", "new_password", db_file=TEST_FILE)
    assert status is False
    assert msg == "Username already exists"


# --- Test 3: ตรวจ Login พลาด ---
def test_login_failures():
    register("customer1", "pass123", db_file=TEST_FILE)

    # case 3.1: รหัสผ่านผิด
    status1, msg1 = login("customer1", "wrong_pass", db_file=TEST_FILE)
    assert status1 is False
    assert msg1 == "Invalid password"

    # case 3.2: ไม่มี Username ในระบบ
    status2, msg2 = login("ghost_user", "pass123", db_file=TEST_FILE)
    assert status2 is False
    assert msg2 == "User not found"