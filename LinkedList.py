# Defining a class for Node of linkedlist
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
#Defining the class Linkedlist for all its operations
class LinkedList:
    
    def __init__(self):
        self.head=None
    def insertAtBeginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        last=Node(data,self.head)
        itr=self.head
        if(self.head==None):
            self.head=Node(data,None)
            return 
        while(itr.next):
            itr=itr.next
        itr.next=Node(data,None)

    def insert_in_index(self,data,index):
        element=Node(data,None)
        count=0
        itr=self.head
        while(count<index-1):
            count+=1
            itr=itr.next
        temp=itr.next
        itr.next=element
        element.next=temp
            
    def print(self):
        if(self.head==None):
            return
        else:
            itr=self.head
            llstr=""
            while itr:
                llstr+=str(itr.data)+"-->"  
                itr=itr.next
            print(llstr)
if __name__=='__main__':
    ll=LinkedList()
    ll.insertAtBeginning(5)
    ll.insertAtBeginning(11)
    ll.insert_at_end(14)
    ll.insert_in_index(10,1)
    ll.print()