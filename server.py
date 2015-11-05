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
    word_cats = nltktest.add_sentence(sentence)
    return jsonify(word_cats=word_cats)

if __name__ == '__main__':
    app.run()