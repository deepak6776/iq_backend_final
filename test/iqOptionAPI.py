from iqoptionapi.stable_api import IQ_Option
import logging
import time

I = IQ_Option("hackeratheart@gmail.com", "aswdkl;123")
check, reason = I.connect()
print(check, reason)
res = I.get_balance()
print(res)
# print(res["id"])
