from flask import Flask, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def test():
    print(request.data)
    return request.data


@app.route('/', methods=['GET'])
def home():
    return ''

if __name__ == '__main__':
    app.run()
