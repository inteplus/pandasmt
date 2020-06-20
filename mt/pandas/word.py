'''Custom word accessor for pandas.'''


import pandas.api.extensions as _pae


@_pae.register_series_accessor("ndarray")
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

    @property
    def ngram(self, n):
        '''Returns a list letter n-grams for each word.

        Parameters
        ----------
        n : int
            number n specifying the letter n-gram
        
        Returns
        -------
        pandas.Series
            each element of the returning series is a list of n-grams of the corresponding element in the input series
        
        Notes
        -----
        You can use pandas' explode() function to process further.
        '''
        return self._obj.apply(lambda x: [x[i:i+2] for i in range(len(x)-1)])

    @property
    def bigram(self):
        '''Returns a list of letter bigrams for each word. See `ngram()`.'''
        return self.ngram(2)

    @property
    def trigram(self):
        '''Returns a list of letter trigrams for each word. See `ngram()`.'''
        return self.ngram(3)
