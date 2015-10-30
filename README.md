# scrabbleWords
scrabble word finder using a hash tables

This is now running as a flask app (albeit with zero formatting)
Simply download packages, change the file path in the scrabbleWords.py for the dictionary and python run.py.

The program will first pull dictionary.csv into a hash table with the sorted word as the key and the value as a list of words. This allows constant time access to the anagrams of a word being searched.

To find all valid words from an input of letters, instead of having to look for all possible permutations which is an O(n!) problem, only have to find sorted combinations which is an O(2^n) problem. 



based on runtime trials n=100 per length of letter input

10: 0.00042273998260498023 seconds

11: 0.0007289695739746093 seconds

12: 0.001456356048583985 seconds

13: 0.0032237672805786135 seconds

14: 0.006046042442321779 seconds

15: 0.01360099315643311 seconds

16: 0.027913050651550288 seconds

17: 0.06181572914123536 seconds

18: 0.12787174701690673 seconds

19: 0.26705210208892827 seconds

20: 0.5579523372650145 seconds
