numbers = [1,2,3,4,5]

for num in numbers: #for değişken adı in liste
    print(num)

names = ['çınar', 'sadık', 'sena']

for name in names:
    print(f'My name is {name}')

name = 'sadık turan'

for n in name:
    print(n)

tuple = [(1,2),(3,4),(5,6)]

for t in tuple:
    print(t)

for a,b in tuple:
    print(a,b)

d = {'k1':1 , 'k2':3, 'k3':3}

for item in d:
    print(item)

for item in d.items():
    print(item)

for key,value in d.items():
    print(key,value)