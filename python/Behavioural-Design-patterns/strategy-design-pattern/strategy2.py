from strategy import PaymentStrategy


class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print(f'{amount}/- rs paid using UPI payment')