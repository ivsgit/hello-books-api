def test_get_all_books_with_no_records(client):
    response = client.get("/books")
    response_body = response.get_json()
    assert response.status_code == 200 
    assert response_body == []

# GET /books/1 returns a response body that matches our fixture
def test_get_one_book(client, two_saved_books):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

# GET /books/1 with no data in test database (no fixture) returns a 404
def test_get_one_book_no_data_in_db_status_404(client):
    response = client.get("/books/100")
    response_body = response.get_json()

    assert response.status_code == 404


# GET /books with valid test data (fixtures) returns a 200 with an array including appropriate test data
def test_get_books_returns_array(client, two_saved_books):

    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200 
    assert len(response_body) == 2
    assert response_body[0]["description"] == "watr 4evr"


# POST /books with a JSON request body returns a 201
def test_post_json_request_body_returns_201(client):

    post_request = client.post("/books", json={"title": "titulo", "description": "descrição"})

    assert post_request.status_code == 201


