class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode
    def insertatend(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            self.tail.next=newnode
            self.tail=newnode
    def insertatpos(self,position,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            temp=self.head
            for i in range(1,position-1):
                temp=temp.next
            newnode=Node(value)
            newnode.next=temp.next
            temp.next=newnode
            temp=None

    def delatbeg(self):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            self.head=temp.next
            temp=None

    def delatend(self):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def delatpos(self,key):
        if(self.head==None):
            print("empty")
        else:
            count=0
            temp=self.head
            while(temp.data is not key):
                count=count+1
                if(temp.next is not None):
                    prev = temp
                    temp = prev.next
                else:
                    print("Value to be deleted is not found")
                    break
            if(count is not 0):
                prev.next=temp.next
            else:
                print("tring to delete the value")
            temp=None
            prev=None

    def searching(self,key):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    prev = temp
                    temp = prev.next
                else:
                    print("data not found")
                    break
            else:
                print("data found")
            temp=None

    def updating(self,oldv,newv):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            while(temp.data is not oldv):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("data not found")
                    break
            else:
                temp.data=newv
            temp=None

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

singly=SLL()
print("Welcome to linked list")
while(True):
    print("Which operation need to be performed?")
    print("1.Insertion 2.Deletion 3.Searching 4.Updation 5.Display 6.Exit")
    n=input()
    if(n=="1"):
        print("Which operation need to be")
        print("1. Insertion at beginning")
        print("2. Insertion at end")
        print("3. Insertion at any position")
        n=int(input())
        if(n==1):
            print("Enter value to be inserted")
            val=input()
            singly.insertatbeg(val)
        elif(n==2):
            print("Enter value to be inserted")
            val=input()
            singly.insertatend(val)
        elif(n==3):
            print("Enter the position, where value to be inserted")
            pos=int(input())
            print("Enter value to be inserted")
            val=int(input())
            singly.insertatpos(pos,val)
        else:
            print("Invalid input")
    elif(n=="2"):
        print("Which deletion need to be performed?")
        print("1. Deletion at beginning")
        print("2. Deletion at end")
        print("3. Deletion at any position")
        n=int(input())
        if(n==1):
            singly.delatbeg()
        elif(n==2):
            singly.delatend()
        elif(n==3):
            print("Enter value to be deleted")
            val=input()
            singly.delatpos(val)
        else:
            print("Invalid input")
    elif(n=="3"):
        print("Enter value to be searched")
        val=input()
        singly.searching(val)
    elif(n=="4"):
        print("Enter the value to be updated")
        val=input()
        print("Enter the new value")
        val1=input()
        singly.updating(val,val1)
    elif(n=="5"):
        singly.display()
    elif(n=="6"):
        exit()
    else:
        print("Invalid input")
