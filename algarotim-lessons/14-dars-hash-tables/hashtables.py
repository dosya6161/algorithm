"""
Ma'lumotlar tuzilmasi va algoritimlar

# 14 - dars  Hash tables

Doston Kamolov

"""
"""

    HASH FUNKSIYA

Hash finksiya matnni takrorlamas,
noyob songa o'tqazib beradi
Hash finksiyalarning turi ko'p
Yaxshi hash funksiya belgilari:
    Bir hil matn uchun bir xil son qaytaradi 
    Xar hil matnlar uchun xar hil son qaytaradi
Hash funksiya sizga kerakli oraliqdagi 
sonlarni qaytaradi

    HASH TABLES

Eng foydali va ko'p ishlatiladigan mal'lumotlar tuzilmasi 
Aksar dasturlash tilarida tadbiq qilingan
    Hash maps
    Maps
    Dictionaries (Python) 

"""

def linear_search(list, item):
    for n in range(len(list)):
        if list[n]==item:
            return n
    return None

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



if __name__ == '__main__':
    myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
    print(linear_search(myList1,11))
    print(binary_search(myList1,11))
    
    myList2 = [18,12,25,1,3,4,10,5,23,4,13,89]
    myList2.sort()
    print(linear_search(myList2,13))
    print(binary_search(myList2,13))
    mevalar = ['olma','anor','olcha','behi','shaftoli','anjir']
    # mevalar.sort()
    print(mevalar)
    print(binary_search(mevalar,'behi'))