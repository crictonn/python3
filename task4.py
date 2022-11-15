import json

try:
    F = open("firms.txt", "r", encoding="utf-8")
except FileNotFoundError as FError:
    print("Ошибка открытия файла")
else:
    dct = {}
    averageIncome = 0
    firmAmount = 0
    for line in F:
        ls = line.split()
        ls.append(int(ls[2])-int(ls[3]))
        dct[ls[0]] = int(ls[2])-int(ls[3])
        if int(ls[2])-int(ls[3]) >= 0:
            averageIncome += int(ls[2])-int(ls[3])
            firmAmount += 1
    print("Средний доход: ", averageIncome/firmAmount)
    incomeDict = {"average_profit" : averageIncome/firmAmount}
    res = [dct, incomeDict]
    print(res)
    with open("my_file.json", "w") as write_f:
        json.dump(res, write_f)

