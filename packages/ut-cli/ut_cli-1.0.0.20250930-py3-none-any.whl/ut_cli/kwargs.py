from ut_cli.aoeq import AoEq
from ut_cli.doeq import DoEq

from typing import Any
TyAny = Any
TyArr = list[Any]
TyDic = dict[Any, Any]


class KwArgs:
    """
    Command Line Interface
    """
    @classmethod
    def sh(cls, cls_app, cls_parms, *args) -> TyDic:
        """
        show keyword arguments
        """
        _d_eq: TyDic = AoEq.sh_d_eq(*args)
        _kwargs: TyDic = DoEq.sh_d_eq(_d_eq, d_parms=cls_parms.d_eq)
        _kwargs['cls_app'] = cls_app
        _kwargs['com'] = cls
        return _kwargs
