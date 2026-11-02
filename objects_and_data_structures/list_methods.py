numbers = [1,2,3,4,1]
letters = ['a','b','c','a']

val = min(numbers)
print(val)
val = max(numbers)
print(val)
val = min(letters)
print(val)
val = max(letters)
print(val)

val = numbers[1:4]
print(val)
val = numbers[:2]
print(val)

numbers[4] = 40
print(numbers)

numbers.append(49) #sona ekler.
print(numbers)

numbers.insert(3,78) #3. indexe ekler.
print(numbers)

numbers.insert(-1,52) #son elemandan öndeye ekler.
print(numbers)

numbers.pop() #son elemanı siler.
print(numbers)

numbers.pop(0) 
print(numbers)

numbers.remove(40)
print(numbers)

letters.sort() #sıralar.
print(letters)

letters.reverse() #ters sıralar.
print(letters)

print(len(letters))

print(numbers.count(2)) #kaç tane 10 var?
print(letters.count('a'))

numbers.clear() #tüm elemanları siler.
print(numbers)