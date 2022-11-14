def isfloat(arg):
    try:
        b = float(arg)
    except ValueError as V:
        return False
    else:
        return True


try:
    F = open("task2.txt", "r", encoding="utf-8")
    min = F.readline()
    F.seek(0)
except FileNotFoundError as FNF:
    print("Ошибка открытия файла")
else:
    for line in F:
        a = line.split()
        for i in range(len(a)):
            if isfloat(a[i]) is True:
                if min > a[i]:
                    min = a[i]
                if float(a[i]) > 2.0:
                    print(line.replace("\n", ""))
    F.seek(0)
    for line in F:
        if line.find(min) != -1:
            print("Минимальный оклад: " + line)
