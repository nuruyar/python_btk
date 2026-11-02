"""
Dairenin Alanı : pi * r^2
Dairenin Çevresi : 2 * pi * r

Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız.
"""

pi = 3.14
r = input("Yarıçap: ")

floatYaricap = float(r)

alan = pi * (floatYaricap**2)
print("alan = ", alan)

cevre = 2 * pi * floatYaricap
print("çevre = ", cevre)

print("alan: " + str(alan)+ "çevre: " + str(cevre)) #string birleştirme yaparken de tür dönüşümü yapılmalı.