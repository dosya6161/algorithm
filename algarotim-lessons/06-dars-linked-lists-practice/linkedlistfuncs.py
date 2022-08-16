"""
Ma'lumotlar tuzilmasi va algoritimlar

# 06 - dars LINKED LISTS / AMALIYOT 

Doston Kamolov

"""

class Node:
    """Tugun (node) obyekti"""
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class LinkedList:
    """Linked List obyekti"""
    def __init__(self):
        self.head = None 

    def printList(self):
        temp = self.head 
        while temp:
            print(temp.data)
            temp = temp.next 
            
    def push(self,new_data):
        """List boshiga tugun qo'shish"""
        # Yangi node yaratamiz
        new_node = Node (new_data)
        # List boshini keyingi o'ringa suramiz
        new_node.next = self.head 
        # Yangi nodeni list boshiga qo'yamiz
        self.head = new_node
        
    def insertAfter(self,prev_node, new_data):
        """Biror tugundan so'ng tugun qo'shish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        # Yangi tugun qo'shamiz
        new_node = Node(new_data)
        # Yangi tugunni kayingi tugunga bog'laymiz
        new_node.next = prev_node.next
        # Avvalgi tugunni yangi tugunga bog'laymiz 
        prev_node.next = new_node
        
    def append(self, new_data):
        """List oxirgi tugun qo'shish"""
        # Yangi tugun yaratamiz
        new_node = Node(new_data)
        # List bo'sh emasligini tekshiramiz
        if self.head is None:
            # Bo'sh bo'lsa yangi tugun list boshi
            self.head = new_node
            return
        # Aks holda list oxiriga boramiz
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def deleteNode(self,key):
        """Listada qiymat uchirish"""
        # List boshini topib olamiz
        temp = self.head
        # Birinchi tuguni tekshiramiz
        if (temp and temp.data == key):
            self.head = temp.next
            temp = None     
            return 
        # Aks holda keyingi tugunlarni qarab chiq 
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # Agar qiymat topilmasa 
        if temp==None:
            return
        # Tugunni listdan o'chiramiz
        prev.next = temp.next 
        temp = None        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        