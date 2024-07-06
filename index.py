from selenium import webdriver # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver import chrome # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.chrome.service import Service as ChromeService # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from dotenv import load_dotenv # type: ignore
import os
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time
from selenium.webdriver.common.action_chains import ActionChains # type: ignore

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Setup WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # type: ignore

# Open the HTML file
driver.get("https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/")

driver.maximize_window()


try:
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight;")
    
    # Scroll down slowly to the bottom
    scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
    current_position = 0
    
    while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment
    
    # Wait for 3 seconds (adjust as necessary)
    time.sleep(1)
    
    # Scroll back slowly to the top
    while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment
    
    # Scroll to exactly top to handle small adjustments
    driver.execute_script("window.scrollTo(0, 0);")

    print("Slow scroll to the bottom, waited, and scrolled back to the top successfully!")

except Exception as e:
    print(f"Failed to scroll. Error: {str(e)}")


time.sleep(6)

link_text = 'Login'
login_link = driver.find_element(By.LINK_TEXT, link_text)
login_link.click()

time.sleep(2)
username_field = driver.find_element(By.NAME, 'username')
time.sleep(3)
password_field = driver.find_element(By.NAME, 'password')
time.sleep(2)

# Now you can interact with these elements, for example:
username_field.send_keys('user')
password_field.send_keys('password')

login_button = driver.find_element(By.CSS_SELECTOR, 'input[type=\"submit\" i]')
time.sleep(2)
login_button.click()

time.sleep(3)

try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/products.html'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")

    
try:
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight;")
    
    # Scroll down slowly to the bottom
    scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
    current_position = 0
    
    while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment
    
    # Wait for 3 seconds (adjust as necessary)
    time.sleep(1)
    
    # Scroll back slowly to the top
    while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment
    
    # Scroll to exactly top to handle small adjustments
    driver.execute_script("window.scrollTo(0, 0);")

    print("Slow scroll to the bottom, waited, and scrolled back to the top successfully!")

except Exception as e:
    print(f"Failed to scroll. Error: {str(e)}")

time.sleep(5)


link_text = 'About Us'
about_link = driver.find_element(By.LINK_TEXT, link_text)
about_link.click()

time.sleep(2)

try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/about_us1'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")

    
try:
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight;")
    
    # Scroll down slowly to the bottom
    scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
    current_position = 0
    
    while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment
    
    # Wait for 3 seconds (adjust as necessary)
    time.sleep(1)
    
    # Scroll back slowly to the top
    while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment
    
    # Scroll to exactly top to handle small adjustments
    driver.execute_script("window.scrollTo(0, 0);")

    print("Slow scroll to the bottom, waited, and scrolled back to the top successfully!")

except Exception as e:
    print(f"Failed to scroll. Error: {str(e)}")

time.sleep(5)



time.sleep(5)


link_text = 'Home'
home_link = driver.find_element(By.LINK_TEXT, link_text)
home_link.click()

time.sleep(2)

try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/products.html'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")

time.sleep(5)

link_text = 'Account'
account_link = driver.find_element(By.LINK_TEXT, link_text)
account_link.click()

time.sleep(2)


try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/settings'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")

time.sleep(5)


link_text = 'Home'
home_link = driver.find_element(By.LINK_TEXT, link_text)
home_link.click()

time.sleep(2)


try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/products.html'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")


time.sleep(5)








link_text = 'Add to cart'
addtocart_link = driver.find_element(By.LINK_TEXT, link_text)
addtocart_link.click()

time.sleep(2)


try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/success.html'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")

try:
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight;")
    
    # Scroll down slowly to the bottom
    scroll_increment = 10  # Adjust scroll increment (pixels) for slower scrolling
    current_position = 0
    
    while current_position < page_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position += scroll_increment
    
    # Wait for 3 seconds (adjust as necessary)
    time.sleep(1)
    
    # Scroll back slowly to the top
    while current_position > 0:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.03)  # Adjust scroll speed (seconds) for slower scrolling
        current_position -= scroll_increment
    
    # Scroll to exactly top to handle small adjustments
    driver.execute_script("window.scrollTo(0, 0);")

    print("Slow scroll to the bottom, waited, and scrolled back to the top successfully!")

except Exception as e:
    print(f"Failed to scroll. Error: {str(e)}")

time.sleep(5)


link_text = 'here'
home_link = driver.find_element(By.LINK_TEXT, link_text)
home_link.click()

time.sleep(2)


try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/products.html'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")
time.sleep(5)


link_text = 'Logout'
logout_link = driver.find_element(By.LINK_TEXT, link_text)
logout_link.click()

time.sleep(2)

try:
    # Wait up to 10 seconds for the current URL to match the expected dashboard URL
    expected_dashboard_url = 'https://66894b914250edb0285871ad--tourmaline-halva-f854f9.netlify.app/index.html'  # Replace with your expected dashboard URL
    current_url = driver.current_url
    
    if expected_dashboard_url == current_url:
        print(f"Success: Dashboard URL '{expected_dashboard_url}' accessed successfully!")
    else:
        print(f"Failed: Expected dashboard URL '{expected_dashboard_url}', but current URL is '{current_url}'")
        
except Exception as e:
    print(f"{str(e)}")


time.sleep(5)



            



print('************************************************************')
print("Testing of Cure e-Commerce Website is successfully Done......")
print('************************************************************')

driver.quit()


