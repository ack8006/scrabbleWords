from scrabbleWords import *
import time
import multiprocessing as mp
from random import randint

anagram_dict = gen_anagram_dict()
letters = 'abcdefghijklmnopqrstuvwxyz'


def time_getting_words(word):
    start_time = time.time()
    all_words = get_all_words(word)
    time_duration = time.time()-start_time
    return (len(word), time_duration)


random_words= []
num_repeats = 20
#for length in xrange(2,14):
for word_length in xrange(5,15):
    for repeats in xrange(num_repeats):
        random_word = ''
        for character in xrange(word_length):
            random_word += letters[randint(0,len(letters)-1)]
        random_words.append(random_word)

durations = {}
for word in random_words:
    duration = time_getting_words(word)
    if duration[0] not in durations:
        durations[duration[0]] = 0
    durations[duration[0]] += (duration[1]/num_repeats)

print durations



