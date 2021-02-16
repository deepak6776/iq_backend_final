from iqoptionapi.stable_api import IQ_Option
import time
import random
Iq=IQ_Option("hackeratheart@gmail.com","aswdkl;123")
Iq.connect()#connect to iqoption

ACTIVES="EURUSD"
duration=1#minute 1 or 5
amount=1
action="call"#put
print(type(ACTIVES))
print(type(duration))
print(type(amount))
print(type(action))
print(Iq.buy_digital_spot(ACTIVES,amount,action,duration))