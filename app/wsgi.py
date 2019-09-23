'''
Created on 2019-09-15

@author: trentaa
'''
from argparse import ArgumentParser

from linguine_app import app as application


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-d', action='store_true')
    args = parser.parse_args()
    application.run(debug=args.d)
