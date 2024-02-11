*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           BuiltIn
Library           JSONLibrary

*** Variables ***
${BASE_URL}       http://localhost:5000

*** Test Cases ***
Positive Test Case: Add a New Product
    [Documentation]    Positive test case to add a new product
    Create Session    api_session    ${BASE_URL}
    ${product_data}=    Create Dictionary    name=Test Product    price=20
    ${response}=    POST On Session    api_session    /products    json=${product_data}
    Should Be Equal As Strings    ${response.status_code}    200
    Dictionary Should Contain Key    ${response.json()}    price

Negative Test Case: Add Product with Incomplete Data
    [Documentation]    Negative test case to add a product with incomplete data
    Create Session    api_session    ${BASE_URL}
    ${invalid_product_data}=    Create Dictionary    name=Incomplete Product
    ${response}=    POST On Session    api_session    /products    json=${invalid_product_data}
    Should Be Equal As Strings    ${response.status_code}    400

Positive Test Case: Retrieve All Products
    [Documentation]    Positive test case to retrieve all products
    Create Session    api_session    ${BASE_URL}
    ${response}=    GET On Session    api_session    /products
    Should Be Equal As Strings    ${response.status_code}    200
    ${products}=    Evaluate    json.loads('''${response.content}''')
    ${length}=    Get Length    ${products}
    Should Be True    ${length} > 0

Positive Test Case: Place a New Order
    [Documentation]    Positive test case to place a new order
    Create Session    api_session    ${BASE_URL}
    ${order_data}=    Create Dictionary    product=Test Product    quantity=3
    ${response}=    POST On Session    api_session    /orders    json=${order_data}
    Should Be Equal As Strings    ${response.status_code}    200

Negative Test Case: Place Order with Invalid Product Name
    [Documentation]    Negative test case to place an order with an invalid product name
    Create Session    api_session    ${BASE_URL}
    ${invalid_order_data}=    Create Dictionary    product=Nonexistent Product    quantity=1
    ${response}=    POST On Session    api_session    /orders    json=${invalid_order_data}
    Should Be Equal As Strings    ${response.status_code}    400

Positive Test Case: Retrieve All Orders
    [Documentation]    Positive test case to retrieve all orders
    Create Session    api_session    ${BASE_URL}
    ${response}=    GET On Session    api_session    /orders
    Should Be Equal As Strings    ${response.status_code}    200
    ${orders}=    Evaluate    json.loads('''${response.content}''')
    ${length}=    Get Length    ${orders}
    Should Be True    ${length} > 0
