1. File test_login.py
Strengths: Group 08 successfully implemented Data-Driven Testing using pytest.mark.parametrize for the login failure scenarios. This is a smart way to test multiple inputs like empty fields and wrong passwords without rewriting the entire test logic.

Weaknesses: They manually rewrote the navigation and setup steps inside the function instead of fully relying on the provided login helper.

2. File test_search.py
Strengths: Good logic in filtering books. They properly used a loop to check the category of every single book card displayed on the screen.

Weaknesses: There is a syntax error in the assertion message for the empty search result test. They forgot the f-string prefix. If the test fails, the log will print the raw code syntax instead of the actual number of books found.

3. File test_borrow_return.py
Strengths: Outstanding test coverage. They went beyond the basic requirements by testing edge cases like librarian overdue checks, expired members, and suspended members. Linking a known bug using the pytest xfail marker shows a great quality assurance mindset.

Weaknesses: A critical automation anti-pattern exists in the return book test. They hardcoded a specific receipt ID like BR001. This makes the test extremely flaky because it will break as soon as the database state changes.

4. File test_general.py
Strengths: Successfully verified UI state changes after logout and language switching. The text assertions are clear and accurate.

Weaknesses: The assertions could be more robust by waiting for specific elements to disappear rather than just checking for new text.

5. Bug
Here is a consolidated list of the actual code flaws found in the submission from Group 08:

Hardcoded Locators: The most critical error is hardcoding the ID BR001 in their return book test. This breaks the independence of the test and guarantees a crash if the library database is ever reset.

Missing f-string Formatting: In the search test file, an assertion message is missing the letter f at the beginning of the string. It will output variable names as literal text rather than their actual dynamic values.

Unnecessary Code Duplication: Despite having a login helper function, they repeatedly hardcoded the email input, password input, and click actions across multiple test files. This violates basic clean code principles and makes maintenance difficult.

6. General Comparison: Group 23 versus Group 08
Group 08 Profile: They have excellent theoretical knowledge and impressive test coverage. Their use of advanced testing markers and extra scenarios is commendable. However, their execution suffers from brittle locators, repeated code, and minor syntax carelessness.

Group 23 Profile: Our group focused on building a highly stable and practical test suite. By using dynamic relative locators like dot first and explicit state waits like waiting for an element to be hidden, our scripts are much more resilient.

Final Verdict: Group 08 wrote a broader suite, but Group 23 wrote a more reliable one. In a professional continuous integration pipeline, stability outweighs sheer volume. Therefore, the automation suite built by Group 23 is practically superior. overall score 15/20

7. link
Group23: https://github.com/USTH-STQA-2026/stqa-automation-testing-stqa-group-23
Group08: https://github.com/USTH-STQA-2026/stqa-automation-testing-stqa_group_08