from playwright.sync_api import sync_playwright
import time

def test_form_submission():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("file:///C:/Users/nitin/Desktop/Projects/GenAIPlaywright/exampleWebsite/index.html")
        time.sleep(1)

        page.fill('input[name="username"]', 'nitin')
        time.sleep(1)

        page.fill('input[name="password"]', 'password123')
        time.sleep(1)

        page.click('input[name="remember-me"]')
        time.sleep(1)

        page.click('button[name="Submit"]')

        time.sleep(1)

        browser.close()

if __name__ == "__main__":
    test_form_submission()