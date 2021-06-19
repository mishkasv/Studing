from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome!"


@app.route('/hello')
def hello():
    return 'Hi there!'

@app.route('/user')
def user():
    return 'Hello Mykhailo'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
