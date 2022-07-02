#A class to make the node
class Node:
    def __init__(self,data):
        #To assign the value of data to self.data
        self.data=data
        #To assign the value of None to self.next
        self.next=None

#A class to make the linked list
class phoneContact:
    def __init__(self):
        self.head=None
    #To check if the linked list is empty
    def isEmpty(self):
        return self.head is None
    #To delete the node
    def deleteContact(self,temp):
        if(self.isEmpty()):
            print("No Data!")
        else:
            #If the node is self.head
            if(temp==self.head):
                firstData=self.head
                self.head=firstData.next
                del firstData
            elif(temp!=self.head and temp.next is not None):
                a=self.head
                if(a.next.data==temp.data):
                    a.next=a.next.next
                    del temp                    
                else:
                    a=a.next
            elif(temp!=self.head and temp.next is None):
                a=self.head
                if(a.next.data==temp.data):
                    a.next=None
                    del temp
        print("")
        print("CONTACT DELETED!")
        print("")                         

    #To add new data to node
    def addContact(self):
        print("")
        print("ADD CONTACT")
        print("==========================")
        firstName=input("First Name       : ") .upper()
        lastName=input("Last Name        : ") .upper()
        phoneNumber=input("Phone Number     : ")
        data={'First Name':firstName,
              'Last Name':lastName,
              'Phone Number':phoneNumber}
        print("")
        print("CONTACT")
        print("================================")
        print("First Name   : ",data['First Name'])
        print("Last Name    : ",data['Last Name'])
        print("Phone Number : ",data['Phone Number'])
        print("")
        print("1. Save",end='           ')
        print("0. Cancel")
        print("")
        user=int(input("Please input your choice : "))
        if user==1:
            newData=Node(data)
            if(self.isEmpty()):
                newData.next=self.head
                self.head=newData
            else:
                temp=self.head
                while(temp.next):
                    temp=temp.next
                temp.next=newData
            print("")
            print("CONTACT SAVED!")
            print("")
        elif user==0:
            c.mainMenu()
    
    #To update the data in Node
    def updateContact(self,temp):
        end=False
        print("")
        while(end==False):
            print("1. First Name  2. Last Name  3. Phone Number  0. Main Menu")
            print("")
            user=int(input("Please enter your choice : "))
            if(user==1):
                newFirstName=input("Please enter new first name : ") .upper()
                temp.data.update({"First Name": newFirstName})
                break
            elif(user==2):
                newLastName=input("Please enter new last name : ") .upper()
                temp.data.update({"Last Name": newLastName})
                break
            elif(user==3):
                newPhoneNumber=input("Please enter new phone number : ")
                temp.data.update({"Phone Number":newPhoneNumber})
                break
            elif(user==0):
                end=True
                break
        print("")
        print("Data Updated!")
        print("")
        c.mainMenu()
    
    #To display all contact
    def displayAll(self):
        print("")
        print("CONTACT LIST : ")
        print("")
        if(self.isEmpty()):
            print("NO DATA!")
        else:
            temp=self.head
            i=1
            while(temp):
                print(f"Contact {i}")
                print("First Name   : ",temp.data['First Name'])
                print("Last Name    : ",temp.data['Last Name'])
                print("Phone Number : ",temp.data['Phone Number'])
                print("")
                i+=1
                temp=temp.next
            print("0. Back")
            print("")
            user=int(input("Please input your choice : "))
            if user==0:
                c.displayContact()  
                
    #To display one contact
    def displayContact(self):
        print("")
        print("CONTACT LIST : ")
        print("")
        if(self.isEmpty()):
            print("NO DATA!")
            print("")
            print("0. Back")
            print("")
            user=int(input("Please input your choice : "))
            if user==0:
                c.mainMenu()                    
        else:
            temp=self.head
            end=False
            i=1
            while(end==False):
                print(f"Contact {i}")
                print("=======================================")
                print("First Name   : ",temp.data['First Name'])
                print("Last Name    : ",temp.data['Last Name'])
                print("Phone Number : ",temp.data['Phone Number'])
                print("")
                print("1. Next", end='           ')
                print("2. Show all", end='           ')
                print("3. Delete",end='           ')
                print("4. Update",end='           ')
                print("0. Main Menu")
                print("")
                user=int(input("Please input your choice : "))
                if user==1:
                    if(temp.next is not None):
                        i+=1
                        temp=temp.next
                    else:
                        print("")
                        print("No Data!")
                        print("")
                elif user==2:
                    c.displayAll()
                elif user==3:
                    print("")
                    print("1. Yes", end='           ')
                    print("0. Back")
                    print("")
                    userConfirm=int(input("Are sure you want to delete this data? "))
                    if userConfirm==1:
                        c.deleteContact(temp)
                        break
                    elif userConfirm==0:
                        break
                elif user==4:
                    c.updateContact(temp)
                elif user==0:
                    end=True
                    break
            c.mainMenu()
    #Main menu
    def mainMenu(self):
        end=False
        while(end==False):
            print("")
            print("PHONE CONTACT MANAGEMENT")
            print("     BY EDWIN JAYA      ")
            print("========================")
            print("1. Add Contact")
            print("2. Show Contact")
            print("0. Exit")
            print("")
            user=int(input("Please input your choice :  "))
            if(user==1):
                c.addContact()
            elif(user==2):
                c.displayContact()
            elif(user==0):
                end=True
                exit()

#To run the program
if __name__=='__main__':
    c=phoneContact()
    c.mainMenu()
                    
        