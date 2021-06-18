from flask import Flask

# create a new Flask app instance
app = Flask(__name__)
#to define the starting point, also known as the root
@app.route('/')
def hello_world():
    return 'Hello world'

