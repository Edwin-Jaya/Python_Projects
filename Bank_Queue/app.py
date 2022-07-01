#Import the LinkedListQueue.py as ll variable
import LinkedListQueue as ll

class BankQueue:
    def __init__(self):
        self.counterOne=0
        self.counterTwo=0
        self.counterVip=0
    
    def interface(self):
        print("")
        print("NATIONAL BANK OF DA GIGA CHAD")
        print("=============================")
        print("ONE",end="           ")
        print("TWO",end="           ")
        print("VIP")
        print(self.counterOne,end="             ")
        print(self.counterTwo,end="             ")
        print(self.counterVip)
        print("")
        print("NEXT REGULAR : ",b.peek())
        print("NEXT VIP     : ",v.peek())

    def mainMenu(self):
        end=False
        while(end==False):
            q.interface()
            print("")
            print("TICKET   : ")
            print("")
            print("1.REGULAR(R)",end="             ")
            print("2.VIP(V)")
            print("")
            print("CALL     : ")
            print("")
            print("3.R TO COUNTER ONE",end="         ")
            print("4.R TO COUNTER TWO")
            print("5.V TO VIP COUNTER",end="         ")
            print("0.EXIT")
            print("")
            user=int(input("Please input your option : "))
            if(user==1):
                b.enqueue()
            elif(user==2):
                v.enqueue()
            elif(user==3):
                self.counterOne=b.dequeue()
            elif(user==4):
                self.counterTwo=b.dequeue()
            elif(user==5):
                self.counterVip=v.dequeue()
            elif(user==0):
                end=True
                exit()

#To run the program
if __name__ =='__main__':
    b=ll.linkedListRegular()
    v=ll.linkedListVIP()
    q=BankQueue()
    q.mainMenu()
       