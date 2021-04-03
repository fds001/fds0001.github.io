from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
       return "Hello, Flask! test 123"

@app.route("/test")
def new():
        return "Test 123456"


if __name__ == '__main__':
    app.run(port=5000, debug=True)