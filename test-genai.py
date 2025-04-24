from playwright.sync_api import sync_playwright
from genai import generateTest
import time

webpage = r"C:\Users\nitin\Desktop\Projects\GenAIPlaywright\exampleWebsite\index.html"
def test_login():
    """
    Test the generateTest function on a Wikipedia page.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(webpage)
        time.sleep(2)

        generateTest("Enter nitin in username field", page)
        time.sleep(2)

        generateTest("Enter password123 in password field", page)
        time.sleep(2)

        generateTest("Check the remember me checkbox", page)
        time.sleep(2)

        generateTest("Click on the button named Submit", page)
        time.sleep(3)
        
        browser.close()

test_login()