from kameleo.local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile
from playwright.sync_api import sync_playwright
import time

client = KameleoLocalApiClient()
base_profiles = client.search_base_profiles(
    device_type='desktop',
    os_family='windows',
    browser_product='chrome',
    language='en-us'
)

# Create a new profile with recommended settings
# for browser fingerprinting protection
create_profile_request = BuilderForCreateProfile \
    .for_base_profile(base_profiles[0].id) \
    .set_recommended_defaults() \
    .build()
profile = client.create_profile(body=create_profile_request)

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
    page.goto('https://www.harrods.com')
    time.sleep(2)
    page.click('text=Women')

client.stop_profile(profile.id)