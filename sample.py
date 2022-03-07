from selenium import webdriver

HEADLESS_PROXY = "localhost:3128"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": HEADLESS_PROXY,
    "sslProxy": HEADLESS_PROXY,
    "proxyType": "MANUAL",
}

with webdriver.Firefox() as driver:
    driver.get("https://toscrape.com")
    driver.save_screenshot("screenshot.png")