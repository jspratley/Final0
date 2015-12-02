from flask import Flask, render_template, request, jsonify, g
from contextlib import closing
from lang_proc import nltktest, markovchain
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
    for cat in lexicon['children']:
        for w in cat['children']:
            g.db.execute('insert or ignore into entries (word, wordtype) values (?, ?)',
                         [w['name'], cat['name']])
    g.db.commit()

def extract_from_db():
    """
    Retrieves data from the database
    :return: lexicon dictionary matching the necessary format for the visualization
    """
    lexicon = {'name': 'lexicon', 'children': []}
    type_dict = {}

    cur = g.db.execute('select word, wordtype from entries order by id desc')
    for row in cur.fetchall():
        if row[1] not in type_dict:
            type_dict[row[1]] = []
        type_dict[row[1]].append(row[0])
    for key in type_dict:
        temp_dict = {'name': key, 'children': []}
        for w in type_dict[key]:
            word_dict = {'name': w}
            temp_dict['children'].append(word_dict)
        lexicon['children'].append(temp_dict)
    return lexicon

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

@app.route('/lex', methods=['GET'])
def lex():
    updated_lex = extract_from_db()
    return jsonify(word_cats=updated_lex)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    sentence = request.args.get('sentence', "", type=str)

    #Create the markov chain and get the new sentence
    sentence_chain = markovchain.MarkovChain(2)
    sentence_chain.train_paragraph(sentence)
    new_sentence = sentence_chain.generate_by_words()

    #Create the lexicon from the database
    lex = nltktest.create_structure_from_sentence(sentence)
    add_to_db(lex)
    updated_lex = extract_from_db()
    return jsonify(word_cats=updated_lex, new_sent=new_sentence)

if __name__ == '__main__':
    init_db()
    app.run()