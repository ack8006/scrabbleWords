import csv
import time
from itertools import combinations

def gen_anagram_dict():
    print 'GENERATING ANAGRAM DICT'
    anagram_dict = {}
    with open('/home/hitch/GitHub/scrabbleWords/app/static/dictionary.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key = ''.join(sorted(row[0]))
            if key in anagram_dict:
                anagram_dict[key] += row
            else:
                anagram_dict[key] = row
    return anagram_dict


def all_anagrams(word, anagram_dict):
    return anagram_dict.get(''.join(sorted(word)))


def all_possible_words(letters, anagram_dict):
    words = get_all_words(''.join(sorted(letters)))
    possible_words = []
    for word in words:
        anagrams = anagram_dict.get(word)
        if anagrams:
            possible_words += anagrams
    return sorted(possible_words, key=len)


def get_all_words(letters):
    possible_combos = [letters]
    for len_word in xrange(1,len(letters)):
        combos = combinations(letters, len_word)
        for combo in combos:
            combo = ''.join(combo)
            possible_combos.append(combo)
    return list(set(possible_combos))


def score_words(all_words):
    value_list = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
                  'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
                  'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
                  'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

    word_scores = [(word, sum(value_list[char] for char in word)) for word
                   in all_words]
    return sorted(word_scores, key = lambda x: x[1], reverse = True)



if __name__ == '__main__':
    anagram_dict = gen_anagram_dict()

    while True:
        letters = raw_input('Please Insert Letters: ').lower()
        start_time = time.time()
        all_words = sorted(all_possible_words(letters, anagram_dict))
        all_words = sorted(all_words, key=len)
        scored_words = score_words(all_words)
        print str(time.time()-start_time) + ' seconds'
        print scored_words[:100]


