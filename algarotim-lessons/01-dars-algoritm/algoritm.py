"""
01/08/2022

# 01 - dars ALGORITMLAR / ALGORITM NIMA ?

Doston Kamolov

"""
"""
        ALGORITM NIMA ?
Algoritim - bu muammoni hal qilish uchun aniq ketma-ketlikda berilgan ko'rsatmalar to'plami.

Algoritimni huddi ovqat pishirish uchun berilgan reseptga o'xshatish mumkin

Bir muammoga bir nechta yechim - algoritm bo'lishi mumkin
Algoritimlar bir-biridan tezligi va qancha xotira egallashi bilan fariq qiladi.

Yaxshi algoritmning belgilari:
    * Kirish (muammo) va chiqish (yechim) aniq berilgan bo'lishi kerak. 
    * Algoritimning har bir bosqichi aniq va ravshan bo'lishi kerak.
    * Algoritm muammoni hal qilishning turli usullari orasida eng samaralisi bo'lishi kerak.
    * Algoritimda kompyuter kodi bo'lmasligi kerak. Buning o'rniga algoritim turli xil dasturlash tillarida ishlatilishi 
      mumkin bo'lgan tarzda yozilishi kerak.
      
"""
"""
        ALGORITMGA MISOLLAR 
        
Foydalanuvchi kiritgan ikki sonni qo'shish algoritmi:
    1.Start 
    2.son1,son2 va summa o'zgaruvchilarini yaratamiz
    3.son1 va son2 qiymatlarini qabul qilamiz
    4.son1 va son2 qo'shamiz, natijani summa ga yuklaymiz: summa=son1+son2
    5.summa ni foydalanuchiga qaytaramiz
    6.Stop
    
# # # # # # # # # # # # # # # # # # # # # # # # # #    
    
Uchta sondan eng kattasini topish algoritmi:
    1.Start 
    2.a,b va c o'zgaruvchilarini yaratamiz 
    3.a,b va c ga qiymatlar beramiz 
    4.Agar a>b bo'lsa
       * agar a>c bo'lsa
            * a eng katta son deb qaytar 
       * aks holda 
            * c eng katta son deb qaytar
    5.aks holda (ya'ni a<b) bo'lsa 
       * agar b>c bo'lsa 
            * b eng katta son deb qaytar
       * aks holda
            * c eng katta son deb qaytar  
       
# # # # # # # # # # # # # # # # # # # # # # # # # #

N faktorialni hisoblash algortmi

    ! N faktorial deb 1 dab N gacha bo'lgan sonlarning ko'paytmasiga aytiladi. 
    Masalan N=5 bo'lsa, 5 faktorial 1*2*3*4*5=120 teng.

    1.Satrt     
    2.N, faktorial va i o'garuvchilarini yaratamiz
    3.faktorial va i ga 1 qiymatini yuklaymiz : faktorial=1, i=1
    4.Foydalanuvchidan N qiymatini qabul qlamiz 
    5.i=N bo'lgunga qadar quydagi qadamlarni takrorlaymiz:
        1.faktorial = faktorial  * i
        2.i = i + 1
    6.faktorial qiymatini qaytar    
    7.Stop
    
"""
# Ikki son yi'gindisi
son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
summa = son1 + son2
print(summa)

# # # # # # # # # # # # # # #

# Uchta sondan eng kattasini topish algoritmi
def getLargest(a,b,c):
    if a>b:
        if a>c:
            return a
        else: 
            return c
    else:
        if b>c:
            return b
        else:
            return c

# # # # # # # # # # # # # # #

# N faktorial hisoblash funkysiyasi 
def faktorial(N):
    i=1
    fakt=1 
    while i!=N+1:
        fakt = fakt*i
        i += 1
        return fakt
