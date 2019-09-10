class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def insert(self,value):
        if(self.top==None):
            self.top=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.top
            self.top=newnode

    def rem(self):
        if(self.top==None):
            print("empty")
        else:
            temp=self.top
            self.top=temp.next
            temp=None

    def last(self):
        if(self.top==None):
            print("empty")
        else:
            temp=self.top
            print("Top value:")
            print(temp.data)

    def display(self):
        temp=self.top
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

sta=Stack()
print("WELCOME TO STACK")
while(True):
    print("Which operation need to be performed?")
    print("1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    n=int(input())
    if(n==1):
        print("Enter value to be pushed")
        val=input()
        sta.insert(val)
    elif(n==2):
        sta.rem()
    elif(n==3):
        sta.last()
    elif(n==4):
        sta.display()
    elif(n==5):
        exit()
