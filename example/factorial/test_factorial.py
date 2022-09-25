from factorial import *
def test_factorial():
    assert factorial(5) == 120

def test_logFactorial():
    assert factorial(5) == round(math.exp(logFactorial(5)))
    # assert factorial(5) == math.exp(logFactorial(5))0.00
