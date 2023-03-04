"""flask module that will run the server and provide necessary methods to create endpoints"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """basic endpoint, shows "Hello World" string"""
    return "<p>Hello, World!</p>"


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    """Second endpoint, it will show iput box to enter name.
     The name will be saved as input data and sent to result page"""
    if request.method == 'POST':
        # Do something with the input data
        input_data = request.form['input_box']
        # Render a template with the input data
        return render_template('result.html', input_data=input_data)
    return render_template('form.html')
