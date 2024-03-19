from kameleo.local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile
import playwright
from playwright.sync_api import sync_playwright
import time

client = KameleoLocalApiClient()
# Search for a mobile Base Profiles
base_profile_list = client.search_base_profiles(
    device_type='mobile',
    os_family='ios',
    browser_product='safari',
    language='en-us'
)

# Create a new profile with recommended settings
# Choose one of the Base Profiles
# Set the launcher to 'chromium' so the mobile profile will be started in Chroma (our custom built browser)
create_profile_request = BuilderForCreateProfile \
    .for_base_profile(base_profile_list[0].id) \
    .set_recommended_defaults() \
    .set_launcher('chromium') \
    .build()
profile = client.create_profile(body=create_profile_request)

# Start the profile
client.start_profile_with_options(profile.id, body={
    # This allows you to click on elements using the cursor when emulating a touch screen in the browser.
    # If you leave this out, your script may time out after clicks and fail.
    'additionalOptions': [
        {
            'key': 'disableTouchEmulation',
            'value': True,
        },
    ],
})

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
    page.goto('https://whoer.net')

client.stop_profile(profile.id)