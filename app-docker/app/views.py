'''
Created on 2019-09-16

@author: trentaa
'''
from app import app
from flask import render_template


@app.route('/')
def home():
   return render_template('home.html')
