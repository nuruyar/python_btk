# 1- Girilen 2 sayıdan hangisi büyüktür?

# a = int(input('a: '))
# b = int(input('b: '))
# result = (a > b)
# print(f"a: {a} b: {b}'den büyüktür: {result}")

# 2- Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalamasını hesaplayınız.

# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final: '))
# result = ((vize1+vize2)/2)*0.6 + final*0.4
# print(result)

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = int(input('sayi: '))

# tekcift = (sayi % 2 == 0)
# print(f'girilen sayı çift olma durumu: {tekcift}')

# 4- Girilen bir sayının negatif olma durumunu yazdırın.

# sayi = int(input('sayi: '))

# pozitifMi = (sayi > 0)
# print(f'girilen sayı pozitif olma durumu: {pozitifMi}')


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
    # (email: email@sadikturan.com parola:abc123)

email = "email@sadikturan.com"
parola = "abc123"

girilenEmail = input('email: ')
girilenParola = input('parola: ')

isEmail = (email == girilenEmail)
isPassword = (parola == girilenParola)
print(f'email bilgisi doğruluk: {isEmail}, parola bilgisi doğruluk: {isPassword}')