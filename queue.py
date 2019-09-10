class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def enque(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode

    def deque(self):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def searching(self,key):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("Value is not found")
                    break
            else:
                print("Value is found")
            temp=None

    def updating(self,newv):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.data=new

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next
QUE=Queue()
print("WELCOME TO QUEUE")
while(True):
    print("Which operation need to be performed?")
    print("1. Enque  2. Deque  3. Searching  4. Updation  5. Display  6. Exit")
    n=int(input())
    if(n==1):
        print("Enter value to be enqued")
        val=input()
        QUE.enque(val)
    elif(n==2):
        QUE.deque()
    elif(n==3):
        print("Enter value to be searched")
        val=input()
        QUE.searching(val)
    elif(n==4):
        print("Enter the new value")
        val1=input()
        QUE.updating(val1)
    elif(n==5):
        QUE.display()
    elif(n==6):
        exit()
