from .core import _add, _sub, _mul, _div

def add(a: float, b: float) -> float:
    """加法"""
    return _add(a, b)

def sub(a: float, b: float) -> float:
    """减法"""
    return _sub(a, b)

def mul(a: float, b: float) -> float:
    """乘法"""
    return _mul(a, b)

def div(a: float, b: float) -> float:
    """除法"""
    return _div(a, b)

#加减乘除函数的封装