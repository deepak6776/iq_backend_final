import time
from iqoptionapi.stable_api import IQ_Option
import json
import logging

# logging level
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

Iq = IQ_Option("deepak.enka@gmail.com", "aswdkl;123")

# connect to iqoption
check, reason = Iq.connect()

print(check, reason)

# connect to iq option
Iq.connect()

goal="EURUSD"
print("get candles")

iqCandles = Iq.get_candles(goal, 60, 111, time.time())
iqCandles_json = json.dumps(iqCandles)
print(type(iqCandles))
print(type(iqCandles_json))
print(iqCandles)
print(iqCandles_json)