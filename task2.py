a = input()
k = list(a.replace(" ", ""))
check = 0
for i in range(len(k)):
    if k[i].isdigit():
        print("good")
    else:
        check = 1
    if check == 0:
        print('Boobs') #Здесь нужно записать строку во второй файл
print(k, check)
