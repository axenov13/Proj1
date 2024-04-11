from random import random
import itertools

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

class DoubleElementListIterator:
    def __int__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]

class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)

def random_generator(k):
    for i in range(k):
        yield i

gen = random_generator(5)

def simple_gen():
    print("Yes")
    yield
    print("No")
    yield
    print("Hop")
    raise StopIteration("This is the end")

"""
    Программа Python для фильтрации нечетных чисел
    в списке, используя функцию filter()
"""

# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)


class multifilter:
    def judge_half(self, pos, neg):
        if pos >= neg:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(self, pos, neg):
        if pos >= 1:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(self, pos, neg):
        if neg == 0:
            return True
        else:
            return False
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.lst = iterable # iterable - исходная последовательность
        self.funcs = funcs # funcs - допускающие функции
        self.judge = judge

    def __iter__(self):
        for el in self.lst:
            results = []
            for f in self.funcs:
                results.append(f(el))
            pos = results.count(True)
            neg = results.count(False)
            if self.judge(self, pos, neg):
                yield el
        # возвращает итератор по результирующей последовательности


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


def primes():
    yield 2
    i = 2
    while True:
        i += 1
        flag = 1
        for k in range(2, i):
            if i % k == 0:
                flag = 0
        if flag:
            yield i

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]