import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    # A fixture in pytest refers to a mechanism that allows you to provide
    # a fixed baseline or context for your test functions
    driver = webdriver.Chrome()
    return driver