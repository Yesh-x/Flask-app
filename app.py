from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TO check the workflow of the code'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
