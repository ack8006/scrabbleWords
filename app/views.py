from app import app
from flask import render_template, request, jsonify
from scrabbleWords import *


anagram_dict = None

@app.route('/')
def scrabble():
    global anagram_dict
    anagram_dict = gen_anagram_dict()
    return render_template('home.html')


@app.route('/scrabbleWords', methods=['GET'])
def get_scrabble_words():
    letters = request.args.get('letters','').lower()
    all_words = all_possible_words(letters, anagram_dict)
    scored_words = score_words(all_words)
    return jsonify(scored_words)
