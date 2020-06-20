'''Custom word accessor for pandas.'''


import pandas.api.extensions as _pae


@_pae.register_series_accessor("word")
class WordAccessor:
    '''Accessor for word fields.'''

    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    @property
    def english(self):
        '''Returns which item is like an English word'''
        return self._obj.str.match("[a-zA-Z]+$")

    @property
    def vietnamese(self):
        '''Returns which item is like a Vietnamese word'''
        return self._obj.str.match("[a-zA-ZàáảãạâầấẩẫậăằắẳẵặđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴ]+$")

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
