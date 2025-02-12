import pytest

from app.test.utils.functions import get_random_string, get_random_price

def test__get_orders_service_when_status_is_200_should_return_all_orders(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}    
    for order in create_orders:
        pytest.assume(order.json['_id'] in returned_orders)

def test__create_order_service_when_status_is_200_should_return_the_order_created(create_order):
    order = create_order
    pytest.assume(create_order.status.startswith('200'))
    pytest.assume(order.json['_id'])
    pytest.assume(order.json['client_dni'])
    pytest.assume(order.json['client_name'])
    pytest.assume(order.json['client_phone'])
    pytest.assume(len(order.json['detail']) != 0)

def test__get_order_by_id_service_when_status_is_200_should_return_the_properly_order(client, create_order, order_uri):
    current_order = create_order.json
    response = client.get(f'{order_uri}{current_order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_order = response.json
    for param, value in current_order.items():
        pytest.assume(returned_order[param] == value)
