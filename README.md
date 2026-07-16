# Mobile Automation Testing Toolkit

A lightweight, practical toolkit for automating mobile app UI testing. Supports Android via Appium + UIAutomator2 and iOS via XCUITest. Written in Python 3 with async support.

## Features

- Cross-platform mobile UI automation (Android & iOS)
- Page Object Model (POM) design pattern
- Screenshots on failure with timestamp
- Logging with structured output
- Parallel test execution support
- Built-in wait utilities with fluent assertions

## Requirements

- Python 3.8+
- Node.js 18+ (for Appium server)
- Android SDK or iOS Simulator / Real Device

## Installation

\\\ash
pip install appium-python-client selenium pytest pytest-asyncio
npm install -g appium
\\\

## Quick Start

1. Start Appium server:
\\\ash
appium --address 127.0.0.1 --port 4723
\\\

2. Connect your device (USB debugging enabled for Android)

3. Run a sample test:
\\\ash
python -m pytest tests/ -v
\\\

## Project Structure

\\\
.
\-\- core/
│   \-\- driver.py        # Appium driver setup
│   \-\- base_page.py     # Base page object
│   \-\- wait_utils.py    # Custom wait utilities
\-\- pages/               # Page Object files
\-\- tests/               # Test cases
\-\- utils/               # Helpers (screenshots, logs)
\-\- config.py            # Desired capabilities
\-\- conftest.py          # Pytest fixtures
\-\- requirements.txt
\-\- README.md
\\\

## Core Code Example

\\\python
import asyncio
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

CAPS = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "./apps/sample.apk",
    "automationName": "UiAutomator2",
    "noReset": True
}

async def get_driver():
    options = UiAutomator2Options().load_capabilities(CAPS)
    return await webdriver.Remote("http://localhost:4723", options=options)

async def example_test():
    driver = await get_driver()
    try:
        el = driver.find_element(AppiumBy.ID, "com.example:id/btn_login")
        el.click()
        assert "logged" in driver.page_source.lower()
    finally:
        driver.quit()

if __name__ == "__main__":
    asyncio.run(example_test())
\\\

## Config

Edit \config.py\ to set your desired capabilities:

\\\python
DESIRED_CAPS = {
    "platformName": "Android",       # or "iOS"
    "platformVersion": "14",          # Android/iOS version
    "deviceName": "Pixel_6",
    "app": "./apps/your-app.apk",
    "automationName": "UiAutomator2", # or "XCUITest"
    "newCommandTimeout": 300,
    "autoGrantPermissions": True
}
\\\

## Page Object Pattern

\\\python
from core.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (AppiumBy.ID, "com.example:id/et_username")
    PASSWORD = (AppiumBy.ID, "com.example:id/et_password")
    SUBMIT   = (AppiumBy.ID, "com.example:id/btn_submit")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.tap(self.SUBMIT)
        self.assert_visible("Home")
\\\

## License

MIT License

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

**Website**: https://www.qtphone.com/
**WhatsApp**: @along915
**Telegram**: @Alongyun
**Email**: ailong9281@gmail.com