"""
Search & Filter Tests (Kiểm thử Tìm kiếm & Lọc sách) — Library Book Borrowing System (Hệ thống Mượn sách thư viện)

Students must complete ALL 4 test cases in this file.
(Sinh viên cần hoàn thành TẤT CẢ 4 test case trong file này.)

Hints (Gợi ý):
    - After logging in, use flutter_fill() to type into the search box
      (Sau khi đăng nhập, dùng flutter_fill() để nhập vào ô tìm kiếm)
    - Search box aria-label: "Tìm kiếm theo tên sách hoặc tác giả..."
    - Category filter aria-label: "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    - Each book card has role="group" and aria-label containing book info
      (Mỗi card sách có role="group" và aria-label chứa thông tin sách)
    - Use login() helper from conftest.py to log in before testing
      (Dùng login() helper từ conftest.py để đăng nhập trước khi test)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter,
)


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found (Tìm kiếm sách theo tên — tìm thấy kết quả)

    🟢 COMPLETED (ĐÃ HOÀN THÀNH)

    Description (Mô tả):
        Log in → search keyword "Flutter" → verify Flutter books appear in results.
        (Đăng nhập → tìm kiếm từ khóa "Flutter" → kiểm tra có sách Flutter trong kết quả.)
    """
    # 1. Access the web dashboard using predefined configuration files
    login(page, test_config)
    
    # 2. Input search criteria targeting known inventory records
    search_label = "Tìm kiếm theo tên sách hoặc tác giả..."
    flutter_fill(page, search_label, "Flutter")
    
    # 3. Leverage smart visibility assertions to wait for tree canvas operations
    wait_for_flutter(page, text="Flutter")
    
    # 4. Enforce validation rule mapping back to test suite criteria
    books_found = page.locator('flt-semantics[aria-label*="Flutter"]')
    assert books_found.count() > 0, "Expected target book entries containing 'Flutter' in semantic attributes."


def test_search_book_no_result(page, test_config):
    """TC-05: Search book – no results (Tìm kiếm sách — không có kết quả)

    🟢 COMPLETED (ĐÃ HOÀN THÀNH)

    Description (Mô tả):
        Log in → search a non-existent keyword (e.g. "xyz_khong_ton_tai_12345")
        → verify no books are displayed.
        (Đăng nhập → tìm kiếm từ khóa không tồn tại → kiểm tra không có sách nào hiển thị.)
    """
    # 1. Access the web dashboard using predefined configuration files
    login(page, test_config)
    
    # 2. Execute query utilizing a string certain to miss inventory matching indices
    search_label = "Tìm kiếm theo tên sách hoặc tác giả..."
    flutter_fill(page, search_label, "xyz_khong_ton_tai_12345")
    
    # 3. Maintain synchronization using semantic node lookup engines
    wait_for_flutter(page, text="Không tìm thấy sách")
    
    # 4. Verify system bounds drop active display elements to exactly zero
    displayed_books_count = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count()
    assert displayed_books_count == 0, f"Expected 0 inventory rows rendered, found: {displayed_books_count}"


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ' (Lọc sách theo thể loại 'Công nghệ')

    🟢 COMPLETED (ĐÃ HOÀN THÀNH)

    Description (Mô tả):
        Log in → enter "Công nghệ" in the category filter → verify all displayed books
        belong to the "Công nghệ" category.
        (Đăng nhập → nhập "Công nghệ" vào ô lọc thể loại → kiểm tra tất cả sách
        hiển thị đều thuộc thể loại Công nghệ.)
    """
    # 1. Access the web dashboard using predefined configuration files
    login(page, test_config)
    
    # 2. Feed categorization target metrics into form criteria
    filter_label = "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    flutter_fill(page, filter_label, "Công nghệ")
    
    # 3. Allow execution filters to finalize layout manipulation
    wait_for_flutter(page, text="Công nghệ")
    
    # 4. Query current matching group structural blocks within viewport bounds
    book_locator = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    total_books = book_locator.count()
    
    # 5. Enforce system return expectations
    assert total_books > 0, "No inventory matching categorization string 'Công nghệ' was captured."
    
    # 6. Iteratively evaluate structural attributes across response elements to prove isolation
    for i in range(total_books):
        aria_label = book_locator.nth(i).get_attribute("aria-label")
        assert "Công nghệ" in aria_label, f"Mismatch found at position index {i}. Text content reads: {aria_label}"


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name (Tìm kiếm sách theo tên tác giả)

    🟢 COMPLETED (ĐÃ HOÀN THÀNH)

    Description (Mô tả):
        Log in → search author name (e.g. "Nguyễn Minh Đức") → verify results found.
        (Đăng nhập → tìm kiếm tên tác giả → kiểm tra có kết quả.)
    """
    # 1. Access the web dashboard using predefined configuration files
    login(page, test_config)
    
    # 2. Populate input parameters with targeted validation components
    search_label = "Tìm kiếm theo tên sách hoặc tác giả..."
    author_keyword = "Nguyễn Minh Đức"
    flutter_fill(page, search_label, author_keyword)
    
    # 3. Synchronize rendering states using structural search utilities
    wait_for_flutter(page, text=author_keyword)
    
    # 4. Enforce accuracy validation check across returned semantic items
    author_matches = page.locator(f'flt-semantics[aria-label*="{author_keyword}"]')
    assert author_matches.count() > 0, f"Expected active search structures matching author metadata: '{author_keyword}'."