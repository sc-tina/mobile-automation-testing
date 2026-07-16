"""Desired capabilities configuration for mobile automation."""

DESIRED_CAPS_ANDROID = {
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "Android Emulator",
    "app": "./apps/sample.apk",
    "automationName": "UiAutomator2",
    "newCommandTimeout": 300,
    "autoGrantPermissions": True,
    "noReset": False,
    "fullReset": False,
}

DESIRED_CAPS_IOS = {
    "platformName": "iOS",
    "platformVersion": "17.0",
    "deviceName": "iPhone 15 Simulator",
    "app": "./apps/sample.app",
    "automationName": "XCUITest",
    "newCommandTimeout": 300,
    "autoAcceptAlerts": True,
    "noReset": False,
}

APPIUM_SERVER = "http://127.0.0.1:4723"
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20
SCREENSHOT_DIR = "./screenshots/"
LOG_DIR = "./logs/"
