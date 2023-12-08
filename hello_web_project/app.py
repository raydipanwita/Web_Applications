import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    vowel_number = 0
    for letter in text:
        if letter in 'aeiou':
            vowel_number += 1
    return f'There are {vowel_number} vowels in "{text}"'

# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'
        
    # Send back a friendly greeting with the name
    return f"Hello {name}!"
    # return "No name provided!!!"

# To make a request, run:
# curl "http://localhost:5001/hello?name=David"

# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/namemessage', methods=['POST'])
def namemessage():
    name = request.form['name']
    message = request.form["message"]
    return f"Thanks {name}, you sent this message: {message}"


@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'text' not in request.form:
        return 'You did not submit any names!',400
    text = request.form['text']
    text = text.split(',')
    sortedtext = sorted(text)
    return ','.join(sortedtext)

@app.route('/add-name', methods=['GET'])
def post_add_names():
    list_of_names = ['Julia','Alice', 'Karim']
    if 'name' not in request.args:
        s_names = sorted(list_of_names)
        return ', '.join(s_names) + " - This is the predefined list, you need to submit a new name"
    name_given = request.args['name']
    list_of_names.append(name_given)
    sorted_names = sorted(list_of_names)
    return ', '.join(sorted_names)


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
