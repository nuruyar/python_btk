"""
Bir müşterinin aşağıdaki bilgileri için değişkenler oluşturunuz.

Müşteri Adı
Müşteri Soyadı
Müşteri Adı ve Soyadı
Müşteri Cinsiyet
Müşteri TC Kimlik
Müşteri Doğum Yılı
Müşteri Adres Bilgisi
Müşteri Yaşı
"""

customerName = 'Ali'
customerLastname = 'Yılmaz'
customerFullName = customerName + ' ' + customerLastname
customerGender = True #erkeğe karşılık gelsin.
customerID = '1234567'
customerDateofBirth = 1989 #'1989' sayısal işlem yapacağımız için şekinde tanımlamadık
customerAdress = 'Kadıköy, İstanbul'
customerAge = 2019 - customerDateofBirth

print(customerAge)

"""
    Aşağıdaki değişkenlerin toplam bilgisini hesaplayınız.
    Sipariş 1 = 110 TL
    Sipariş 2 = 1100.5 TL
    Sipariş 3 = 356.95 TL
"""

order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3
print("Total:" , total)