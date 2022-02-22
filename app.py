from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello beautiful world'

@app.route('/about')    
def about():
    return 'All about a second route'
