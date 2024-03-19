from kameleo.local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile

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
    .build()
profile = client.create_profile(body=create_profile_request)

# Start the browser
client.start_profile(profile.id)
client.stop_profile(profile.id)

# At this point you can automate the browser with your favorite framework