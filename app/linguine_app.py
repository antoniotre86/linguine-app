'''
Created on 2019-09-15

@author: trentaa
'''

from flask import Flask, render_template, request
from predict import Model


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/", methods=['POST'])
def form_post():
    text = request.form['text']
    prediction = Model.predict_word(text)
    prediction.update({'input':text})
    out = {
        'input': text,
        'prediction': prediction['prediction'],
        'score': prediction['score']
    }
    return render_template('home.html', **out)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
