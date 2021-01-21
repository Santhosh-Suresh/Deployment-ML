from flask import Flask

app = Flask( __name__ )
# __name__ is for the name of the file in which this code is written

@app.route('/')
def hello_world():
    return "Hello World"

app.run( debug = True )