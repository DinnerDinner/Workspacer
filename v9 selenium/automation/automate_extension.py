# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
# import requests
# import os

# # Path to the ChromeDriver executable
# CHROMEDRIVER_PATH = r'C:\\Users\\Pro\\~Work~\\Programs\\Workspacer\\v9 selenium\\chromedriver.exe'

# # Path to your extension directory
# EXTENSION_PATH = r'C:\\Users\\Pro\\~Work~\\Programs\\Workspacer\\v9 selenium\\extension'

# # Initialize the Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument('--disable-web-security')
# chrome_options.add_argument('--disable-site-isolation-trials')
# chrome_options.add_argument('--disable-gpu')

# chrome_options.add_argument(f"--load-extension={EXTENSION_PATH}")

# # Start the WebDriver and navigate to Chrome
# service = Service(executable_path=CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Wait for the extension to load
# time.sleep(5)

# # Trigger the extension by opening its URL
# # Replace the `chrome-extension://your-extension-id` with your actual extension URL
# extension_url = 'chrome-extension://olifadgjmpmjoiohjlgomkojaafaghib'
# driver.get(extension_url)

# # Wait for the extension to process and send the URLs
# # You might need to adjust this wait time based on your extension's behavior
# time.sleep(5)

# # Close the browser
# driver.quit()

# # Notify the server to save the URLs
# response = requests.post('http://localhost:5000/save_urls', json={})
# if response.status_code == 200:
#     print("URLs saved successfully!")
# else:
#     print("Failed to save URLs:", response.json())


import requests

# Send request to the server to trigger the extension
response = requests.post('http://localhost:5000/trigger_extension')

if response.status_code == 200:
    print("Extension triggered successfully!")
else:
    print("Failed to trigger extension:", response.json())
