import csv

def gen_anagram_dict():
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
    words = get_all_words(letters)
    possible_words = []
    for word in words:
        anagrams = anagram_dict.get(word)
        if anagrams:
            possible_words += anagrams
    return sorted(possible_words, key=len)


def get_all_words(letters):
    letters = ''.join(sorted(letters))
    possible_combos = [letters]
    if len(letters) == 1:
        return possible_combos
    uq_letters = sorted(list(set(letters)))
    for let in uq_letters:
        new_letters = letters.replace(let, '', 1)
        possible_combos += get_all_words(new_letters)
    return list(set(possible_combos))


if __name__ == '__main__':
    print 'GENERATING DICT'
    anagram_dict = gen_anagram_dict()

    #while True:
    #    letters = raw_input('Please Insert Letters: ')
    #    print all_possible_words(letters, anagram_dict)


