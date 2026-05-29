"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 3 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 3 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - "Mượn / Trả" tab: role="tab", aria-label="Mượn / Trả"
    - Available books have "Có sẵn" in aria-label, borrowed books have "Đang mượn"
      (*Sách "Có sẵn" có aria-label chứa "Có sẵn", sách "Đang mượn" chứa "Đang mượn"*)
    - Borrow button: 'flt-semantics[role="button"]:has-text("Mượn sách này")'
      (*Nút mượn*)
    - After clicking "Mượn sách này", a confirmation dialog appears — click "Mượn" again
      (*Sau khi click "Mượn sách này" sẽ hiện dialog xác nhận — cần click nút "Mượn" lần nữa*)
    - Return button: 'flt-semantics[role="button"]:has-text("Trả sách")'
      (*Nút trả*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, wait_for_flutter, SCREENSHOT_DIR,
)


def test_borrow_book(page, test_config):
    """TC-08: Borrow an available book (*Mượn sách có trạng thái 'Có sẵn'*)

    COMPLETED

    Description (*Mô tả*):
        Log in → find an "Available" book → click "Mượn sách này" → confirm dialog
        → verify book status changes to "Borrowed".
        (*Đăng nhập → tìm sách "Có sẵn" → click "Mượn sách này" → xác nhận dialog
        → kiểm tra sách chuyển sang trạng thái "Đang mượn".*)

    Suggested steps (*Gợi ý các bước*):
        1. login(page, test_config)
        2. Find available book: page.locator('flt-semantics[role="group"][aria-label*="Có sẵn"]')
           (*Tìm sách Có sẵn*)
        3. Click "Mượn sách này" button inside that book card
           (*Click nút "Mượn sách này" trong sách đó*)
        4. Wait for confirmation dialog, re-enable semantics
           (*Đợi dialog xác nhận, bật lại semantics*)
        5. Click "Mượn" button (confirm button in dialog)
           (*Click nút "Mượn" — nút xác nhận trong dialog*)
        6. Assert: "Đang mượn" or "thành công" appears
           (*Assert: "Đang mượn" hoặc "thành công" xuất hiện*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    # 1.Đăng nhập bằng tài khoản chưa mượn sách
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "dam.tran@email.com")
    flutter_fill(page, "Mật khẩu", "password123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Trần Dựa Dẫm")
    # 2.Tìm sách "Có sẵn" và nhấn nút mượn
    wait_for_flutter(page, text="Có sẵn")
    page.locator('flt-semantics[role="button"]:has-text("Mượn sách này")').first.click()
    # Chờ dialog xác nhận bật lên và click nút "Mượn" 
    wait_for_flutter(page, text="Mượn")
    page.locator('flt-semantics[role="button"]:has-text("Mượn")').last.click()
    # 3.Đợi UI render lại trạng thái sách thành "Đang mượn"
    wait_for_flutter(page, text="Đang mượn")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc08_borrow_success.png"))
    # 4.Kiểm tra trạng thái "Đang mượn" xuất hiện trong semantics tree
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đang mượn" in sem_text, "Lỗi: Trạng thái sách không chuyển sang 'Đang mượn' sau khi thao tác"


def test_view_borrowed_books(page, test_config):
    """TC-09: View borrowed books list (*Xem danh sách sách đang mượn — tab Mượn / Trả*)

    COMPLETED

    Description (*Mô tả*):
        Log in → switch to "Mượn / Trả" tab → verify borrowed books are shown.
        (*Đăng nhập → chuyển sang tab "Mượn / Trả" → kiểm tra có sách đang mượn.*)

    Hints (*Gợi ý*):
        - Click tab: page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
        - Verify: books with "Đang mượn" in aria-label, or "Trả sách" button exists
          (*Kiểm tra: có sách với aria-label chứa "Đang mượn" hoặc có nút "Trả sách"*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    # 1.Đăng nhập bằng tài khoản ba.nguyen
    login(page, test_config)
    # 2.Chuyển sang tab "Mượn / Trả"
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    # 3.Đợi các element của phiếu mượn xuất hiện
    wait_for_flutter(page, text="Trả sách")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc09_view_borrowed_books.png"))
    # 4.Kiểm tra danh sách hiển thị phiếu mượn
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Trả sách" in sem_text or "Đang mượn" in sem_text, "Lỗi: Không tìm thấy phiếu mượn nào trong tab Mượn / Trả"


def test_return_book(page, test_config):
    """TC-10: Return a borrowed book (*Trả sách đang mượn*)

    COMPLETED

    Description (*Mô tả*):
        Log in → go to "Mượn / Trả" tab → click "Trả sách" → verify book is returned.
        (*Đăng nhập → tab "Mượn / Trả" → click "Trả sách" → kiểm tra sách được trả.*)

    Hints (*Gợi ý*):
        - Switch to "Mượn / Trả" tab (*Chuyển tab "Mượn / Trả"*)
        - Find return button: page.locator('flt-semantics[role="button"]:has-text("Trả sách")')
          (*Tìm nút "Trả sách"*)
        - Click and verify status change or success message
          (*Click và kiểm tra sách chuyển trạng thái hoặc có thông báo thành công*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    # 1.Đăng nhập với tài khoản ba.nguyen và chuyển qua tab "Mượn / Trả"
    login(page, test_config)
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    wait_for_flutter(page, text="Trả sách")
    # 2.Lấy nút Trả sách đầu tiên và click
    return_btn = page.locator('flt-semantics[role="button"]:has-text("Trả sách")').first
    return_btn.click()
    # 3.Đợi nút "Trả sách" đó biến mất khỏi DOM
    return_btn.wait_for(state="hidden", timeout=5000)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc10_return_success.png"))
    # 4.Xác nhận việc trả sách cập nhật UI chính xác
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Trả sách" not in sem_text or "Có sẵn" in sem_text, "Lỗi: Sách chưa được trả thành công, nút 'Trả sách' vẫn còn tồn tại"
