'''
MAX_COUNT = 1000
import sys
#print("abc".find("x"))

#print("{:.1}".format(3.4))

s = input()
a = input()
b = input()

i = 0
while True:
    if s.count(a) == 0:
        print(i)
        break
    else:
        s = s.replace(a, b)
        i += 1
        if i >= MAX_COUNT:
            print("Impossible")
            break
'''

#s = "abababa"
#t = "aba"

s = input()
t = input()

counter = 0
for i in range(len(s)):
    if s.startswith(t, i):
        counter += 1
    i += 1
print(counter)
