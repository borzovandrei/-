from __future__ import print_function


mas = []
for i in range(int(input())):
    mas.append(int(input()))

def minarr(mas):
    minmas = mas[0]
    for i in mas:
        if i < minmas:
            minmas = i
    return minmas

def summas(a):
    s=0.0
    for i in a:
        s+=i
    return s

def avr(mas):
    return summas(mas)/len(mas)

print(minarr(mas))
print(avr(mas))



