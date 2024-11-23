numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
lhalf = numbers[0:4]
rhalf = numbers[5:]
newnum = lhalf + rhalf
summa = sum(newnum)
count = len(numbers)
avarage = summa / count
numbers[4]= avarage
print("Измененный список:", numbers)
