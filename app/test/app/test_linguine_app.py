'''
Created on 2019-09-17

@author: trentaa
'''
from unittest import TestCase
import requests


class TestApp(TestCase):
    def test_post(self):
        req = requests.post('http://127.0.0.1:5000', data={'text': 'panini'})
        self.fail()
