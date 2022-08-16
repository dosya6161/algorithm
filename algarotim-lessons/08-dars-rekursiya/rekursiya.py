"""
Ma'lumotlar tuzilmasi va algoritimlar

# 08 - dars REKURSIYA / RECURSION

Doston Kamolov

"""
"""

REKURSIYA - malum bir funksiyani ichida qaytarib yana mana shu funksiyani chaqirshga, REKURSIYA deb ataladi

Rekursiv funksiyalar ikki qisimdan iborat bo'ladi :
    Rekursiya sharti (recursive case)
    To'xtash sharti (base case)                                    
    
"""
    
    
# 10 dan 1 ga teskari sanash dasturi    
 
def sana(n):
    print(n)    
    if n<=1:
        return
    else:
        sana(n-1)

sana(10)

"""

n faktorial hisoblash uchun funksiya 
n! = n * (n - 1) * (n - 2) * ... * 2 * 1
5! = 5 * 4 * 3 * 2 * 1 = 120

"""

def fact(x):
    print(x,end=' ')
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))
