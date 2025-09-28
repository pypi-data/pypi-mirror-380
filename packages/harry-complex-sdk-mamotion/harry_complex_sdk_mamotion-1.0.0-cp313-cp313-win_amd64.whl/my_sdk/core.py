def _add(a: float, b: float) -> float:
    return a + b

def _sub(a: float, b: float) -> float:
    return a - b

def _mul(a: float, b: float) -> float:
    return a * b

def _div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b
