from iqoptionapi.stable_api import IQ_Option
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

Iq = IQ_Option("deepak.enka@gmail.com", "aswdkl;123")

# Default is "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

header = {"User-Agent":r"Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}

cookie = {"Iq": "BAD"}

Iq.set_session(header, cookie)

# connect to iqoption
Iq.connect()