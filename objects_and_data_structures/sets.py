fruits = {'orange', 'apple', 'banana'}
print(fruits)
# print(fruits[0])

for x in fruits:
    print(x)

fruits.add('cherry')
print(fruits)

fruits.update(['mango', 'grapes', 'apple']) #bir elemandan sadece bir tane ekler
print(fruits)

fruits.remove('mango')
print(fruits)
fruits.discard('apple')
print(fruits)
fruits.pop() #herhalgi bir elemanı siler
print(fruits)
fruits.clear()
print(fruits)

myList = [1,2,3,3,4,4,5]
print(set(myList)) #tekrarlanan elemanları yazmaz

