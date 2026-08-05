"""
Design a data structure that supports adding words and searching for
strings with wildcard '.' characters (each '.' can match any letter).
Uses a dictionary keyed by word length for efficient lookup.
"""

import re


class WordDictionary:
    def __init__(self):
        self.words = {}

    def add_word(self, word):
        """Add a word to the dictionary, grouped by length."""
        length = len(word)
        if length in self.words:
            self.words[length].append(word)
        else:
            self.words[length] = [word]

    def search(self, word):
        """Search for a word. '.' acts as a wildcard matching any character."""
        length = len(word)
        if length not in self.words:
            return False

        if '.' not in word:
            return word in self.words[length]

        pattern = re.compile('^' + word + '$')
        return any(pattern.match(item) for item in self.words[length])
