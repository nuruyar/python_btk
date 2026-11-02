list = [1,2,3]
print(type(list)
      )
tuple = (1, 'iki', 3) #parantez kullanılmasa da olur
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list = ['ali', 'veli']
tuple = ('damla', 'ayşe', 'ayşe')

list[0] = 'ahmet'
#tuple[0] = 'deniz' #tupleda tek bir eleman üzerinde atandıktan sonra değişmez, silinmez, listede değişir

print(list)
print(tuple)

print(tuple.count('ayşe'))

print(tuple.index('ayşe'))

names = ('demet', 'emel', 'ayşe') + tuple
print(names)