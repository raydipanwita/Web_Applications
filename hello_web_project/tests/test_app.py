# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get('/wave?name=Dana')

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""    
# EXAMPLE 1

# POST / sort-names
# With names = Joe,Alice,Zoe,Julia,Kieran
# Expected response (200 OK):

Alice,Joe,Julia,Kieran,Zoe
"""

def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'text': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
# EXAMPLE 2

# POST / sort-names
# With names = Aaaaaa,Aaaaaz, Aaaaab
# Expected response (200 OK):

Aaaaaa,Aaaaab,Aaaaaz
"""
def test_post_sort_similar_names(web_client):
    response = web_client.post('/sort-names', data={'text': 'Aaaaaa,Aaaaaz,Aaaaab'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaaaaa,Aaaaab,Aaaaaz'

"""
# EXAMPLE 3

# POST / sort-names
# With names = with no names
# Expected response :Invalid Request code

You did not submit any names
"""
def test_post_sort_no_names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'You did not submit any names!'



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
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

"""
GET /add-name to existing list of names
Parameters:
    name: Blank

Expected response (200 OK):
    "Julia, Alice, Karim"
"""
def test_post_add_names_no_new_name_added(web_client):
    response = web_client.get('/add-name')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Julia, Karim - This is the predefined list, you need to submit a new name'