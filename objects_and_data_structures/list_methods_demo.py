names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- 'Cenk' ismini listenin sonuna ekleyin.

names.append('Cenk')
print(names)

# 2- 'Sena' ismini listenin başına ekleyin.

names.insert(0,'Sena')
print(names)

# 3- 'Deniz' ismini listeden silin.

names.remove('Deniz')
print(names)

# 4- 'Ali' isminin indexi nedir?

index = names.index('Ali')
print(index)

# 5- 'Ali' listenin bir elemanı mıdır?

result = 'Ali' in names
print(result)

# 6- Liste elemanlarının ters çevirin.

result = names[::-1]
print(result)
names.reverse()
print(names)
result = years[::-1]
print(result)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğüne göre sıralayınız.

years.sort()
print(years)

# 9- str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.

str = "Chevrolet, Dacia"
result = str.split(',')
print(result)

# 10- years dizisinin en büyük ve en küçük elemanı nedir? 

min = min(years)
print(min)
max = max(years)
print(max)

# 11- years dizisinde kaç tane 1998 değeri vardır?

result = years.count(1998)
print(result)

# 12- years dizisinin tüm elemanlarını silin

years.clear()
print(years)

# 13- Kullanııcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
print(markalar)