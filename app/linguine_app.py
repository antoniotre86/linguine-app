'''
Created on 2019-09-15

@author: trentaa
'''

from flask import Flask, render_template, request
from predict import Model


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def form_post():
    word = request.form['text']
    prediction = Model.predict_word(word)
    prediction.update({'input': word})
    pred_language = prediction['prediction']
    score = prediction['score']
    confidence = (1-score if pred_language == 'Italian' else score) * 100
    out = {
        'input': word,
        'prediction': pred_language,
        'score': '{}'.format(score),
        'confidence': '{:0.3g}%'.format(confidence)
    }
    return render_template('result.html', **out)


@app.route("/predict/<word>")
def predict_word(word):
    prediction = Model.predict_word(word)
    prediction.update({'input': word})
    out = {
        'input': word,
        'prediction': prediction['prediction'],
        'score': str(prediction['score'])
    }
    return out

