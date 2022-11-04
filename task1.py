f1 = open("file1.txt", "a")
st = " "
while st != "":
    st = input("Данные (пустая строка для окончания ввода): ")
    f1.write(st + "\n")
f1 = open("file1.txt", "r")
data = f1.read()
print(data)
f1.close()
