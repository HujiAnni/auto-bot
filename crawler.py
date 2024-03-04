#!/usr/bin/env python3

### chmod 755 crawler.py before executing the code

# Basic library from selenium to grasp element from the website given url
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# buffer for waiting the page to load for interaction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import for system file management
import os
import shutil


# define a funtion that will move the file to specified directory
def wait_for_download(directory, timeout=30):
    """
    Wait for a download to complete in the specified directory.
    
    Args:
    - directory: The path to the directory to monitor.
    - timeout: Maximum time to wait for the download to complete, in seconds.
    
    Returns:
    - The name of the downloaded file, or None if timeout is reached.
    """
    initial_files = set(os.listdir(directory))
    elapsed_time = 0
    while elapsed_time < timeout:
        current_files = set(os.listdir(directory))
        new_files = current_files - initial_files
        if new_files:
            return new_files.pop()  # Return the name of the new file
        else:
            time.sleep(10)  # Wait for 1 second before checking again
            elapsed_time += 10
    return None


### Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background if preferred
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

### Navigate to the templates page
url = "https://365datascience.com/resources-center/templates/"
pages = [f"?page={i}" for i in range(1,11)]
hrefs = []

# Please use your name and email for the f_name and email variables
f_name = 'jhu'
email = 'jennifer@customerx.org'

### HERE WE COLLECT THE LIST OF URLS WE'LL HAVE TO VISIT SEPERATELY TO DOWNLOAD THE TEMPLATES SO THAT
### WE DON'T NEED TO VISIT THE LANDING PAGE EVERYTIME WHEN WE GO INTO A DOWNLOADING PAGE
for i in range(10):
    driver.get(url+pages[i])
    cards = driver.find_elements(By.CSS_SELECTOR, ".resource a")

    # Loop through each card
    for card in cards:
        # Open the template card page
        hrefs.append(card.get_attribute('href'))

working_href = list(set(hrefs))
#len(working_href)

# open file in write mode
with open(r'templates.txt', 'w') as fp:
    for item in working_href:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')
    
# empty list to read list from a file
working_href = []

# open file and read the content in a list
with open(r'templates.txt', 'r') as fp:
    for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        working_href.append(x)

# # display list
# print(working_href)
        
