"""
Ma'lumotlar tuzilmasi va algoritimlar

# 09 - dars STACK VA REKURSIYA

Doston Kamolov

"""
"""
    The Stack

LIFO Ma'lumot to'plami
LIFO (Last In First Out) - Oxirgi kirgan, birinchi chiqadi
Ma'lumot to'plam ustiga qo'shiladi va to'plam ustidan olinadi. 

    The Stack ustida ammalar 

Push - element qo'shish
Pop - element sug'urib olish
isEmpty - to'plam bo'sh ekanligini tekshiradi 
isFull - to'plam to'la ekanligini tekshiradi
Peek - eng yuqoridagi element qiymatini ko'rish

"""
class Stack:
    """Stack obyekti"""
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        """Bo'sh ekanligini tekshirish"""
        return len(self.stack)==0
    
    def push(self,data):
        """Element qo'shish"""
        self.stack.append(data)
        return True
    
    def pop(self):
        """Element sug'urib olish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    
    def peek(self):
        """Eng ustki elementni ko'rish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]

if __name__=='__main__':
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print("Top element: ", stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())    

"""

    Stack va Rekursiya 

Rekursiv funksiyalar ham stack asosida ishlaydi
Dasturlash bu call stack yoki program stack deyiladi 