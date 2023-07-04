class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def detectAndRemoveLoop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        slow_p=self.head
        fast_p=self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if slow_p==fast_p:
                print("Meeting point",slow_p.data)
                slow_p=self.head
                while(slow_p.next!=fast_p.next):
                    slow_p=slow_p.next
                    fast_p=fast_p.next
                print("Start of the loop",fast_p.next.data)
                fast_p.next=None
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
llist=LinkedList()
llist.head=Node(60)
llist.head.next=Node(2)
llist.head.next.next=Node(1)
llist.head.next.next.next=Node(45)
llist.head.next.next.next.next=Node(92)
extra=Node(53)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
llist.detectAndRemoveLoop()
print("Linked List After Removing loop")
llist.printList()

                    
                    
