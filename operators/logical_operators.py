x = 6
hak = 5
devam = 'e'

result = 5 <= x < 10
print(result)

#and
result =  x > 5 and x < 10
print(result)
result = (hak > 0) and (devam == 'e')
print(result)

#or
result = (x > 6) or (x % 2 == 1)
print(result)

#not
result = (x > 0)
print(result)
result = not(x > 0)
print(result)

# x, 5 ile 10 arasında olan bir çift sayı mı
result = (x > 5) and (x < 10) and (x % 2 == 0)
print(result)