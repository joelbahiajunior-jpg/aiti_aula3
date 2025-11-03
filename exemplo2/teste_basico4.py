from funcoes import *

def test_email_valido():
    assert email_valido("@.") is True
    assert email_valido("@") is False


def test_dividir():
    assert dividir(1,0)==None
    assert dividir(1,1)==True