class ATM :
    def __init__(self, cardNumber, pinNumber):

        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def BalanceInquiry(self):
        print("you balance is ______")

    def CashWithdrawal(self):
        print(" withdraw is processing")

    def ChangePin(self):
        pin = str(input("Type the new Pin "))
        print("Your new pin is " + pin)

person1 = ATM("0111 0011 00001", "123456")
person1.ChangePin()

person2 = ATM("3422 5633 99981", "874564")
person2.BalanceInquiry()

person2 = ATM("1233 3344 44556", "879675")
person2.CashWithdrawal()

    
