import pytest

from app.test.utils.functions import get_random_string, get_random_price

def test__get_sizes_service_when_status_is_200_should_return_all_sizes(client, size_uri, create_sizes):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith('200'))
    returned_sizes = {size['_id']: size for size in response.json}    
    for size in create_sizes:
        pytest.assume(size['_id'] in returned_sizes)

def test__create_size_service_when_status_is_200_should_return_the_size_created(create_size):
    size = create_size.json
    pytest.assume(create_size.status.startswith('200'))
    pytest.assume(size['_id'])
    pytest.assume(size['name'])
    pytest.assume(size['price'])


def test__update_size_service_when_status_is_200_should_return_the_size_updated(client, create_size, size_uri):
    current_size = create_size.json
    update_data = {**current_size, 'name': get_random_string(), 'price': get_random_price(1, 5)}
    response = client.put(size_uri, json=update_data)
    pytest.assume(response.status.startswith('200'))
    updated_size = response.json
    for param, value in update_data.items():
        pytest.assume(updated_size[param] == value)


def test__get_size_by_id_service_when_status_is_200_should_return_the_properly_size(client, create_size, size_uri):
    current_size = create_size.json
    response = client.get(f'{size_uri}{current_size["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_size = response.json
    for param, value in current_size.items():
        pytest.assume(returned_size[param] == value)
