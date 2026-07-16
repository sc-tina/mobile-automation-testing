"""Base page object with common UI interaction methods."""
import time
from typing import Tuple, Optional
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import config


class BasePage:
    """Base page object for all page classes."""

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    def find(self, locator: Tuple[str, str]):
        """Find a single element with explicit wait."""
        return self._wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator: Tuple[str, str]):
        """Find a clickable element."""
        return self._wait.until(EC.element_to_be_clickable(locator))

    def tap(self, locator: Tuple[str, str]):
        """Tap an element."""
        el = self.find_clickable(locator)
        el.click()
        return self

    def type(self, locator: Tuple[str, str], text: str, clear_first: bool = True):
        """Type text into an element."""
        el = self.find(locator)
        if clear_first:
            el.clear()
        el.send_keys(text)
        return self

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Get text content of an element."""
        return self.find(locator).text

    def is_visible(self, locator: Tuple[str, str]) -> bool:
        """Check if element is visible."""
        try:
            return self._wait.until(EC.visibility_of_element_located(locator)) is not None
        except TimeoutException:
            return False

    def wait_for_text(self, text: str, timeout: int = None):
        """Wait for specific text to appear in the page source."""
        t = timeout or config.EXPLICIT_WAIT
        try:
            self._wait.until(lambda d: text.lower() in d.page_source.lower())
            return True
        except TimeoutException:
            return False

    def swipe_up(self, duration: int = 300):
        """Swipe up on screen."""
        size = self._driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.8)
        end_y = int(size["height"] * 0.3)
        self._driver.swipe(start_x, start_y, start_x, end_y, duration)
        return self

    def take_screenshot(self, name: str = None):
        """Take a screenshot with timestamp."""
        import os
        os.makedirs(config.SCREENSHOT_DIR, exist_ok=True)
        ts = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{name or 'shot'}_{ts}.png"
        path = f"{config.SCREENSHOT_DIR}{filename}"
        self._driver.save_screenshot(path)
        return path
