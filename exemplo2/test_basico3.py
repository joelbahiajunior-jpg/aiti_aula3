def somar(a,b):
    return a+b

def test_somar():
    assert somar(5,2) == 7

def comprimento(lista):
    return len(lista)

def test_comprimento():
    assert comprimento([1,2,3,4,5]) == 5
