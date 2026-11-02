maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

#Değişken Tanımlama Kuralları

number1 = 10 #değişken başına rakam almaz.
print(number1)

number1 = 20 #yeni atanan değeri alır.
print(number1)

number1 += 30
print(number1)

age = 20
AGE = 30 #büyük küçük harf duyarlılığı vardır.

print(age)
print(AGE)

yas = 20 #türkçe karakter kullanılmamalı.
_age = 20

x = 1 #int veri tipi
y = 2.3 #float veri tipi
name = "Çınar" #string veri tipi
isStudent = True #bool veri tipi

a = '10'
b = '20'
print(a+b) #string birleştirme işlemi

firstName = "Sadık"
lastName = " Turan"
print(firstName + lastName)

x2, y2, name2, isStudent2 = (1, 2.3, "Ayşe", False)
print(x2, y2, name2, isStudent2)