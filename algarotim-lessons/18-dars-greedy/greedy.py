"""
Ma'lumotlar tuzilmasi va algoritimlar

# 18 - dars  Ochko'z Algoritmlar

Doston Kamolov

"""
"""

    GREEDY ALGORITHMS

Ba'zi muammolar hech qanday algoritmga tushmaydi
Shunday holata bizga ochko'z algoritmlar yordam beradi
Ochko'z algoritmlar har qadamda eng optimal yechimi tanlash
Greedy algoritmlar har doim ham to'g'ri yechimni bermaydi 

    Quydagi muammoni ko'ramiz:
Bizda sinifxona va quydagi darslar jadvali bor:
    Matematika: 9:00-10:00
    Fizika: 9:30-10:30
    Adabiyot: 10:00-11:00
    informatika: 10:30-11:30
    Tarix: 11:00-12:00
  Berilgan sinfda o'tish mumkin bo'lgan darslar ro'xatini tuzing 
Yechim:
    1. Eng erta tugaydigan darsni tanlaymiz va ro'yxatga qo'shamiz
    2. Ro'yxat oxiridagi darsdan keyin boshlanadigan eng erta darsni tanlaymiz va
       ro'yxatga qo'shamiz.
    3. Jadvaldagi darslar tugaguncha 2-qadamni takrorlayveramiz
    
The Kanpsack Problem (To'rvaxalta muammosi)

    GREEDY ALGORITHMS

Ochko'z algoritmlar har doim ham eng to'g'ri yechimni bermaydi
Lekin amalga oshirish (dasturlash ) oson
Agar to'g'ri yechimni topish juda ko'p vaqt (resurs) talab qilsa
qoniqarli yechimni topish uchun Greedy Algoritmlarni tanlang

The set-covering problem
To'plamni yopish muammosi

    THE SET_COVERING PROBLEM
Tasavvur qiling, siz yangi uyali aloqa kompaniyasi uchun shahar
bo'ylab antenalar o'rnatib chiqishingiz kerak
Siz antenna o'rnatish uchun 4 ta binoga ruhsat tegdi
Har bir binoga qo'yilgon antenna faqatgina sanoqli hududlarni 
qamrab oladi 
Muammo barcha hududlarni qamraydigan eng kam antennalar 
(binolarni) toping
        Yechim:
    1. Binolarning mavjud kombinasiyalarini quramiz 
       N ta bino uchun 2n kombinasiya mavjud
    2. Kombinasiya orasidan barcha hududlar qamrab
       oladigonlarni topamiz
    3. Ularning orasidan eng kam bino bor to'plamini tanlaymiz
    
"""