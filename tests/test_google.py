import os
import random
import unittest

from selenium import webdriver
from selenium.webdriver import Keys


class ExampleTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")                               # Headless mode - browser with UI (faster)
        # options.add_experimental_option("detach", True)                # Leave browser open

        # Connect to Selenium Hub
        # Instead of localhost, change it to the name of the server running Selenium hub
        if 'SELENIUM_URL' in os.environ:
            hub_url = os.environ['SELENIUM_URL']
            print(f"Hub URL: {hub_url}")
            self.driver = webdriver.Remote(command_executor=hub_url, options=options)
        else:
            self.driver = webdriver.Chrome(options=options)

    def test_google(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title

        # Find the search box by name attribute and type a random topic
        search_box = self.driver.find_element("name", "q")

        # Example list of random topics
        topics = ["Python programming", "Machine learning", "Space exploration", "Artificial intelligence"]

        # Choose a random topic from the list
        random_topic = random.choice(topics)

        # Type the random topic into the search box and press Enter
        search_box.send_keys(random_topic)
        search_box.send_keys(Keys.RETURN)

        # Wait for a few seconds to see the results
        self.driver.implicitly_wait(5)
        self.driver.quit()
