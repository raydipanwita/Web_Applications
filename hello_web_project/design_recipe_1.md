{{ GET /Add-names }} Route Design Recipe

Test-drive a new route POST/sort-names which receives a list of names (as a comma separated string) and return the same list sorted alphabetically.

# Request

# GET http://localhost:5001/add-names

# With body parameters:
names = Julia, Alice, Karim, 

# Expected response (add given name to the list of names):
Julia, Alice, Karim, Eddie

1. Design the Route Signature
# EXAMPLE

GET / add-names
    names : add new name to a predefined list of names

# Home route
GET /home



2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE 1

# POST / add-names
# With names = Julia, Alice, Karim,
# Expected response (200 OK):

"""
Julia, Alice, Karim, Eddie
"""

# EXAMPLE 2 - If no new name given returns the original list

# GET / add-names
# With names = Julia, Alice, Karim,
# Expected response (200 OK):
"""
Julia, Alice, Karim
"""


3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.


"""
GET /add-name to existing list of names
  Parameters:
    name: Eddie

  Expected response (200 OK):
    "Julia, Alice, Karim, Eddie"
"""
def test_post_add_names(web_client):
    response = web_client.get('/add-name?name=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

  """
GET /add-name to existing list of names
  Parameters:
    name: Blank

  Expected response (200 OK):
    "Julia, Alice, Karim"
"""
def test_post_add_names(web_client):
    response = web_client.get('/add-name?name=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim'