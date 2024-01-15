import pytest

from selene import browser


@pytest.fixture(params=[(1920, 1080), (1280, 720)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(800, 480), (480, 360)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1920, 1080), (1280, 720), (800, 480), (480, 360)])
def is_desktop_browser(request):
    resolution = request.param
    if resolution in [(1920, 1080), (1280, 720)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False


@pytest.fixture(params=[(1920, 1080), (1280, 720), (800, 480), (480, 360)])
def is_mobile_browser(request):
    resolution = request.param
    if resolution in [(800, 480), (480, 360)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False
