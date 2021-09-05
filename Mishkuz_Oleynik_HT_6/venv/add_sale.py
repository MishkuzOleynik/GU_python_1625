import sys
try:
    file_name, cost = sys.argv
    with open("buys.csv" , "a" , encoding="utf-8") as buys:
        # buys.write(cost+"\n")
        buys.write(cost)
except:
    print("Ошибка ввода параметров")
