message = " Hello There. My name is Sadık Turan"

print(message)

message = message.upper()
print(message)

message = message.lower()
print(message)

message = message.title() #her kelimenin baş harfi büyük
print(message)

message = message.capitalize() #sadece en baştaki harf büyük
print(message)

message = message.strip() #baştaki boşluk karakterini siler.
print(message)

parts = message.split('.') #her kelimeyi nokta karakterlerinden ayırır ve karakter dizisi haline getirir.
print(parts)

words = message.split() #her kelimeyi boşluk karakterlerinden ayırır ve karakter dizisi haline getirir.
print(words)
print(words[0]) #dizi halinde olduğundan index mantığı çalışır.

message = '*'.join(words) #oluşturduğumuz words dizisini * kullanarak birleştirir, ' ' olsaydı boşluk bırakır eski haline döndürürdü.
print(message)

index = message.find('sadik') #find metodu bir int döndürür ve aradığımız kelimenin başladığı indexi verir. cümle içinde yoksa -1 döndürür.
print(index)

isFound = message.startswith('h') #hangi karakterle başladığı veya endswith ile bittiği kontrol edilebilir.
print(isFound)

message = message.replace('sadik', 'çınar').replace('*',' ')
print(message)

message = message.center(50) #50 karakterlik yer oluşturur ve ortalar.
print(message)