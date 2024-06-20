import os
import random

from selenium import webdriver
from selenium.webdriver import Keys


# Connect to Selenium Hub
# Instead of localhost, change it to the name of the server running Selenium hub

def test_google():
    options = webdriver.ChromeOptions()
    #options.add_argument("headless")                               # Headless mode - browser with UI (faster)
    #options.add_experimental_option("detach", True)                # Leave browser open
    if 'SELENIUM_URL' in os.environ:
        hub_url = os.environ['SELENIUM_URL']
        print(f"Hub URL: {hub_url}")
        driver = webdriver.Remote(command_executor=hub_url, options=options)

    else:
        driver = webdriver.Chrome(options=options)

    # Perform a simple test
    driver.get("http://www.google.com")
    assert "Google" in driver.title

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
    driver.quit()


if __name__ == '__main__':
    print("Hello World")
    test_google()
    print("Goodbye World")