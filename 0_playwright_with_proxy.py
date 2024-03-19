from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, proxy={
        'server': 'us.smartproxy.com:10001',
        'username': 'user-sp9b7bac04-sessionduration-30',
        'password': 'etQtf9c89AStrmA2gn'
    })

    context = browser.new_context()
    page = context.new_page()
    page.goto('https://browserleaks.com/webrtc')
    browser.close()
