from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is a demo python project!'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
