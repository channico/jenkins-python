import random
import allure
from selenium.webdriver.common.keys import Keys


@allure.feature('Navigation')
@allure.story('Open Example Domain')
@allure.severity(allure.severity_level.CRITICAL)
def test_google(driver):
    with allure.step('Open Google'):
        driver.get('https://www.google.com')

    with allure.step("Verify the page title"):
        assert "Google" in driver.title

    with allure.step("Search from a list of random topics"):
        # Find the search box by name attribute and type a random topic
        search_box = driver.find_element("name", "q")

        # Example list of random topics
        topics = ["Python programming", "Machine learning", "Space exploration", "Artificial intelligence"]

        # Choose a random topic from the list
        random_topic = random.choice(topics)

        # Type the random topic into the search box and press Enter
        search_box.send_keys(random_topic)
        search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results
    driver.implicitly_wait(5)

    # Take a screenshot
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
