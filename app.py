from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Welcome to learn!
Mandatory to enterthe details 

"
