from mypackage.mypackage import mypackage_func
import pytest

def test_mypackage_func():
    assert "{:.2f}".format(mypackage_func()) == "3.14", "小数点以下2桁までを比較"
    assert not mypackage_func() == 3, "円周率は3ではない"
