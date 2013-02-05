import collections
from collections import defaultdict

class CryptKeeper:
    """Define some common useful tools for decryption"""
    def __init__(self, enc_string):
        self.enc_string = enc_string
        self.freqs = self._get_freqs("letter_occurence")

    def __call__(self):
        return [m for m in self._name().__dict__ if m[:1] != '_']
    
    @classmethod
    def _name(cls):
        return cls
    
    def decrypt(self):
        '''
        Return decrypted string
    
        enc_string -- the original encoded string
    
        1) load dictionary of all letters and their frequency
            {'a':3, 'b':14, 'c': 16, 'z':26, ...}
        
        2) determine count of letters in string...
                {'a':18, 'b':2, 'c':2, etc...}
        3) match these up, and make a new string with letters swapped
        4) print this and check
        5) Check first letters of word and compare against first letter frequency
        6) Try printing string again after this conversion

        # next steps - refine this by adding new methods. Such as the ability
          to decrypt each word, noting the frequency of the first and last letter,
          double letters, etc...
        '''
        # 1)
        freqs = self.freqs

        # 2)
        string = self.enc_string.lower().replace(' ', '')
        str_length = len(string)
        used = self._build_letter_freq_dict()

        # calculate what letters should be per enc_string count
        # match actual letter as closely as possible, up or down rounded
        return string

    def _get_norm_freq(letter):
	    return self.freqs[letter] * total

    def _build_letter_freq_dict(self):
        """
        Return a dictionary of letters and frequencies used by encoded 
        string.
        """
        #set up an empty dict with default values created by int()
        container = defaultdict(int)
        for letter in self.enc_string:
            container[letter] += 1
        return container
    
    def display_dict(self, name):
        """Display a dictionary for debugging"""
        for k, v in name:
            print("%s - %s" %(k, v))

    def check_frequencies(self, show=False):
        """Check to make sure the frequencies included correctly sum to 1."""
        val = sum([letter.values()[0] for letter in self.freqs]) 
        return val if show else round(val, 4) == float(1)

    def _get_freqs(self, data_type):
        """Return the desired decryption data"""
    
        return {
            'letter_occurence': [
                {'a': 0.08167}, {'b': 0.01492}, {'c': 0.02782}, {'d': 0.04253}, 
                {'e': 0.12702}, {'f': 0.02228}, {'g': 0.02015}, {'h': 0.06094}, 
                {'i': 0.06966}, {'j': 0.00153}, {'k': 0.00772}, {'l': 0.04025}, 
                {'m': 0.02406}, {'n': 0.06749}, {'o': 0.07507}, {'p': 0.01929}, 
                {'q': 0.00095}, {'r': 0.05987}, {'s': 0.06327}, {'t': 0.09056}, 
                {'u': 0.02758}, {'v': 0.00978}, {'w': 0.02360}, {'x': 0.00150}, 
                {'y': 0.01974}, {'z': 0.00074}
            ]
        }[data_type]