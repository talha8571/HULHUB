import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Launch the Chrome browser using Selenium
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the desired URL
url = "https://vinfax-api.designitic.com/api/get/carfax/report?vin=7FARW2H56JE022576"
driver.get(url)

# Get the current URL from the driver
current_url = driver.current_url

# Bearer token
bearer_token = "12|6EVbTSgbtuoAqCQpH1NO05tGWriVmHy6OVSWqYCP"

# Create headers with Bearer token
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json"
}

# Send a GET request to the URL with headers using requests library
response = requests.get(current_url, headers=headers)

# Get the response content
response_content = response._content

# Print the response content
print(response_content)

# Close the browser
driver.quit()