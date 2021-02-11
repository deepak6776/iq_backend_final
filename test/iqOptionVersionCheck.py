from iqoptionapi.stable_api import IQ_Option

Iq = IQ_Option("deepak.enka@gmail.com", "aswdkl;123")
print(IQ_Option.__version__)
# print(Iq.SESSION_COOKIE)
Iq.connect()
print(Iq.check_connect())
balance_type="PRACTICE"
Iq.change_balance(balance_type)