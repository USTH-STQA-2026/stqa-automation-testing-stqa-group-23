"""
Logout & Language Tests (*Kiểm thử Đăng xuất & Chuyển ngôn ngữ*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)
"""
import os
import pytest
from conftest import (
    flutter_click_button,
    login, wait_for_flutter, SCREENSHOT_DIR,
)

def test_logout(page, test_config):
    """TC-11: Đăng xuất thành công"""
    # 1. Đăng nhập trước
    login(page, test_config)

    # 2. Nhấn nút Đăng xuất
    flutter_click_button(page, "Đăng xuất")

    # 3. Chờ hệ thống quay về trang đăng nhập
    wait_for_flutter(page, text="Đăng nhập")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "logout_success.png"))

    # 4. Assert: Chỉ cần kiểm tra có chữ "Đăng nhập" là đủ xác nhận đã out
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đăng nhập" in sem_text, "Không tìm thấy chữ Đăng nhập sau khi Log out"


def test_switch_language_to_english(page, test_config):
    """TC-12: Chuyển ngôn ngữ sang tiếng Anh"""
    # 1. Đăng nhập vào hệ thống
    login(page, test_config)

    # 2. Click nút chuyển sang tiếng Anh
    flutter_click_button(page, "EN")

    # 3. Chờ nút "Sign out" xuất hiện (vì web dùng chữ Sign out thay cho Logout)
    wait_for_flutter(page, text="Sign out")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "switch_language_en.png"))

    # 4. Assert: Kiểm tra các từ khóa menu cốt lõi đã thành tiếng Anh
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Sign out" in sem_text or "Borrow this book" in sem_text