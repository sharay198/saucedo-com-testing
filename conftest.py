import pytest
from selenium import webdriver


@pytest.fixture()
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    return webdriver.Chrome(options=options)
