website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?

lenght = len(course)
print(lenght)

# 2- 'website' içinden www karakterlerini alın.

result = website[7:10]
print(result)

# 3- 'website' içinden com karakterlerini alın.

lenght = len(website)
result = website[22:25]
print(result)

result2 = website[lenght-3:lenght]
print(result2)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

result = course[0:15]
print(result)
result = course[:15]
print(result)

result = course[-15:]
print(result)

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

result = course[::-1]
print(result)
result = course[::1]
print(result)

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# Yukarıdaki verilen değişkenlerle ekrana aşağıdaki ifadeyi yazdırın.
#   'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis'

result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}. "
print(result)

result = "Benim adım {} {}, Yaşım {} ve mesleğim {}. ".format(name, surname, age, job)
print(result)

result = "Benim adım " + name + " " + surname + ", Yaşım " + str(age) + " ve mesleğim " + job
print(result)

## tek tırnak içinde tek tırnak kullanılabilir.

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

s.replace('w', 'W')
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

degisken = 'abc'
print(degisken*3)