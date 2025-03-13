# waf/app.py
from flask import Flask, request
from waf_middleware import waf_check

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the secure web application!"

@app.route('/login', methods=['POST'])
@waf_check
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "password":
        return "Login successful"
    return "Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)
