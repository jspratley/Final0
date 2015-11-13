from flask import Flask, render_template, request, jsonify, g
from contextlib import closing
from lang_proc import nltktest
import sqlite3

#Configuration
DATABASE = 'C:/Temp/lex.db'
DEBUG = True
SECRET_KEY = 'disizdeend343'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def add_to_db(lexicon):
    """
    Adds data to the database (not yet a way to retrieve it)
    :param lexicon: lexicon to be processed and inserted
    :return: nothing
    """
    for w in lexicon:
        g.db.execute('insert into entries (word, wordtype) values (?, ?)',
                     [w[0], w[1]])
    g.db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    sentence = request.args.get('sentence', "", type=str)
    tagged = nltktest.tag_in_twos(sentence)
    add_to_db(tagged)
    lex = {}
    lex = nltktest.create_structure_from_sentence(sentence)
    return jsonify(word_cats=lex)

if __name__ == '__main__':
    init_db()
    app.run()