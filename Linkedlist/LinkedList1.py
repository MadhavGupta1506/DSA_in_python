class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def insert_at_Beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        itr=self.head
        if(self.head==None):
            self.head=Node(data,None)
        while(itr.next):
            itr=itr.next
        itr.next=Node(data,None)
    def insert_at_index(self,data,index):
        itr=self.head
        node=Node(data,None)
        count=0
        while(count<index-1):
            if(itr.next==None):
                return
            itr=itr.next
            count+=1
        temp=itr.next
        itr.next=node
        node.next=temp
    def traversal(self):
        itr=self.head
        if(itr.next==None):
            return 
        else:
            itrstr=""
            while(itr):
                itrstr+=str(itr.data)+"-->"
                itr=itr.next
            print(itrstr+"None")
    def insert_values(self,datalist):
        for data in datalist:
            self.insert_at_end(data)
    def len(self):
        count=0
        itr=self.head
        while(itr):
            count+=1
            itr=itr.next
        return (count)
    def remove_last(self):
        count=0
        itr=self.head
        while(count<self.len()-2):
            itr=itr.next
            count+=1
        itr.next=None
    def remove_head(self):
        itr=self.head
        self.head=itr.next
    def remove_index(self,index):
        if(index<0 or index>self.len()):
            raise Exception("Invalid index")
        if(index==0):
            self.head=self.head.next
            return
        itr=self.head
        count=0
        while(count<index-1):
            count+=1
            itr=itr.next
        
        itr.next=itr.next.next
if(__name__=="__main__"):
    ll=LinkedList()
    ll.insert_at_Beginning(5)
    ll.insert_at_end(3)
    ll.insert_at_index(55,1)
    ll.insert_values([1,2,3,4,5,6,7])
    ll.remove_index(4)
    ll.traversal()
    
    ll.remove_last()
    ll.remove_head()
    ll.traversal()
    print(ll.len())
    