'''Custom word accessor for pandas.'''


import pandas.api.extensions as _pae


@_pae.register_series_accessor("ndarray")
class NdarrayAccessor:
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
