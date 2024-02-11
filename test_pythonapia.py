import pytest
import requests


base_url = 'http://localhost:5000'


def test_add_product_positive():
    # Positive test case: Add a new product
    product_data = {'name': 'Test Product', 'price': 20}
    response = requests.post(f'{base_url}/products', json=product_data)
    assert response.status_code == 200, 'Product Added'
    assert 'price' in response.json(), 'Product price not returned in response'

def test_add_product_negative():
    # Negative test case: Add a product with incomplete data (should fail)
    invalid_product_data = {'name': 'Incomplete Product'}
    response = requests.post(f'{base_url}/products', json=invalid_product_data)
    assert response.status_code == 400, 'Added product with incomplete data'
    assert 'error' in response.json(), 'Error message not returned in response'


def test_get_products():
    # Positive test case: Retrieve all products
    response = requests.get(f'{base_url}/products')
    assert response.status_code == 200, 'Failed to retrieve products'
    products = response.json()
    assert len(products) > 0, 'No products found'


def test_place_order_positive():
    # Positive test case: Place a new order
    order_data = {'product': 'Test Product', 'quantity': 3}
    response = requests.post(f'{base_url}/orders', json=order_data)
    assert response.status_code == 200, 'Order placed'
    

def test_place_order_negative():
    # Negative test case: Place an order with invalid product name (should fail)
    invalid_order_data = {'product': 'Nonexistent Product', 'quantity': 1}
    response = requests.post(f'{base_url}/orders', json=invalid_order_data)
    assert response.status_code == 400, 'Placed order with invalid product name'
    assert 'error' in response.json(), 'Error message not returned in response'


def test_get_orders():
    # Positive test case: Retrieve all orders
    response = requests.get(f'{base_url}/orders')
    assert response.status_code == 200, 'Failed to retrieve orders'
    orders = response.json()
    assert len(orders) > 0, 'No orders found'

if __name__ == '__main__':
    pytest.main(['-v', '--html=report.html'])
