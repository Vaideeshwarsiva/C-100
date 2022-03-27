class Atm:
    def __init__(self, cardNumber, pinNumber, balance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = balance
    
    def CashWithdrawl(self, Atm):
        withdraw = input("How much cash do you want to withdraw? ")
        
        length = 0

        for i in self.cardNumber:
            if length >= 10:
                print(i, end="")
                length += 1
            else:
                print("*", end="")
                length += 1
        print("\n")
    
    def BalanceEnquiry(self, Atm):
        print(self.balance)
        

cardNumberInput = input("Enter 16 digit card number: ")

while(True):
    if len(cardNumberInput) > 16 or len(cardNumberInput) < 16:
        print("Please enter a 16 digit card number")
        cardNumberInput = input("Enter 16 digit card number: ")
        continue
    else:
        break

balance = Atm(cardNumberInput, '2', '4000')
balance.BalanceEnquiry(balance)     
