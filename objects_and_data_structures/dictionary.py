# key - value şeklinde çalışır (34 - istanbul gibi)

sehirler = ['kocaeli', 'istanbul']
plakalar = [41, 34]

print(plakalar[sehirler.index('kocaeli')])
print(plakalar[sehirler.index('istanbul')])

# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

plakalar = {'kocaeli' : 41, 'istanbul': 34}

print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara'] = 6 #key ekleme
print(plakalar)

plakalar['kocaeli'] = 'new value' #value güncelleme
print(plakalar)

users = {
    'sadikturan' : {
        'age' : 36,
        'roles' : ['user'],
        'email' : 'sadik@gmail.com',
        'adress' : 'kocaeli',
        'phone' : 123321
    },
    'cinarturan' :{
        'age' : 2,
        'roles' : ['admin', 'user'],
        'email' : 'cinar@gmail.com',
        'adress' : 'kocaeli',
        'phone' : 123321
    }
}
print(users['cinarturan'])
print(users['cinarturan']['age'])

print(users['cinarturan']['roles'][0 ])
