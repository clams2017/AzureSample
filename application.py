#!/usr/bin/env python
# -*- encoding:utf8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
