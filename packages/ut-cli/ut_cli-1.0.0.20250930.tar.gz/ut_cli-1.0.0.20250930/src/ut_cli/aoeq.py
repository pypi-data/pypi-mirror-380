# coding=utf-8
from typing import Any

TyArr = list[Any]
TyDoEq = dict[Any, Any]
TyStr = str


class AoEq:
    """ Dictionary of Equates
    """
    @staticmethod
    def sh_a_eq(eq: TyStr) -> TyArr:
        a_eq = eq.split('=')
        if len(a_eq) == 1:
            return ['cmd', *a_eq]
        return a_eq

    @classmethod
    def sh_d_eq(cls, a_eq: TyArr) -> TyDoEq:
        _d_eq: TyDoEq = {}
        for eq in a_eq[1:]:
            _a_eq = cls.sh_a_eq(eq)
            if _a_eq[0] == 'cmd':
                _a_cmd = _a_eq[1].split()
                _d_eq[_a_eq[0]] = _a_cmd
            else:
                _d_eq[_a_eq[0]] = _a_eq[1]
        return _d_eq
