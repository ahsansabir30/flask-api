from flask import Flask, render_template
import requests
import random

app = Flask(__name__)
@app.route('/get/animal/', methods=['POST', 'GET'])
def getanimal():
    animal = ['dog', 'cat', 'cow']
    random_index = random.randint(0,2)
    random_animal = animal[random_index]

    response = requests.post(f'http://localhost:5001/animals/', data=random_animal)
    response_text = response.text
    return render_template('main.html', type=random_animal, response=response_text)

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')