class Node():
    def __init__(self, d):
        self.d = d
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = None
    
    def insert_back(self, d):
        if d == None:
            raise ValueError('Cannot add None to a linked list')
        
        if self.head == None:
            self.head = Node(d)
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = Node(d)

    def insert_front(self, d):
        if d == None:
            raise ValueError('Cannot add None to a linked list')

        n = Node(d)
        n.next = self.head
        self.head = n

    def delete(self, d):
        if self.head == None:
            raise ValueError('Cannot delete a node from an empty linked list')
        
        n = self.head
        while n.next != None:
            if n.d == d:
                n = n.next
                break
            n = n.next

    def __str__(self):
        if self.head == None:
            return '[]'
        
        n = self.head
        s = ['[']
        while True:
            s.append(str(n.d))
            if n.next == None:
                break
            s.append(', ')
            n = n.next
        s.append(']')
        return ''.join(s)
    
my = SingleLinkedList()
my.insert_back(4)
my.insert_back(7)
my.insert_front(1)
my.delete(4)
print(my)
