import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    # A fixture in pytest refers to a mechanism that allows you to provide
    # a fixed baseline or context for your test functions
    if browser == "Edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    elif browser == "safari":
        print("Launching Safari Browser")
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    return driver

def pytest_addoption(parser): # This will get the value from CLI/ Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


############# HTML Report Generation

#This hook is used for adding environment in HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Vivek'
#
# #This hook is used to delete/ modify environment info in HTMl report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)