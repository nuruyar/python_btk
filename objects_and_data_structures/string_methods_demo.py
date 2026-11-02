website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result = ' Hello World '.strip()
print(result)
result = ' Hello World '.lstrip() #soldaki boşluğu siler.
print(result)
result = ' Hello World '.rstrip() #sağdaki boşluğu siler.
print(result)

result = website.lstrip('/:pth') #belirtilen harfleri siler.
print(result)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

result = 'www.sadikturan.com'.strip('w.moc')
print(result)

# 3- 'course' karakter dizisinin tüm kaarakterlerini küçük harf yapın.

result = course.lower()
print(result)
result = course.upper()
print(result)
result = course.title() #her kelimenin baş harfini büyütür.
print(result)

# 4- 'website' içinde kaç tane 'a' karakteri var?

result = website.count('a')
print(result)
result = website.count('www')
print(result)
result = website.count('ww',0,10) #0 ve 10. karakter arasını kontrol eder.
print(result)

# 5- 'website' www ile başlayıp com ile bitiyor mu?

result =  website.startswith('www')
print(result)
result =  website.endswith('com')
print(result)

# 6- 'website' içerisinde '.com' ifadesi var mı?

result = website.find('.com') #kaçındı indexte olduğunu yazar.
print(result)
result = website.find('.com',0,10) 
print(result)
result = course.find('Python') 
print(result)
result = course.rfind('Python') #dizi içinde sağdan sayar.
print(result)

result = website.index('com')
print(result)
result = website.rindex('com')
print(result)
# result = website.rindex('comm')
# print(result) #find ve index farkı burada exception verir.

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

result = course.isalpha()
print(result)
result = 'Hello'.isalpha()
print(result)
result = course.isdigit()
print(result)
result = '123'.isdigit()
print(result)

# 8- 'Contents' ifadesini satırda 50 karakter içerisine yerleştirip sağına ve soluna * ekleyiniz.

result = 'Contents'.center(50,'*')
print(result)
result = 'Contents'.ljust(50,'*')
print(result)
result = 'Contents'.rjust(50,'*')
print(result)

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini - ile değiştir.

result = course.replace(' ','-')
print(result)
result = course.replace(' ','-',5)
print(result)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştir.

result = 'Hello World'.replace('World','There')
print(result)

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

result = course.split(' ')
print(result)
result = result[2]
print(result)
