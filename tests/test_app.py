from http import HTTPStatus


def test_create_user(client):
    # client = TestClient(app)  # Arrange

    data = {
        'username': 'alice',
        'email': 'alice@example.com',
        'password': 'secret',
    }

    response = client.post('/users', json=data)  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }

    assert response


def test_update_user(client):
    data = {
        'username': 'bob',
        'email': 'bob@example.com',
        'password': 'mynewpassword',
    }

    response = client.put('/users/1', json=data)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
