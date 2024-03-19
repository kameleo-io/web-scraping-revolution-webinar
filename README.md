# Web Scraping Revolution Webinar
On 2024-03-20 we created a webinar with Pierluigi Vinciguerra from The Web Scraping Club. During the webinar our CEO showcased Kameleo. Here we share the code that was used during the demo.

>To run the following code examples, you need to run Kameleo.CLI.exe on your machine.

### 0_playwright_against_cloudflare
We use regular playwright to start chrome and visit harrods.com website, that has advanced bot-detection. After clicking on a menu item the browser gets detected.

### 0_playwright_with_proxy
We set up a proxy for the browser that is started by playwright. We showcase a WebRTC Leak on [Browserleaks.com](https://browserleaks.com/webrtc)

### 1_create_the_first_profile
We showcase how you can create a Kameleo virtual browser profile. For more info, check out our [Getting Started guide](https://help.kameleo.io/hc/en-us/articles/4418166326417-Getting-started-with-Kameleo-Automation).

### 2_use_playwright_to_contol_the_browser
Now we control Chroma (browser started by Kameleo) with Playwright. On harrods.com we can scrape data without any issue, despite they are using an advanced bot detection system.

### 3_customize_profiles_set_up_proxies
A couple of examples on how you can customize the browser fingerprint of a Kameleo browser profile. Also showcasing how to set up a proxy.
> We recommend you to only changing the proxy settings and keep every config option on the recommended defaults.

### 4_intelligent_canvas
Showcasing the [Intelligent Canvas Spoofing](https://help.kameleo.io/hc/en-us/articles/7021925786397-Intelligent-Canvas-Spoofing-Our-research-on-canvas) in Kameleo. Thanks to this feature websites with canvas fingerprinting won't detect the host machine's OS. Please read the linked article for more insights.

### 5_junglefox
We ship Kameleo with 2 separate, custom-built browsers: Chroma and Junglefox. If one of the browsers is not working, it worth trying the other. IN this example we visit harrods.com with a firefox profile, that is emulated in Junglefox.

### 6_mobile_profiles
Sometimes you need to emulate mobile profiles for your tasks. This is also possible with Kameleo, emulate any Android or iOS profiles.

### 7_reuse_profiles
Ever needed to run profiles with persistent context? Needed to scrape data behind a login wall? With Kameleo you can simply import a previously exported profile. In this example we are loading a profile that is already logged in to Gmail and YouTube.
> The imported .kameleo profile is not part of the repository for data privacy reasons 