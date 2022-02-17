

import pytest

from selenium import webdriver



# to run parallel tests on different  browsers
# tara make sure to make webdrivers for browsers on local enviroment asof my code.
# parallel test ko lagi cahe -pytest xdist  plugin add garnu
# ani command line bata specify garda no of workers (browsers) push garnu
# -n=(no of methods)
#i have not used pytest -xdist


#__________________________ REgulary used kura haru yaha bata operate garne __________
@pytest.fixture
def setup():
    # if browser=='chrome':

    driver = webdriver.Chrome("D:/automationtesting/chromedriver.exe")
    # elif browser=='firefox':
    #     driver=webdriver.Firefox("")

    return driver

# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture
# def browser(request):
#     return request.config.getoption("--browser")
# ______________________________________________________________________
# concept of hooks

# report banaune

def pytest_configure(config):
    config._metadata['Project Name']='WEBO ASSIGNMNET'
    config._metadata['Module Name' ] ='CONTACT US'
    config._metadata['TESTER NAME'] =' PRAJAY GHIMIRE'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)

