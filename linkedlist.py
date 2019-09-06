linkedlist=["ruby","stellin","mary","chennai"]
print("WELCOME TO MY WEBPAGE")
while(1):
    print("1.INSERT 2.DELETE 3.UPDATE 4.SEARCH 5.EXIT")
    CHOICE=input()
    CHOICE==" "
    print("1.DO YOU WANT TO INSERT FIRST ELEMENT 2.DO YOU WANT TO INSERT LAST ELEMENT 3.WHERE YOU WANT TO INSERT")
    condition=input("ENTER THE FUNCTION VALUE:")
    def firstinsert(linkedlist,data):
        linkedlist.insert(0,data)
        print(linkedlist)
    
    def lastinsert(linkedlist,data):
        linkedlist.append(data)
        print(linkedlist)
    
    def positioninsert(linkedlist,data):
        pos=int(input("enter the position:"))
        linkedlist.insert(pos-1,data)
        print(linkedlist)
    ch=input()
    if condition=="1":
        if ch=="1":
            print("ENTER THE VALUE:")
            data=input()
            firstinsert(linkedlist,data)
        elif ch=="2":
            print("ENTER THE SECOND VALUE:")
            data=input()
            lastinsert(linkedlist,data)    
        elif ch=="3":
            print("position value")
            data=input()
            positioninsert(linkedlist,data)
    #delete function    
    
    def firstdelete(linkedlist,data):
        linkedlist.pop(0)
        print(linkedlist)
        
    def lastdelete(linkedlist,data):
        linkedlist.pop(-1)
        print(linkedlist)
    
    def positiondelete(linkedlist,data):
        pos=int(input("position value:"))
        linkedlist.pop(pos-1)
        print(linkedlist)
    if condition=="2":
        print("1.FIRST ELEMENT DELETE 2.LAST ELEMENT DELETE 3.POSITION DELETE")
        if ch=="1":
            data=input()
            firstdelete(linkedlist,data)
        elif ch=="2":
            data=input()
            lastdelete(linkedlist,data)
        elif ch=="3":
            data=input()
            positiondelete(linkedlist,data)
    #update function
    def UPDATE(linkedlist,oldvalue,newvalue):
        for i in range(0,len(linkedlist)):
            if linkedlist[i]==oldvalue:
                linkedlist[i]=newvalue
                print(linkedlist)
    
    def SEARCH(data):
        if data in linkedlist:
            print("DATA FOUND")
        else:
            print("NOT FOUND")
            print("linkedlist")
        
    if condition=="3":
        oldvalue=input()
        newvalue=input()
        UPDATE(linkedlist,oldvalue,newvalue)
    if condition=="4":
        data=input()
        SEARCH(data)
    if condition=="5":
        exit()
