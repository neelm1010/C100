class ATM:
        def __init__(self,CashWithdrawal, BalanceEnquiry):
            self.BalanceEnquiry=BalanceEnquiry
            self.CashWithdrawal=CashWithdrawal

    
        
        def withdrew(self):
          print("withdrew")
            
        
       

        def balance(self):
            print("in account") 
        

Cash=ATM(100, 350)
       
print(Cash.CashWithdrawal)
Cash.withdrew()
