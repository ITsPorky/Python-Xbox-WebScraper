from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import sched, time
from sendEmail import sendEmail

# ********************************
# Variables
# ********************************

# URL variables
MicrosoftURL = 'https://www.xbox.com/en-AU/consoles/xbox-series-x#purchase'
# Lists
messages = []
values = []

# chrome driver (enter your web driver location)
pathchromedriver = ''

# for opening headless browser
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Initiate Chrome driver
browser = webdriver.Chrome(executable_path=pathchromedriver, options=options)

# Time scheduler
s = sched.scheduler(time.time, time.sleep)

# Time for scheduler
time = 20 # seconds

# ********************************
# Methods
# ********************************
# Check array values for instock
def checkStores():
    # Array of store names
    stores = ['Ebgames', 'Amazon', 'Big W' ,'Harvey Norman', 'JB HI-FI']
    i = 0
    for x in values:
        if(x == 1):
            string = "{} has Xboxs in stock.".format(stores[i])
            messages.append(string)
        else:
            string = "{} has NO Xboxs in stock.".format(stores[i])
            messages.append(string)
        
        i += 1

# Create the email message
def createMessage():
    # Email message
    message = """\
            Subject: Xbox Stock BUY NOW

            There are Xbox Series X available at:

            {}
            https://www.ebgames.com.au/featured/xbox-series-x
            {}
            https://www.amazon.com.au/s?k=xbox+series+x&ref=nb_sb_noss
            {}
            https://www.bigw.com.au/product/xbox-series-x-1tb-console/p/124385/
            {}
            https://www.harveynorman.com.au/xbox-series-x
            {}
            https://www.jbhifi.com.au/pages/xbox?gclid=Cj0KCQiAvP6ABhCjARIsAH37rbQSWI49LWbV9LonOBTV5pqvt3gY4NYsefI09Kk8oyfnjdMy0ABDQpAaAtyxEALw_wcB
           
            https://www.xbox.com/en-AU/consoles/xbox-series-x#purchase""".format(messages[0], messages[1], messages[2], messages[3], messages[4])
    return message

# Method for clearing the array
def clearValues():
    # Clear array values
    del messages[:]


# Check site function
def check_site(sc):
    print("#####################################################################")
    print("Checking for Stock...")
    print("#####################################################################")

    # Open URL on chrome
    browser.get(MicrosoftURL)

    # Naviagate to correct page
    browser.find_element_by_xpath('//*[@id="standalonePurch"]/div/a').click()
    # Check if Value has changed
    stores = browser.find_elements_by_class_name('hatchretailer')
    # Get element 
    elements = browser.find_elements_by_class_name('oostext')

    # Check element value
    for value in elements:
        if(value.text == 'OUT OF STOCK'):
            print('there are no Xbox Series X available')
            values.append(0)
            
        else:
            print('There are Xbox Series X available')
            values.append(1)
            
    checkStores()
    email = createMessage()
    sendEmail(email)
    print('Email sent...')
    clearValues()
    s.enter(time, 1, check_site, (sc,))

# ********************************
# Begin Script
# ********************************
s.enter(time, 1, check_site, (s,))
s.run()