class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance


    def Account_Holder(self):
        print(f"Acount Holder:{self.name}")
        print(f"Balance:{self.balance}")


    def deposite(self,damount):
        self.damount=damount
        print(f"Deposite Amount:{self.damount}")                                                                                                         

                                                                                                        
                                                                                                        

    def withdraw(self,wamount):
        self.wamount=wamount
        print(f"Withdraw Amount:{self.wamount}")   

                                                                                                        

    def show_balance(self):
        self.balance=self.balance+self.damount-self.wamount
        print(f"Current balance:{self.balance}")
                                               
        if self.wamount>self.balance:
            print("Insufficient Balance")                                                                                                  
        else:
            print("Sufficient")  
                                           

T1=BankAccount("Rahul",100)
T1.Account_Holder()
T1.deposite(50)
T1.withdraw(200)
T1.show_balance()
                                                                                                        
