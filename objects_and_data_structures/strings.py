name = 'Sadık'
surname = 'Turan'
age = 36 # aşağıdaki prrintte hata almamak için ya age değişkenini '36' şeklindetanımlayacağız ya da aşağıdaki gibi tür dönüşümü yapmalıyız.

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.'
print(greeting)

lenght = len(greeting)

print(greeting[0]) #0. indexteki karakteri yazdırır.

print(len(greeting))

print(greeting[lenght-1])
print(greeting[-1])

print(greeting[3:7])

print(greeting[3:])
print(greeting[:15])

print(greeting[2:40:2]) #2. karakterden başla 40. karaktere kadar git, 2 karakterde bir al.