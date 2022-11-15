try:
    F = open("subj.txt", "r", encoding="utf-8")
except FileNotFoundError as FNF:
    print("Ошибка открытия файла")
else:
    d = {}
    for k in F:
        k = k.replace("(лаб)", "")
        k = k.replace("(пр)", "")
        k = k.replace("(л)", "")
        a = k.split()
        sum = 0
        for i in range(len(a)):
            if a[i].isdigit():
                sum += int(a[i])
        a[0] = a[0].replace(":", "")
        d[a[0]] = sum
print(d)
