import csv
import time

def gen_anagram_dict():
    print 'GENERATING ANAGRAM DICT'
    anagram_dict = {}
    with open('/home/hitch/GitHub/scrabbleWords/dictionary.csv', 'rb') as csvfile:
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


def get_all_words(letters, possible_combos = None):
    print letters
    if not possible_combos: possible_combos = []
    possible_combos += [letters]
    if len(letters) == 1:
        return possible_combos
    uq_letters = sorted(list(set(letters)))
    for let in uq_letters:
        new_letters = letters.replace(let, '', 1)
        if new_letters not in possible_combos:
            possible_combos = get_all_words(new_letters, possible_combos)
    return possible_combos

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
        print score_words(all_words)
        print str(time.time()-start_time) + ' seconds'


