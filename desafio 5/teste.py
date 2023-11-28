import unittest
from desafio_5 import count_change


def caso_1():
    assert count_change(4, [1, 2]) == 3
    print("OK - 1")


def caso_2():
    assert count_change(10, [5, 2, 3]) == 4
    print("OK - 2")


def caso_3():
    assert count_change(11, [5, 7]) == 0
    print("OK - 3")


if __name__ == "__main__":
    caso_1()
    caso_2()
    caso_3()
