"""
Ma'lumotlar tuzilmasi va algoritimlar

# 10 - dars Divide and Conquer 

Doston Kamolov

"""
"""

    DIVIDE & CONQUER
    
Bazida muamolarga yechim ko'rinmaydi.
Yaxshi dasturchi muammo oldida yengilmaydi.
Katta muammoni mayda muammolarga bo'lib olib, 
har bir muammoni alohida hal qiladi.
Bu divide and conquer metodi deb ataladi.
Divide and conquer metodi juda ko'p muammolarga yechim 
bo'lishi mumkin.
Keyingi safar murakkab to'qnash kelganingizda shu
metodni esga soling.

    DIVIDE & CINQUER

Keling endi divide and conquer metodini ko'ramiz
Buning uchun biz rekursiyani esga solamiz
Rekursiya ishlashi uchun bizga to'xtash sharti kerak

    DIVIDE & CINQUER

Keling endi divide and conquer metodini ko'ramiz
Buning uchun biz rekursiyani esga solamiz
    1.To'xtash shartini topamiz 
    2.To'xtash shartiga yetgunga qadar rekursiyani takororlaymiz
    
    DIVIDE & CINQUER
    
Rekursiyaning har bir qadami bilan moammo kichrayib borishi kerak.

"""
# Yevklid algoritmi. Ayirish usuli

def gcd(a,b):
    if a==0:
        return b
    if a>b:
        a,b=b,a    
    return gcd(b-a,a)

if __name__ == '__main__':
    print(gcd(168,64))
    
# Ikkta soning buluvchisini topish    
def binarySearch(array,value,start=0,end=None):
    if end is None:
        end = len(array)-1
    if start>end:
        return None
    
    mid = (start+end)//2
    if array[mid]==value:
        return mid
    elif array[mid]>value:
        return binarySearch(array,value,start,mid-1)
    else:
        return binarySearch(array,value,mid+1,end)
    return None
    
if __name__ == '__main__':
    array = [1,5,10,22,45,78,92,99]
    print(binarySearch(array,22))    

# Array elemntlarini hisoblash
def summa(array):
    if array == []:
        return 0
    return array[0]+summa(array[1:])

if __name__ == '__main__':
    array = [10,20,30,40,50]
    print(summa(array))