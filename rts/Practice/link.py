import time
import requests
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class BrokenLinksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://staging.beelinks.solutions/home")
        cls.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/div[1]/input").send_keys("talhahhulhub@gmail.com")
        cls.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/div[2]/input").send_keys("12345678")
        cls.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/button").click()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_broken_links(self):
        time.sleep(6)
        # Find all <a> tags in the page
        links = self.driver.find_elements_by_tag_name("a")
        # Extract the href attribute from each link
        link_urls = [link.get_attribute("href") for link in links]

        # Check for broken links
        for link_url in link_urls:
            if link_url and link_url.startswith(("http://", "https://")):
                if any(ext in link_url.lower() for ext in [".mp4", ".avi", ".mov"]):
                    response = requests.head(link_url)
                    print(f"Video URL (HEAD): {link_url} - Status Code: {response.status_code}")
                else:
                    response = requests.get(link_url)
                    print(f"URL (GET): {link_url} - Status Code: {response.status_code}")
            elif link_url:
                print(f"Ignored URL: {link_url}")
            else:
                print("Invalid URL: None")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()