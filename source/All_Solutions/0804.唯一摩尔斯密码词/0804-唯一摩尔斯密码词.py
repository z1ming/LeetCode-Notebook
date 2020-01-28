class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_dict = {'a': '.-',  'b': '-...',  'c': '-.-.',  'd': '-..',  'e': '.',  'f': '..-.',  'g': '--.',  'h': '....',  'i': '..',  'j': '.---',  'k': '-.-',  'l': '.-..',  'm': '--',  'n': '-.', 'o': '---',  'p': '.--.',  'q': '--.-',  'r': '.-.',  's': '...',  't': '-', 'u': '..-',  'v': '...-',  'w': '.--',  'x': '-..-',  'y': '-.--',  'z': '--..'}
        morse_rep = lambda word: ''.join([morse_dict[c] for c in word])
        return len(set([morse_rep(word) for word in words]))