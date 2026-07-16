"""Sample mobile automation test cases."""
import pytest
from core.driver import DriverContext


@pytest.fixture
def android_driver():
    """Fixture: provide an Android driver for tests."""
    return DriverContext(platform="Android")


@pytest.mark.asyncio
async def test_app_launch(android_driver):
    """Test that the app launches and the driver connects successfully."""
    async with android_driver as driver:
        assert driver is not None


@pytest.mark.asyncio
async def test_screenshot_capability(android_driver):
    """Test that screenshot utility works."""
    async with android_driver as driver:
        page = driver.get_screenshot_as_file
        assert callable(page)


@pytest.mark.asyncio
async def test_window_size(android_driver):
    """Test that device window size is accessible."""
    async with android_driver as driver:
        size = driver.get_window_size()
        assert "width" in size
        assert "height" in size
        assert size["width"] > 0
        assert size["height"] > 0
