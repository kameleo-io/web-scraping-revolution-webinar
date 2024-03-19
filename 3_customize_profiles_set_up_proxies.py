from kameleo.local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile
from playwright.sync_api import sync_playwright

client = KameleoLocalApiClient()
base_profiles = client.search_base_profiles(
    device_type='desktop', # change it to 'desktop' or 'mobile'
    os_family='windows', # change it to 'macos', 'windows', 'linux', 'android' or 'ios'
    browser_product='chrome',
    language='en-us'
)

# Create a new profile with recommended settings
# for browser fingerprinting protection
create_profile_request = BuilderForCreateProfile \
    .for_base_profile(base_profiles[0].id) \
    .set_recommended_defaults() \
    .set_webgl_meta('manual', { # I suggest you to use 'automatic' instead of 'manual'
            'vendor': 'NVIDIA',
            'renderer': 'GTX4050'
        }) \
    .set_proxy('socks5', {
        'host': 'gate.smartproxy.com',
        'port': 10000,
        'id': 'user-sp9b7bac04-session-3-sessionduration-30-country-us-postalcode-10001',
        'secret': 'etQtf9c89AStrmA2gn'
    }) \
    .set_web_rtc('manual', { # I suggest you to use 'automatic' instead of 'manual'
            'public_ip': '1.1.1.1',
            'private_ip': '192.168.0.1'
        }) \
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
    page.goto('https://browserleaks.com/webgl')
    page.goto('https://browserleaks.com/webrtc')

client.stop_profile(profile.id)