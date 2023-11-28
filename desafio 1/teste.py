import unittest
from desafio1 import sum_intervals

# intervalos = [
#     [1, 5],
#     [10, 20],
#     [1, 6],
#     [16, 19],
#     [5, 11]
# ]
intervalos = [
    [0, 20],
    [-100000000, 10],
    [30, 40]
]


def caso1():
    assert sum_intervals(intervalos) == 100000030
    print("OK - 1")


if __name__ == "__main__":
    caso1()
