from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--headless')

# window size as an argument is required in headless mode
chrome_options.add_argument('window-size=1920x1080')

# Hide the "Chrome is being controlled by automated test software" banner
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)

url = 'https://www.youtube.com/playlist?list=PLjNI3J96cKVKmujglFYJEkHzZwpwJ45LV'
response = driver.get(url)
driver.implicitly_wait(15)

# finds the body tag
elem = driver.find_element_by_tag_name("body")

# you can also use the html tag
# elem = driver.find_element_by_tag_name("html")

no_of_pagedowns = 100
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    sleep(0.2)
    no_of_pagedowns -= 1

title_tags = driver.find_elements_by_id("video-title")
video_titles = []
for title_tag in title_tags:
    video_titles.append(title_tag.get_attribute("aria-label"))

        # save to file
#        with open(save_path, 'a', encoding="utf-8") as f:
            # write out the playlist name
#            f.write(f'{url[2]}\n')

#            # write out the music titles
#            for t in titles:
#                f.write(f'{t}\n')

driver.close()