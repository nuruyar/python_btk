# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 

# nameSurname = input('İsim Soyisminiz:: ')
# age = int(input('Yaşınız: '))
# educationLevel = input('Eğitim seviyeniz: ')

# if age >= 18:
#     if (educationLevel == 'lise' or educationLevel == 'üniversite'):
#        print(f'Sayın {nameSurname} ehliyet alabilirsiniz.')
#     else:
#         print(f'Sayın {nameSurname} ehliyet alamzsınız, eğitim durumu yetersiz.')
# else: 
#     print(f'Sayın {nameSurname}, ehliyet alamazsınız, yaşınız yetersiz.')

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

# exam1 = int(input('1. sınav notu: '))
# exam2 = int(input('2. sınav notu: '))
# exam3 = int(input('3. sınav notu: '))
# ortalama = (exam1+exam2+exam3)/3

# if 0 <= ortalama < 24:
#     print(f'ortalamanız {ortalama} notunuz: 0')
# elif 25 <= ortalama < 44:
#     print(f'ortalamanız {ortalama} notunuz: 1')
# elif 45 <= ortalama < 54:
#     print(f'ortalamanız {ortalama} notunuz: 2')
# elif 55 <= ortalama < 69:
#     print(f'ortalamanız {ortalama} notunuz: 3')
# elif 70 <= ortalama < 84:
#     print(f'ortalamanız {ortalama} notunuz: 4')
# elif 85 <= ortalama <= 100:
#     print(f'ortalamanız {ortalama} notunuz: 5')
# else:
#     print('Yanlış bilgi girdiniz.')

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime
tarih = input('Aracınız hangi tarihte trafiğe çıktı(2019/8/9): ')
tarih = tarih.split('/') # verilen tarih ve şimdiki zamaın arasındaki günü hesaplamak için

trafigeCıkıs = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()

fark = simdi - trafigeCıkıs
days = fark.days


if days <= 365:
    print('1. servis aralığı')
elif 365 < days <= 365*2:
    print('2. servis aralığı')
elif 365*2 < days <= 365*3:
    print('3. servis aralığı')
else:
    print('Geçerisiz gün girdiniz.')