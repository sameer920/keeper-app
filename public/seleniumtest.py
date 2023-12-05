from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pytest

path = './chromedriver.exe'
webpageURL = 'http://localhost:3000'

@pytest.fixture
def browser():
    chromeOptions = Options()
    chromeOptions.add_argument('--headless=new')
    driver = webdriver.Chrome(service = Service(executable_path=ChromeDriverManager().install()),options=chromeOptions)
    driver.get(webpageURL)
    yield driver
    driver.quit()

def test_AddNote(browser):
    try:
        elem = WebDriverWait(browser, 10).until(
            lambda d: browser.find_element(By.CLASS_NAME, 'noteTextArea').is_enabled()
        )



        browser.find_element(By.CLASS_NAME, 'noteTextArea').click()

        browser.find_element(By.NAME, 'title').send_keys('Test Note')
        browser.find_element(By.NAME, 'content').send_keys('This is a test body')
        browser.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(2) > form > button').click()

    finally:
        p_tags = browser.find_elements(By.TAG_NAME, 'p')
        found = any('This is a test body' in p_tag.text for p_tag in p_tags)
        assert found, 'Note wasn\'t added correctly'
        # browser.quit()

def test_DelNote(browser):
    try:
        elem = WebDriverWait(browser, 10).until(
            lambda d: browser.find_element(By.CLASS_NAME, 'noteTextArea').is_enabled()
        )

        browser.find_element(By.CLASS_NAME, 'noteTextArea').click()

        browser.find_element(By.NAME, 'title').send_keys('Test Note')
        browser.find_element(By.NAME, 'content').send_keys('This is a test body')
        browser.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(2) > form > button').click()
        p_tags = browser.find_elements(By.TAG_NAME, 'p')
        found = any('This is a test body' in p_tag.text for p_tag in p_tags)
        assert found, 'Note wasn\'t added correctly'

        browser.find_element(By.CSS_SELECTOR, '#root > div > div.note > button').click()


    finally:
        p_tags = browser.find_elements(By.TAG_NAME, 'p')
        found = any('This is a test body' in p_tag.text for p_tag in p_tags)
        assert not found, "Note wasn't deleted"
        # browser.quit()

def test_MultipleNoteAdd(browser):
    try:
        WebDriverWait(browser, 10).until(
            lambda d: browser.find_element(By.CLASS_NAME, 'noteTextArea').is_enabled()
        )


        for i in range(50):
            browser.find_element(By.CLASS_NAME, 'noteTextArea').click()
            browser.find_element(By.NAME, 'title').send_keys(f'Test Note {i}')
            browser.find_element(By.NAME, 'content').send_keys('This is a test body')
            browser.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(2) > form > button').click()

    finally:
        p_tags = browser.find_elements(By.TAG_NAME, 'p')
        found = [p_tag.text for p_tag in p_tags if p_tag.text == 'This is a test body']
        assert len(found) == 50, 'Not all notes were added successfully'
        # browser.quit()

def test_MultipleNoteDel(browser):
    try:
        WebDriverWait(browser, 10).until(
            lambda d: browser.find_element(By.CLASS_NAME, 'noteTextArea').is_enabled()
        )


        for i in range(50):
            browser.find_element(By.CLASS_NAME, 'noteTextArea').click()
            browser.find_element(By.NAME, 'title').send_keys(f'Test Note {i}')
            browser.find_element(By.NAME, 'content').send_keys('This is a test body')
            browser.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(2) > form > button').click()

        for i in range(20):
            browser.find_element(By.CSS_SELECTOR, '#root > div > div.note > button').click()

    finally:
        p_tags = browser.find_elements(By.TAG_NAME, 'p')
        found = [p_tag.text for p_tag in p_tags if p_tag.text == 'This is a test body']
        assert len(found) == 30, 'Not all notes were deleted successfully'
        # browser.quit()

# test_MultipleNoteDel()