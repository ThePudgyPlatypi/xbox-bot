from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException 
import time
from twilio.rest import Client

twilio_cid = "your_twilio_cid"
twilio_token = "your_token"
twilio_number = "your_twilio_minus_the_plus"
phone_number = "your_number"
bestbuy_product_url = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p"
user = "best_buy_user_name"
password = "best_buy_password"

#enter path to your chrome driver
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options = options)

#open Xbox link for best buy
driver.get(bestbuy_product_url)

#twilio account info
#enter your personal SID and AUTH Token 
client = Client(twilio_cid, twilio_token)
wait = WebDriverWait(driver, 10)
pause = 2
longPause = 7200
jackpot = False
signed_in = False

# Sign in
time.sleep(pause)

while not signed_in:
    account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.account-button')))
    account_button.click()

    if wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.utility-flyout-account-menu'))):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sign-in-btn'))).click()
        time.sleep(pause)
        driver.find_element(By.ID, 'fld-e').send_keys(user)
        driver.find_element(By.ID, 'fld-p1').send_keys(password)
        time.sleep(pause)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cia-form__controls__submit'))).click()
        time.sleep(pause)
        driver.refresh()
        time.sleep(pause)
        account_text = driver.find_element(By.CSS_SELECTOR, '.account-button .plButton-label').text
        if "Hi" in account_text:
            signed_in = True
            print("Signed in Successfully")
            break
        
        print("Failed to sign in. Trying again")
        

#refresh as long as add to cart is disabled 
while not jackpot:
    try:
        if driver.find_element(By.CSS_SELECTOR, '.add-to-cart-button').is_enabled():
            jackpot = True
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.add-to-cart-button')))
            break
        
        driver.refresh()
        print('Add to cart is not clickable. Refreshing')
    except:
        client.messages.create(
            to = phone_number,
            from_ = twilio_number,
            body = "The Bot has crashed for some reason. Restart it as soon as you can!")

def check_exists_by_selector(selector):
    try:
        driver.find_element(By.CSS_SELECTOR, selector)
    except NoSuchElementException:
        return False
    return True

def addToCart(element): 
    time.sleep(pause)
    element.click()
    time.sleep(pause)
    failure = check_exists_by_selector('.shop-alert .c-alert-content')
    if failure:
        print("To many clicks, temporarily locked out. Waiting 2 hours")
        time.sleep(longPause)
        driver.refresh()
        new_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.add-to-cart-button')))
        addToCart(new_element)
    else:
        print('Xbox Added to cart')
        go_to_cart_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.go-to-cart-button a')))
        time.sleep(pause)
        go_to_cart_element.click()

if element: 
    addToCart(element)

    url = "https://www.bestbuy.com/cart"
    message = "Your XBOX is in your cart! " + url + " HURRY HURRY HURRY HURRY HURRY HURRY HURRY!!!!"

    client.messages.create(
        to = phone_number,
        from_ = twilio_number,
        body = message)