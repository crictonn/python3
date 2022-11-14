try:
    F = open("subj.txt", "r", encoding="utf-8")
except FileNotFoundError as FNF:
    print("Ошибка открытия файла")
else:
    for k in F:
        k = k.replace("(лаб)", "")
        k = k.replace("(пр)", "")
        k = k.replace("(л)", "")
        a = k.split()
        sum = 0
        for i in range(len(a)):
            if a[i].isdigit():
                sum += int(a[i])
        print(a[0], " ", sum)
