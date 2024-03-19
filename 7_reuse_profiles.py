from kameleo.local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.models import ImportProfileRequest
from playwright.sync_api import sync_playwright
import time
import os

client = KameleoLocalApiClient()

# Import profile with its persistent context
folder = os.path.dirname(os.path.realpath(__file__))
path = f'{folder}\\persistent-profile-demo.kameleo'
profile = client.import_profile(body=ImportProfileRequest(path=path))

# Start the browser
client.start_profile(profile.id)

# At this point you can automate the browser with your favorite framework
# Connect to the browser with Playwright through CDP
kameleo_port = 5050
browser_ws_endpoint = f'ws://localhost:{kameleo_port}/playwright/{profile.id}'
with sync_playwright() as playwright:
    browser = playwright.chromium.connect_over_cdp(endpoint_url=browser_ws_endpoint)
    context = browser.contexts[0]
    page = context.new_page()

    # Use any Playwright command to drive the browser
    # and enjoy full protection from bot detection products
    page.goto('https://mail.google.com/mail/u/0/#inbox')
    time.sleep(3)
    page.goto('https://www.youtube.com/@KameleoTeam')

client.stop_profile(profile.id)