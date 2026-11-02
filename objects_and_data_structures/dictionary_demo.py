'''
    ogrenciler = {
        '120' : {
            'ad' : 'Ali',
            'soyad' : 'Yılmaz',
            'telefon' : 01
        },
        '125' : {
            'ad' : 'Can',
            'soyad' : 'Korkmaz',
            'telefon' : 02
        },
        '128' : {
            'ad' : 'Volkan',
            'soyad' : 'Yükselen',
            'telefon' : 03
        }
    }

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgiili öğrenci bilgisiniz gösteriniz.

'''
# 1
ogrenciler = {}

number  = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# ogrenciler[number] = {
#     'ad' : name,
#     'soyad' : surname,
#     'telefon' : phone
# }
# print(ogrenciler)

ogrenciler.update({ #bu method da kullanılabilir
    number: {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
    # number: { #başka elemanlar da bu metodla yapılabilir
    #     'ad' : name,
    #     'soyad' : surname,
    #     'telefon' : phone
    # }
})
number  = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({ 
    number: {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
})
number  = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({ 
    number: {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
})
print(ogrenciler)

# 2
ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f'Aradığınız {ogrNo} nolu öğrencinin adı {ogrenci['ad']} soyadı {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}.')