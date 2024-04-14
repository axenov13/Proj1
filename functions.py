'''
x = input().split()

print(x)

n, k = map(int, x)
print(n, k)
'''

#import operator as op

#print(op.add(4, 5))

#x = ["a", "b", "c"]
#getter_of_second_element = op.itemgetter(1)
#print(getter_of_second_element(x))

#attribute_caller = op.attrgetter("sort")
#print([3,2,1].attribute_caller([])) # don't work the way I want

#from functools import partial

#x = int("1101", base=2)
#print(x)

#f = partial(int, base=2)
#print(f("1101"))

def mod_checker(x, mod=0):
    return lambda y: True if (y % x) == mod else False

mod_3 = mod_checker(3)
print(mod_3(4))


