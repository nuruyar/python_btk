# value type - string ve number veri tipleri
x = 5
y = 25

x = y
y = 10

print(x,y) #x etkilenmez çünkü farklı alanlarda tanımlanan iki veri tipi

# reference type - list
a = ["apple", "banana"]
b = ["apple", "banana"]

a = b
b[0] = "grape"

print(a,b) # a yı da etkiler, aynı adresi gösteren iki obje olduğundan