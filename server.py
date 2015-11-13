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
    if 'VERB' in lexicon:
        for w in lexicon['VERB']:
            g.db.execute('insert into verbs (word) values (?)',
                                [w])
    if 'NOUN' in lexicon:
        for w in lexicon['NOUN']:
            g.db.execute('insert into nouns (word) values (?)',
                                [w])
    if 'PRON' in lexicon:
        for w in lexicon['PRON']:
            g.db.execute('insert into pronouns (word) values (?)',
                            [w])
    if 'ADJ' in lexicon:
        for w in lexicon['ADJ']:
            g.db.execute('insert into adjs (word) values (?)',
                            [w])
    if 'ADV' in lexicon:
        for w in lexicon['ADV']:
            g.db.execute('insert into advs (word) values (?)',
                            [w])
    if 'ADP' in lexicon:
        for w in lexicon['ADP']:
            g.db.execute('insert into adpos (word) values (?)',
                            [w])
    if 'CONJ' in lexicon:
        for w in lexicon['CONJ']:
            g.db.execute('insert into conjs (word) values (?)',
                            [w])
    if 'DET' in lexicon:
        for w in lexicon['DET']:
            g.db.execute('insert into dets (word) values (?)',
                            [w])
    if 'NUM' in lexicon:
        for w in lexicon['NUM']:
            g.db.execute('insert into numbers (word) values (?)',
                            [w])
    if 'PRT' in lexicon:
        for w in lexicon['PRT']:
            g.db.execute('insert into functwords (word) values (?)',
                            [w])
    if 'X' in lexicon:
        for w in lexicon['X']:
            g.db.execute('insert into others (word) values (?)',
                            [w])
    if '.' in lexicon:
        for w in lexicon['.']:
            g.db.execute('insert into puncs (word) values (?)',
                            [w])
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
    lex = {}
    nltktest.add_sentence(sentence, lex)
    add_to_db(lex)
    return jsonify(word_cats=lex)

if __name__ == '__main__':
    app.run()