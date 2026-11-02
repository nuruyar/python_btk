name = 'Çınar'
surname = 'Turan'

print('My name is {} {}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {s} {n}'.format(n = name, s = surname))
print('My name is {} {} and i am {} years old.'.format(name, surname, '36')) #age değişkeni de tanımlayabiliriz.
print('My name is {} {} and i am {} years old.'.format(name, name, name))

result = 200/700
print('the result is {r:10.4}'.format(r = result)) #.4 virgülden sonra 4 basamak demek, 10 öncesine 10 karakterlik boşluk demek(sayının karakterleri dahil)

#f string yazım
print(f"My name is {name} {surname} and i am {'36'} years old.")