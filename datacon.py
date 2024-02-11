import requests

base_url = 'http://localhost:5000'

def retrieve_product_data():
    print("Retrieving product data from the server...")
    try:
        response = requests.get(f'{base_url}/products')
        if response.status_code == 200:
            print("Product data retrieved successfully.")
            return response.json()
        else:
            print(f'Failed to retrieve product data: HTTP {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Error retrieving product data: {e}')
        return None

def retrieve_order_data():
    print("Retrieving order data from the server...")
    try:
        response = requests.get(f'{base_url}/orders')
        if response.status_code == 200:
            print("Order data retrieved successfully.")
            return response.json()
        else:
            print(f'Failed to retrieve order data: HTTP {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Error retrieving order data: {e}')
        return None

def check_data_consistency():
    print("Performing data consistency check...")
    product_data = retrieve_product_data()
    order_data = retrieve_order_data()

    if product_data is not None and order_data is not None:
        print("Product and order data retrieved. Beginning consistency check...")
        product_names = {product['name'] for product in product_data}
        for order in order_data:
            if order['product'] not in product_names:
                print(f"Data consistency check failed: Order references non-existent product '{order['product']}'")
        print("Data consistency check completed.")
    else:
        print("Unable to perform data consistency check due to retrieval errors.")

if __name__ == '__main__':
    check_data_consistency()
