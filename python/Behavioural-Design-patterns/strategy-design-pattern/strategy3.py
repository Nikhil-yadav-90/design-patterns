from strategy import PaymentStrategy


class NetBanking(PaymentStrategy):

    def pay(self, amount):
        print(f'{amount}/- rs paid using net banking')
