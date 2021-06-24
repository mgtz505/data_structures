class Node: 
    
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def listprint(self):  #Printing the Linked List
        print_value = self.head
        while print_value is not None:
            print(print_value.data)
            print_value = print_value.next
    
    def atStart(self, newData):  #Method to allow insertion of a node at start of LL
        NewNode = Node(newData)
        NewNode.next = self.head
        self.head = NewNode
    
    def atEnd(self, newData):  #Method to allow insertion of a node at end of LL
        NewNode = Node(newData)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = NewNode

    def inBetween(seld, middle_node, newData):
        if middle_node is None:
            print("The middle node is absent")
            return
        NewNode = Node(newData)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def RemoveNode(self, Removekey):

        Head = self.head

        if(Head is not None):
            if(Head.data == Removekey):
                self.head = Head.next
                Head = None
                return
        
        while Head is not None:
            if(Head.data == Removekey):
                break
            prev = Head
            Head = Head.next
        
        if(Head == None):
            return
        
        prev.next = Head.next

        Head = None
            
        

list = LinkedList()
list.head = Node("A")

n2 = Node("B")
n3 = Node("C")
n4 = Node("D")

list.head.next = n2
n2.next = n3
n3.next = n4
# list.listprint()  #A B C D

#Insert a new Node at the start of the list
list.atStart("A1")
# list.listprint()

#Insert a new Node at the end of the list
list.atEnd("Z")
# list.listprint()

#Insert a node in the middle:
list.inBetween(list.head.next, "@")
# list.listprint()

#Remove a Node from the LL
list.RemoveNode("D")
list.listprint()