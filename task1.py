f1 = open("file1.txt", "a")
f2 = open("file2.txt", "w")
st = " "
while st != "":
    st = input("Данные (пустая строка для окончания ввода): ")
    if st != "":
        f1.write(st + "\n")
f1 = open("file1.txt", "r")
for line in f1:
    a = line.replace("\n", "")
    k = list(a.replace(" ", ""))
    check = 0
    for i in range(len(k)):
        if k[i].isdigit():
            check = 1
        else:
            continue
    if check == 0:
        f2.write(line)
f1.close()
f2.close()
