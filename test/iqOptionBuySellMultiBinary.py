from iqoptionapi.stable_api import IQ_Option
import logging
import time
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("hackeratheart@gmail.com", "aswdkl;123")
# Iq = IQ_Option(content['email'], content['password'])
Iq.connect()
Money=[]
ACTIVES=[]
ACTION=[]
expirations_mode=[]
res = Iq.get_balance()
print(res)
print(Iq.check_connect())
Money.append(1)
ACTIVES.append("EURUSD")
ACTION.append("call")#put
expirations_mode.append(1)

Money.append(1)
ACTIVES.append("EURAUD")
ACTION.append("call")#put
expirations_mode.append(1)

print("buy multi")
id_list=Iq.buy_multi(Money,ACTIVES,ACTION,expirations_mode)

print("check win only one id (id_list[0])")
print(Iq.check_win_v2(id_list[0],2))
