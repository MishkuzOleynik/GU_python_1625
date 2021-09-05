import sys
from itertools import islice
if len(sys.argv) == 1:
    with open("buys.csv", "r", encoding="utf-8") as buys:
        print(buys.read())
elif len(sys.argv) == 2:
    with open("buys.csv", "r", encoding="utf-8") as buys:
        buys_gen = (st for st in buys)
        start_st = int(sys.argv[1]) - 1
        print(*islice(buys_gen, start_st, None))
elif len(sys.argv) == 3:
    with open("buys.csv", "r", encoding="utf-8") as buys:
        buys_gen = (st for st in buys)
        start_st = int(sys.argv[1]) - 1
        end_st = int(sys.argv[2])
        print(*islice(buys_gen, start_st, end_st))
