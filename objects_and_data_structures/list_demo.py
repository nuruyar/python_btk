# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

carList = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
print(carList)

# 2- Liste kaç elemanlıdır?

print(len(carList))

# 3- Listenin ilk ve son elemanı nedir?

result = carList[0]
print(result)
result = carList[3]
print(result)
result = carList[-1]
print(result)

# 4- Mazda değerini Toyota ile değiştirin.

carList[-1] = 'Toyota'
print(carList)

# 5- Mercedes listenin bir elemanı mıdır?

result = 'Mercedes' in carList
print(result)

# 6- Listenin -2 indeksindek değer nedir?

result = carList[-2]
print(result)

# 7- Listenin ilk 3 elemanını alın.

result = carList[0:3]
print(result)

# 8- Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.

carList[-2:] = ['Toyota', 'Renault']
print(carList)

# 9- Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.

result = carList + ['Audi', 'Nissan']
print(result)

# 10- LListenin son elemanını silin.

del carList[-1]
print(carList)

# 11- Liste elemanlarını tersten yazdırınız.

result = carList[::-1]
print(result)

# 12- Aşağıdaki verileri bir liste içinde saklayınız.
    # studentA: Yiğit Bilgi 2010 (70,60,70)
    # studentB: Sena Turan 1999 (80,80,70)
    # studentC: Ahmet Turan 1998 (80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.

result = studentA[0]
print(result)
result = studentB[1]
print(result)
result = studentC[3]
print(result)
result = studentC[3][1]
print(result)
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)