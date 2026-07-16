"""Appium driver factory with async support."""
import asyncio
from typing import Optional
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.webdriver import WebDriver
import config


def _build_android_options():
    """Build UiAutomator2 options from config caps."""
    options = UiAutomator2Options()
    options.load_capabilities(config.DESIRED_CAPS_ANDROID)
    return options


def _build_ios_options():
    """Build XCUITest options from config caps."""
    options = XCUITestOptions()
    options.load_capabilities(config.DESIRED_CAPS_IOS)
    return options


async def create_driver(platform: str = "Android") -> WebDriver:
    """
    Create and return an Appium WebDriver instance.

    Args:
        platform: 'Android' or 'iOS'

    Returns:
        Appium WebDriver connected to the Appium server
    """
    options = _build_android_options() if platform == "Android" else _build_ios_options()
    driver = await webdriver.Remote(config.APPIUM_SERVER, options=options)
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    return driver


class DriverContext:
    """Context manager for driver lifecycle."""

    def __init__(self, platform: str = "Android"):
        self.platform = platform
        self.driver: Optional[WebDriver] = None

    async def __aenter__(self):
        self.driver = await create_driver(self.platform)
        return self.driver

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.quit()
        return False
