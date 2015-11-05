from flask import Flask, render_template
from sqlalchemy import Column, ForeignKey, Integer, String
from contextlib import closing

#Configuration
DATABASE = "C:/Temp/lexicon.db"
DEBUG = True
SECRET_KEY = 'shootureffinmoot3h449'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')