message = 'Hello There. My name is Sadık Turan'.split()
print(message)
print(message[0]) #split methodu kullanmasaydık H harfi verirdi.

myList = [1,2,3]
print(myList)

myList = ['bir',2,'True',5.6]
print(myList)

list1 = ['one','two','three']
list2 = ['four','five','six']
numbers = list1 + list2
print(numbers)
print(len(numbers))

userA = ['Sadık', 36]
userB = ['Çınar', 2]
print(userA)
print(userB)

users = userA + userB #listeleri birleştirip tek liste yapar.
print(users)

users = [userA, userB] #liste içinde liste oluşturur.
print(users)
print(users[1]) #['Çınar', 2]
print(users[1][0]) #['Çınar']