import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from openpyxl import Workbook






#This code defines a test method named test_broken_links that checks for broken links on a webpage using Selenium WebDriver and the requests library.
# The method finds all anchor tags (<a>) on the webpage, extracts their href attributes (URLs), and then checks each URL to verify its status code.
# If the URL starts with "http://" or "https://", it sends either a HEAD or GET request to the link depending on whether it points to a video file.
# The results, including the URL and its status code, are printed to the console and stored in an Excel file named "response_status.xlsx" for analysis and reporting.
# This test function can be used to monitor the status of links on the webpage and identify any broken or non-responsive URLs.







class BrokenLinksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://vinfax-api.designitic.com/")

        # login for beelinks staging
        cls.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[1]/form/div[1]/div/input").send_keys("talha1154@hulhub.com")
        cls.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[1]/form/div[2]/div/input").send_keys("1234567890")
        cls.driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[1]/form/div[4]/div/button").click()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_broken_links(self):
        time.sleep(6)
        # Find all <a> tags in the page
        links = self.driver.find_elements_by_tag_name("a")
        # Extract the href attribute from each link
        link_urls = [link.get_attribute("href") for link in links]

        # Create an Excel workbook and select the active sheet
        workbook = Workbook()
        sheet = workbook.active

        # Check for broken links
        for link_url in link_urls:
            if link_url and link_url.startswith(("http://", "https://")):
                if any(ext in link_url.lower() for ext in [".mp4", ".avi", ".mov"]):
                    response = requests.head(link_url)
                    status_code = response.status_code
                    print(f"Video URL (HEAD): {link_url} - Status Code: {status_code}")
                else:
                    response = requests.get(link_url)
                    status_code = response.status_code
                    print(f"URL (GET): {link_url} - Status Code: {status_code}")
            elif link_url:
                print(f"Ignored URL: {link_url}")
            else:
                print("Invalid URL: None")
                status_code = ""

            # Write the URL and status code to the Excel sheet
            sheet.append([link_url, status_code])

        # Save the Excel file
        workbook.save("response_status.xlsx")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
