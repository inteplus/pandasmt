'''Custom word accessor for pandas.'''


import pandas.api.extensions as _pae
import re as _re


@_pae.register_series_accessor("word")
class WordAccessor:
    '''Accessor for word fields.'''


    # ----- data -----

    
    vi_extended_letters = {
        "lower": "ăâđêôơư",
        "upper": "ĂÂĐÊÔƠƯ"
    }

    vi_vowel_tones = {
        "a": "àáảãạ",
        "ă": "ằắẳẵặ",
        "â": "ầấẩẫậ",
        "e": "èéẻẽẹ",
        "ê": "ềếểễệ",
        "i": "ìíỉĩị",
        "o": "òóỏõọ",
        "ô": "ồốổỗộ",
        "ơ": "ờớởỡợ",
        "u": "ùúủũụ",
        "ư": "ừứửữự",
        "y": "ỳýỷỹỵ",
        "A": "ÀÁẢÃẠ",
        "Ă": "ẰẮẲẴẶ",
        "Â": "ẦẤẨẪẬ",
        "E": "ÈÉẺẼẸ",
        "Ê": "ỀẾỂỄỆ",
        "I": "ÌÍỈĨỊ",
        "O": "ÒÓỎÕỌ",
        "Ô": "ỒỐỔỖỘ",
        "Ơ": "ỜỚỞỠỢ",
        "U": "ÙÚỦŨỤ",
        "Ư": "ỪỨỬỮỰ",
        "Y": "ỲÝỶỸỴ"
    }


    # ----- constructor -----

    
    def __init__(self, pandas_obj):
        self._obj = pandas_obj


    # ----- properties -----

    
    @property
    def english(self):
        '''Returns which item is like an English word'''
        return self._obj.str.match("[a-zA-Z]+$")

    
    @property
    def vietnamese(self):
        '''Returns which item is like a Vietnamese word'''
        pat = "[a-zA-Z" + "".join(self.vi_extended_letters.values()) + "".join(self.vi_vowel_tones.values()) + "]+$"
        return self._obj.str.match(pat)

    
    @property
    def remove_vietnamese_tone(self):
        '''Removes the tone marks in each Vietnamese word.'''
        
        rep = {c:k for k,v in self.vi_vowel_tones.items() for c in v}
        pat = _re.compile("|".join(rep.keys()))
        repl = lambda m: rep[m.group(0)]
        return self._obj.str.replace(pat, repl)

    @property
    def extract_vietnamese_tone(self):
        '''Extracts the tone marks {"`"', "'", "?", "~", "."} each Vietnamese word.'''
        
        l = "`'?~."
        rep = {v[i]:l[i] for k,v in self.vi_vowel_tones.items() for i in range(5)}
        return self._obj.str.replace(".", lambda m: rep.get(m.group(0), ""))

    
    def ngram(self, n):
        '''Returns a list letter n-grams for each word.

        Parameters
        ----------
        n : int
            number n specifying the letter n-gram. Must be integer greater than 1.
        
        Returns
        -------
        pandas.Series
            each element of the returning series is a list of n-grams of the corresponding element in the input series

        Raises
        ------
        ValueError
            if an argument is wrong
        
        Notes
        -----
        You can use pandas' explode() function to process further.
        '''
        if not isinstance(n, int) or n < 2:
            raise ValueError("Expected n to be integer greater than 1, given {}.".format(n))
        return self._obj.apply(lambda x: [x[i:i+n] for i in range(len(x)-n+1)])

    
    @property
    def letter(self):
        '''Returns a list of letters for each word. .'''
        return self._obj.apply(lambda x: list(x))

    
    @property
    def bigram(self):
        '''Returns a list of letter bigrams for each word. See `ngram()`.'''
        return self.ngram(2)

    
    @property
    def trigram(self):
        '''Returns a list of letter trigrams for each word. See `ngram()`.'''
        return self.ngram(3)
