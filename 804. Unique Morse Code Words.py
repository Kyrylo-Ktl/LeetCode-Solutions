from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    MORSE = {
        'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.', 'g': '--.',
        'h': '....', 'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',
        'o': '---',  'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',
        'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--', 'z': '--..',
    }

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(map(self.encode, words)))

    @classmethod
    def encode(cls, word: str) -> str:
        return ''.join(map(cls.MORSE.get, word))
