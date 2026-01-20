from strategy import PaymentStrategy

class CreditCard(PaymentStrategy):
    
    def pay(self, amount):
        print(f'{amount}/- rs paid using credit card')
    