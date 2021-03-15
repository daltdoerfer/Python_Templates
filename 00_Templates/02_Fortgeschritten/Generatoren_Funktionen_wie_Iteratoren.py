# https://www.youtube.com/watch?v=s79SYB8L3V8&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=13
# Neu ist das Yield Statement:
# Stichwort: Lazy Evaluation
# weiter ab Minute 8:00
import random

def random_gen(minimum, maximum, num=10): # num = wieviele Zahlen sollen generiert werden
    for i in range(num):
        yield random.random()*(maximum-minimum)+minimum # Es wird immer nur bis zum nächsten yield gerechnet ohne alle im Speicher zu behalten

for r in random_gen(3.4,8.9):
    print(r)