"""
Ma'lumotlar tuzilmasi va algoritimlar

# 23 - dars K-NN algoritmi. Regressiya

Doston Kamolov

"""
"""

    REGRESSIYA
Nechta somsa pishirish kerak?
Parametrlar:
    Ob-havo (1-yomon, 5-zo'r)
    Ish kuni (0) yoki hafta oxiri (1)
    To'ylar mavsumi (1 va 0)
Mavjud statistika:
    A. (5,1,0) = 300
    B. (3,1,1) = 225
    C. (1,1,0) = 75
    D. (4,0,1) = 200
    E. (4,0,0) = 150
    F. (2,0,0) = 50
    
Bugun havo yaxshi, hafta oxiri, to'y mavsumi emas: (4,1,0)

Bugun nechta somsa pishirish
kerak?
Masofa hisoblaymiz:
    A. 1
    B. 2
    C. 9
    D. 2
    E. 1
    F. 5
    
Bugun = 300 + 225 + 200 + 150 / 4 = 218.75

    K-NN

K-NN algoritmini klassifikasiya va regressiya uchun qo'llash mumkin 
K-NN to'g'ri ishlashi uchun parametrlarni to'g'ri tanlash o'ta muhim 
    Bu ham alohida muammo va universal yechim yo'q
Masofani hisoblash uchun boshqa, aniqroq formulalar ham bor 
(masalan kosinus o'xshashlik - cosine similarity) 

    MACHINE LEARNING

Machine Learning bu - mavjud ma'lumotlar asosida
kompyuterlarni turli muammolarga algoritm tuzishni "o'rganish".

Machine Learning zamonaviy Sun'iy Intellekt dasturlarining asosi hisoblanadi 

K-NN Machine Learningda keng qo'llanuvchi algoritmlardan biri

    MACHINE LEARNING

OCR (optical character recognition) - rasmni yoki qo'lyozmani 
kompyuter matnga o'zgartirish texnologoyasi.
Bu yerda K-NN ishlatiladi va parameter sifatida belgidagi to'gri 
va egri chiziqlar va kesishmalar olinadi

Object detection / identification - obyektlarni tanish

Spam filtr - spamlarni ajratish 

Jarayonlarni bashorat qilish - aktialarni osishi pasayishi, uzgarishlar bashorat qilish K-NN algoritm yordamida qiladi    