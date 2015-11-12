from flask import Flask, render_template, request, jsonify
from contextlib import closing
from lang_proc import nltktest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/lang.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    sentence = request.args.get('sentence', "", type=str)
    lex = {}
    nltktest.add_sentence(sentence, lex)
    return jsonify(word_cats=lex)

if __name__ == '__main__':
    app.run()