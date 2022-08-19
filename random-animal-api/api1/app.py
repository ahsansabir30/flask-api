from flask import Flask, Response, request
import requests

animal = {
    'dog': 'woof',
    'cow': 'moo',
    'cat': 'meow'
}

app = Flask(__name__)

@app.route('/animals/', methods=['POST', 'GET'])
def animals():
    data_sent = request.data.decode('utf-8')
    if data_sent != '':
        sound = animal[data_sent]
        return Response(sound, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')