# To import selenium, you need to run: "from selenium import webdriver" (and not "import selenium").
# To open the browser, run: browser = webdriver.Firefox()
# To send the browser to a URL, run: browser.get(‘https://inventwithpython.com')
# The browser.find_elements_by_css_selector() method will return a list of WebElement objects: elems = browser.find_elements_by_css_selector(‘img')
# WebElement objects have a "text" variable that contains the element's HTML in a string: elems[0].text
# The click() method will click on an element in the browser.
# The send_keys() method will type into a specific element in the browser.
# The submit() method will simulate clicking on the Submit button for a form.
# The browser can also be controlled with these methods: back(), forward(), refresh(), quit().

# Import relevant moduless
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Define Variables
testUrl = 'https://automatetheboringstuff.com'

# Create a Chrome Browser Object
# Specify the user agent string for emulation
user_agent = [
  "Mozilla/5.0 (Linux; Android 4.4.4; [HM NOTE|NOTE-III|NOTE2 1LTET) AppleWebKit/537.39 (KHTML, like Gecko)  Chrome/53.0.2111.335 Mobile Safari/536.6"
  "Mozilla / 5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.2; x64; en-US Trident / 4.0)"
  "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_8; like Mac OS X) AppleWebKit/536.13 (KHTML, like Gecko)  Chrome/50.0.2440.333 Mobile Safari/600.1"
  "Mozilla/5.0 (iPod; CPU iPod OS 11_1_7; like Mac OS X) AppleWebKit/603.49 (KHTML, like Gecko)  Chrome/51.0.1709.273 Mobile Safari/533.6"
]
s = Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument('--user-agent=%s' % random.choice(user_agent))

# Open Browser
browser = webdriver.Chrome(service=s, options=chrome_options)

# Navigate to a Site:
browser.get(testUrl)

# Scroll to Element & Find the Table of Contents Introduction Hyperlink Element
ActionChains(browser).move_to_element(WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Introduction")))).perform()
elemIntroduction = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Introduction")))

# Click the Introduction Hyperlink Element
elemIntroduction.click()

# Navigate back to the Home page
browser.get(testUrl)

# Find Home page Navbar Hamburger menu
elemNavHamMenu = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > nav > div > button > span")))

# Click the elemHamMenu Hyperlink Element
elemNavHamMenu.click()

# Find the Search Field & Send Keys
elemSearchField = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#navbarSupportedContent > form > input.form-control.me-2")))
elemSearchField.send_keys('zophie')

# Submit the search term
elemSearchField.submit()

# Navigate the browser
browser.back()                # Simulate Back button action
browser.forward()             # Simulate Forward button action
browser.refresh()             # Simulate Page Refresh (F5) action
browser.implicitly_wait(30)   # Simulate Waiting 30 seconds for UI to load
browser.quit()                # Close the browser