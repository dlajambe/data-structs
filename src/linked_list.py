class Node():
    def __init__(self, d):
        self.d = d
        self.next = None
        self.prev = None

class SinglyLinkedList():
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
        # The beauty of linked lists is that insertion at the front if
        # O(1) in time complexity
        n = Node(d)
        n.next = self.head
        self.head = n

    def delete(self, d):
        # Case 1 - There is one or zero nodes in the list
        if self.head == None:
            raise ValueError('Cannot delete a node from an empty linked list')
        elif self.head.d == d:
            self.head = None
            return
        
        # Case 2 - There are multiple nodes in the list
        n = self.head
        while n.next != None:
            if n.next.d == d:
                n.next = n.next.next
                return
            n = n.next

        raise ValueError('Node with value {} not found'.format(d))

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
