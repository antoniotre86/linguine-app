'''
Created on 2019-09-17

@author: trentaa
'''
import json

from tensorflow.python.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

MODEL_FILE = './static/models/weights-2.10.hdf5'
VOCAB_FILE = './static/model-data/vocab.json'
MAX_LEN_WORD = 45
MODEL_RANGE = [0.0, 1.0]


def load_vocab(filename):
    with open(VOCAB_FILE, 'r') as foo:
        vocab = json.load(foo)
    return vocab


class Model(object):

    model = load_model(MODEL_FILE)
    model._make_predict_function()
    vocab = load_vocab(VOCAB_FILE)

    @classmethod
    def predict_word(cls, word):
        prediction = cls._get_prediction_for_word(word)
        p = prediction[0][0]
        threshold = (MODEL_RANGE[1] - MODEL_RANGE[0]) / 2.0
        out = {
            'prediction': 'English' if p > threshold else 'Italian',
            'score': str(p)
        }
        return out

    @classmethod
    def _get_prediction_for_word(cls, w):
        ids = cls._convert_word_to_letter_id(w)
        x = pad_sequences([ids], MAX_LEN_WORD)
        x_ = x.reshape((1, MAX_LEN_WORD))
        print(x_, type(x_), len(x_))
        p = cls.model.predict_proba(x_)
        return p

    @classmethod
    def _convert_word_to_letter_id(cls, w):
        out = [cls.vocab.index(c) for c in w]
        return out
