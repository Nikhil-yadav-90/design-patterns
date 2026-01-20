from context import PaymentContext
from strategy1 import CreditCard
from strategy2 import UpiPayment
from strategy3 import NetBanking

payment1 = PaymentContext(CreditCard())

payment1.pay(500)


payment2 = PaymentContext(UpiPayment())

payment2.pay(1000)

payment3 = PaymentContext(NetBanking())

payment3.pay(5000)
