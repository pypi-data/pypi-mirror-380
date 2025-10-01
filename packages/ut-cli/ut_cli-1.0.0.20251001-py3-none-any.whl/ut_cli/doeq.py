# coding=utf-8

from ut_obj.str import Str
from ut_obj.strdate import StrDate

from typing import Any
from collections.abc import Callable

TyArr = list[Any]
TyDic = dict[Any, Any]
TyCallable = Any | Callable[..., Any]
TyDoEq = dict[str, Any]
TyStr = str

TnArr = None | TyArr
TnDic = None | TyDic
TnDoEq = None | TyDoEq
TnStr = None | TyStr


class DoEq:
    """ Manage Commandline Arguments
    """
    sh_value_msg1 = "Wrong parameter: {}; valid parameters are: {}"
    sh_value_msg2 = "Parameter={} value={} is invalid; valid values are={}"

    @classmethod
    def sh_value(cls, d_eq: TyDoEq, d_parms: TnDic) -> TyDoEq:
        if not d_parms:
            return d_eq
        d_eq_new = {}
        for _key, _value in d_eq.items():
            _type: TnStr = d_parms.get(_key)
            if _type is None:
                raise Exception(cls.sh_value_msg1.format(_key, d_parms))
            match _type:
                case 'int':
                    _value = int(_value)
                case 'bool':
                    _value = Str.sh_boolean(_value)
                case 'dict':
                    _value = Str.sh_dic(_value)
                case 'list':
                    _value = Str.sh_arr(_value)
                case '%Y-%m-%d':
                    _value = StrDate.sh(_value, _type)
                case '_':
                    match _type[0]:
                        case '{':
                            _obj = Str.sh_dic(_type)
                            if _value not in _obj:
                                raise Exception(cls.sh_value_msg2.format(_value, _obj))
                        case '[':
                            _obj = Str.sh_dic(_type)
                            if _value not in _obj:
                                raise Exception(cls.sh_value_msg2.format(_value, _obj))
            d_eq_new[_key] = _value
        return d_eq_new

    @classmethod
    def verify(cls, d_eq: TyDoEq, d_parms: TnDic) -> TyDoEq:
        if d_parms is None:
            return d_eq
        _d_eq_new: TyDoEq = cls.sh_value(d_eq, d_parms)
        return _d_eq_new

    @classmethod
    def sh_d_eq(cls, d_eq: TyDoEq, d_parms) -> TyDic:
        """ show equates dictionary
        """
        _d_eq: TyDic = cls.verify(d_eq, d_parms)
        _sh_prof = _d_eq.get('sh_prof')
        if callable(_sh_prof):
            _d_eq['sh_prof'] = _sh_prof()
        return _d_eq
