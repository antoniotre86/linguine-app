import unittest

import predict


class TestModel(unittest.TestCase):
    def test_predict_word(self):
        p = predict.Model.predict_word('bottle')
        self.assertGreaterEqual(p['score'], -1)
        self.assertLessEqual(p['score'], 1)


if __name__ == '__main__':
    unittest.main()

