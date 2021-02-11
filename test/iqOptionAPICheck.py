from iqoptionapi.stable_api import IQ_Option
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("deepak.enka@gmail.com", "aswdkl;123")
check, reason=Iq.connect()#connect to iqoption
print(check, reason)