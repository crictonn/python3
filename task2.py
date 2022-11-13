def isfloat(a):
    try:
        b = float(a)
    except:
        return False
    return True


try:
    F = open("task2.txt", "r")
except FileNotFoundError as e:
    print("Ошибка открытия файла")
else:
    for line in F:
        a = line.split()
        for i in range(len(a)):
            if a[i].isdigit or isfloat(a):
                print(a)
                # print("BOOBS")


