from selenium import webdriver

# URL variables
url = 'https://www.youtube.com/c/KalleHallden/videos'
MicrosoftURL = 'https://www.xbox.com/en-AU/consoles/xbox-series-x#purchase'

# Initiate Chrome driver
browser = webdriver.Chrome(executable_path=r'D:\Software\Development Tools\WebDrivers\chromedriver.exe')

# Open URL on chrome
browser.get(MicrosoftURL)

# Naviagate to correct page
browser.find_element_by_xpath('//*[@id="standalonePurch"]/div/a').click()
# browser.find_element_by_xpath('//*[@id="XB19_RRT-00021"]/div[2]/div/div[2]/div/div[1]/span[3]/span').click()
    
# Check if Value has changed
stores = browser.find_elements_by_class_name('hatchretailer')
# Get element 
elements = browser.find_elements_by_class_name('oostext')
# elements = browser.find_elements_by_class_name('oostext')
# Check element value
if(elements.get_attribute('value') == 'OUT OF STOCK'):
    print('there are no Xbox Series X available')
else:
    print('There are Xbox Series X available')


# if(browser.find '//*[@id="XB19_RRT-00021"]/div[2]/div/div[2]/div/div[1]/span[3]/span')
