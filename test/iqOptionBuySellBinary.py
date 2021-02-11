from iqoptionapi.stable_api import IQ_Option
import logging
import time
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("hackeratheart@gmail.com", "aswdkl;123")
# Iq = IQ_Option(content['email'], content['password'])
Iq.connect()
res = Iq.get_balance()
print(res)
print(Iq.check_connect())
goal="EURUSD"
# # print("get candles")
# # print(Iq.get_candles(goal,60,111,time.time()))
Money=1
ACTIVES="EURUSD"
ACTION="call"#or "put"
expirations_mode=1
#
check,id=Iq.buy(Money,ACTIVES,ACTION,expirations_mode)
if check:
    print("!buy!")
else:
    print("buy fail")