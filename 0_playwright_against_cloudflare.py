from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)  # Set headless=False to see the browser UI
    page = browser.new_page()
    page.goto('https://www.harrods.com')
    time.sleep(2)
    page.click('text=Women')
    browser.close()