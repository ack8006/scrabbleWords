import unittest
from ..scrabbleWords import *

class scrabbleTests(unittest.TestCase):
    anagram_dict = gen_anagram_dict()

    def test_get_anagram_failure(self):
        assert(all_anagrams('zarbzz', self.anagram_dict) == None)

    def test_get_anagram_five_letter(self):
        result = ['skate', 'stake', 'steak', 'takes', 'teaks']
        assert(sorted(all_anagrams('skate', self.anagram_dict)) == sorted(result))

    def test_get_anagrams_many(self):
        result = ['apers', 'apres', 'asper', 'pares', 'parse', 'pears', 'prase', 'presa', 'rapes', 'reaps', 'spare', 'spear']
        assert(sorted(all_anagrams('spare', self.anagram_dict)) == sorted(result))

    def test_get_two_letter_word(self):
        assert(all_possible_words('et', self.anagram_dict) == ['et'])

    def test_get_three_letter_word(self):
        assert(all_possible_words('set', self.anagram_dict) == ['et','es','set'])

    def test_get_seven_letter_word(self):
        result = ['el', 'es', 'er', 're', 'be', 'al', 'la', 'as', 'ab', 'ba', 'ae', 'ar', 'lar', 'als', 'las', 'sal', 'abs', 'bas', 'sab', 'els', 'sel', 'cel', 'sec', 'sae', 'sea', 'are', 'ear', 'era', 'ers', 'res', 'ser', 'ale', 'lea', 'ars', 'ras', 'cab', 'alb', 'bal', 'lab', 'arb', 'bar', 'bra', 'ace', 'lac', 'sac', 'arc', 'car', 'ebb', 'bel', 'reb', 'rec', 'arbs', 'bars', 'bras', 'abbe', 'babe', 'lars', 'earl', 'lear', 'rale', 'real', 'ales', 'lase', 'leas', 'sale', 'seal', 'bels', 'cels', 'barb', 'recs', 'bare', 'bear', 'brae', 'base', 'sabe', 'able', 'bale', 'blae', 'arcs', 'cars', 'scar', 'rebs', 'ares', 'arse', 'ears', 'eras', 'rase', 'sear', 'sera', 'alec', 'lace', 'carb', 'crab', 'cabs', 'scab', 'aces', 'case', 'acre', 'care', 'race', 'carl', 'lacs', 'albs', 'bals', 'labs', 'slab', 'blab', 'ebbs', 'bleb', 'ables', 'bales', 'blase', 'sable', 'babel', 'acres', 'cares', 'carse', 'escar', 'races', 'scare', 'serac', 'abler', 'baler', 'blare', 'blear', 'carls', 'abbes', 'babes', 'blabs', 'barbe', 'blebs', 'carle', 'clear', 'lacer', 'alecs', 'laces', 'scale', 'barbs', 'bares', 'baser', 'bears', 'braes', 'saber', 'sabre', 'carbs', 'crabs', 'cable', 'acerb', 'brace', 'caber', 'arles', 'earls', 'lares', 'laser', 'lears', 'rales', 'reals', 'seral', 'braces', 'cabers', 'carles', 'clears', 'lacers', 'scaler', 'sclera', 'barbel', 'rabble', 'babels', 'barbes', 'balers', 'blares', 'blears', 'cables', 'barbels', 'rabbles', 'slabber', 'clabber', 'scabble', 'clabbers', 'scrabble']
        assert(sorted(all_possible_words('scrabble', self.anagram_dict)) == sorted(result))

    def test_scoring_one(self):
        assert(score_words(['test']) == [('test', 4)])

    def test_scoring_two(self):
        assert(score_words(['zebra']) == [('zebra', 16)])

    def test_multi_scoring(self):
        assert(score_words(['score','test']) == [('score', 7), ('test',4)])

