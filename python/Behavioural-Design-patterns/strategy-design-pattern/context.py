from strategy import PaymentStrategy




class PaymentContext:
    def __init__(self, payment: PaymentStrategy):
        self.strategy = payment
    
    def pay(self, amount):
        self.strategy.pay(amount)
