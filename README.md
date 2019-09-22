# linguine-app

Little web app that predicts whether a word provided "sounds" more Italian or more English. 

Under the hood is a character-level LSTM model trained on vocabularies of Italian and English words. 

Deployed on Digitalocean using Flask + wsgi + nginx; following [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04).
