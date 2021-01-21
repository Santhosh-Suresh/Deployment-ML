from flask import Flask, render_template

app = Flask( __name__ )
# __name__ is for the name of the file in which this code is written

@app.route('/')
def hello_world():
    return render_template("index.html")
#the "templates" folder should be in the same location as the Flask*.py
# that actually calls the render_template function

app.run( debug = True )