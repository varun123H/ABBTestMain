
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get('http://localhost:5000')


time.sleep(10)


wait = WebDriverWait(driver, 10)

# Test adding a product
product_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="productName"]')))
product_name_input.send_keys('Test Product')

product_price_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="productPrice"]')))
product_price_input.send_keys('20')


time.sleep(10)

add_product_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//form[@id="productForm"]/button')))
add_product_button.click()

# Verify product is added
product_table = wait.until(EC.visibility_of_element_located((By.XPATH, '//table[@id="productTable"]')))
products = product_table.find_elements(By.TAG_NAME, 'tr')
assert len(products) > 1, 'Product not added successfully'

# Test placing an order
order_product_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="orderProduct"]')))
order_product_input.send_keys('Test Product')

order_quantity_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="orderQuantity"]')))
order_quantity_input.send_keys('3')


time.sleep(10)

place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//form[@id="orderForm"]/button')))
place_order_button.click()

# Verify order is placed
order_table = wait.until(EC.visibility_of_element_located((By.XPATH, '//table[@id="orderTable"]')))
orders = order_table.find_elements(By.TAG_NAME, 'tr')
assert len(orders) > 1, 'Order not placed successfully'

print('UI tests passed successfully')

driver.quit()
