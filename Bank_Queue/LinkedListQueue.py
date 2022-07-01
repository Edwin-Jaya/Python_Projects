#A class to create Node
class Node:
    def __init__(self,data):
        #Assign the value of data to self.data
        self.data=data
        #Assign the value of self.next to None
        self.next=None

#A class to create a linked list for regular customer
class linkedListRegular:
    def __init__(self):
        #Assign the value of self.front to None
        self.front=None
        #Assign the value of self.rear to None
        self.rear=None
        #Assign the value of self.number to 1
        self.number=1
    
    #To check if the linked list is empty
    #If self.front is equal to None it means it's empty
    def isEmpty(self):
        return self.front is None
    
    #To count how many data is in the linked list
    def count(self):
        temp=self.front
        data=0
        while(temp):
            data=data=1
            temp=temp.next
        return data
    
    #Print the linked list
    def __str__(self):
        printOut="Queue : "
        temp=self.front
        if self.isEmpty():
            printOut= printOut + " Empty "
        else:
            while(temp):
                printOut=printOut+str(temp.data)+" "
                temp=temp.next
        return printOut
    
    #To add a node
    def enqueue(self):
        newData=Node(self.number)
        self.number+=1
        if self.isEmpty():
            self.front=newData
            self.rear=newData
        else:
            self.rear.next=newData
            self.rear=newData
    
    #To delete a node
    def dequeue(self):
        if(self.isEmpty()):
            print("No Data!")
        else:
            frontElement=self.front.data
            firstNode=self.front
            if(self.front==self.rear):
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
            del firstNode
            return frontElement
    
    #To peek the self.front
    def peek(self):
        if(self.isEmpty()):
            pass
        else:
            temp=self.front
            return temp.data
    #To clear the linked list
    def empty(self):
        while not self.isEmpty():
            self.dequeue()

#A class to create a linked list for VIP customer
class linkedListVIP:
    def __init__(self):
        self.front=None
        self.rear=None
        self.number=1
    
    def isEmpty(self):
        return self.front is None
    
    def count(self):
        temp=self.front
        data=0
        while(temp):
            data=data=1
            temp=temp.next
        return data
    
    def __str__(self):
        printOut="Queue : "
        temp=self.front
        if self.isEmpty():
            printOut= printOut + " Empty "
        else:
            while(temp):
                printOut=printOut+str(temp.data)+" "
                temp=temp.next
        return printOut

    def enqueue(self):
        newData=Node(self.number)
        self.number+=1
        if self.isEmpty():
            self.front=newData
            self.rear=newData
        else:
            self.rear.next=newData
            self.rear=newData

    def dequeue(self):
        if(self.isEmpty()):
            print("No Data!")
        else:
            frontElement=self.front.data
            firstNode=self.front
            if(self.front==self.rear):
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
            del firstNode
            return frontElement

    def peek(self):
        if(self.isEmpty()):
            pass
        else:
            temp=self.front
            return temp.data

    def empty(self):
        while not self.isEmpty():
            self.dequeue()


