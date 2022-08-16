"""
Ma'lumotlar tuzilmasi va algoritimlar

# 11 - dars Quicksort 

Doston Kamolov

"""
"""

    QUICKSORT

Quicksort ham ma'lumotlarni tartiblash algoritmi
Selection sortga nisbatan bir necha barobar tezroq
Divide and conquer yordamida ishlaydi

    QUICKSORT 

Tasavvur qiling biz biror array elementlarini tartibga keltirmoqchimiz 
Birinchi qiladigan ishimiz to'xtash sharti (base case ) topish
To'xtash sharti ikki hil bo'lishi mumkin:
    Bo'sh array []
    Bir elemntdan iborat array [9]
Yuqoridagi ikki holatda array tartibi bo'ladi.    

"""    
"""
    QUICKSORT

Agar array 2 ta elementdan iborat bo'lsa, tartiblash oson:
    Birinchi elementni 2-element bilan solishtiramiz va kerak bo'lsa o'rnini
    almashtiramiz : [12,10] > [10, 12]  
    
    QUICKSORT

Quicksortga algoritmi tez ishlashi uchun tayanch elementini tasodifiy 
olgan afzal (aks holda Big O qiymati O(n2) bo'lishi mumkin)
Umuman olganda esa quicksort uhcun Big O: O(nlogn)

"""
from random import randrange
def qsort(array):
    if len(array)<2:        
        return array
    else:
        #pivot = array.pop(0)
        pivot = array.pop(randrange(len(array)))        
        kichik = [i for i in array if i<=pivot]
        katta = [i for i in array if i>pivot]
        print(f"{kichik}+[{pivot}]+{katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

if __name__ == '__main__':
    #array1 = [1, 5, 12, 0, -5, 66]
    #print(array1)
    #print(qsort(array1))
    array2 = list(range(20))
    print(array2)
    print(qsort(array2))
    #array3 = ['olma', 'anjir', 'shaftoli', 'qovun', 'tarvuz']
    #print(qsort(array3))



















