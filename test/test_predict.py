from unittest import TestCase

from app import predict


class TestModel(TestCase):
    def test_predict_word(self):
        p = predict.Model.predict_word('bottle')
        self.assertGreaterEqual(p['score'], -1)
        self.assertLessEqual(p['score'], 1)
