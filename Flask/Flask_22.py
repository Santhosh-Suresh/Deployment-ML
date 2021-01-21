from flask import Flask, render_template, request

app = Flask( __name__ )
# __name__ is for the name of the file in which this code is written

@app.route('/')
def hello_world():
    return render_template("form.html")
#the "templates" folder should be in the same location as the Flask*.py
# that actually calls the render_template function

@app.route('/predict', methods = ['POST'])
def predict():
    any_variable_name = request.form.get('exp')
    score = request.form.get('Name')
    points = request.form.get('Age')

    print(any_variable_name, score, points)
    return 'Form is submitted'
app.run( debug = True )