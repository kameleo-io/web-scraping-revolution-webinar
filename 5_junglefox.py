from kameleo.local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile
from playwright.sync_api import sync_playwright
import time
import os

client = KameleoLocalApiClient()
base_profiles = client.search_base_profiles(
    device_type='desktop',
    os_family='windows',
    browser_product='firefox',
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
    # The exact path to the bridge executable is subject to change. Here, we use %LOCALAPPDATA%\Programs\Kameleo\pw-bridge.exe
    executable_path_example = os.path.expandvars(r'%LOCALAPPDATA%\Programs\Kameleo\pw-bridge.exe')
    browser = playwright.firefox.launch_persistent_context(
        '',
        # The Playwright framework is not designed to connect to already running
        # browsers. To overcome this limitation, a tool bundled with Kameleo, named
        # pw-bridge.exe will bridge the communication gap between the running Firefox
        # instance and this playwright script.
        executable_path=executable_path_example,
        args=[f'-target {browser_ws_endpoint}'],
        viewport=None)

    # Kameleo will open the a new page in the default browser context.
    # NOTE: We DO NOT recommend using multiple browser contexts, as this might interfere
    #       with Kameleo's browser fingerprint modification features.
    page = browser.new_page()

    # Use any Playwright command to drive the browser
    # and enjoy full protection from bot detection products
    page.goto('https://www.harrods.com')
    time.sleep(2)
    page.click('text=Women')

client.stop_profile(profile.id)