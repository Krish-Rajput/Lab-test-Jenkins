import os
from bs4 import BeautifulSoup

def test_registration_form():
    file_path = "index.html"
    assert os.path.exists(file_path), "index.html not found!"

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Check if form exists
    form = soup.find("form")
    assert form is not None, "Registration form element missing!"

    # Verify required input fields & submit button
    fields = ["studentName", "rollNumber", "email", "course"]
    for field in fields:
        elem = soup.find(id=field) or soup.find("input", {"name": field})
        assert elem is not None, f"Required input field '{field}' is missing!"

    submit_btn = soup.find("button", {"type": "submit"}) or soup.find("input", {"type": "submit"})
    assert submit_btn is not None, "Submit button is missing!"

    print("SUCCESS: All student registration form fields and submit button are present.")

if __name__ == "__main__":
    test_registration_form()