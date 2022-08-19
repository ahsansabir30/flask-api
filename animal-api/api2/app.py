from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/get/animal/<type>', methods=['POST', 'GET'])
def getanimal(type):
    response = requests.post(f'http://localhost:5001/animals/', data=type)
    response_text = response.text
    return render_template('main.html', type=type, response=response_text)

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')