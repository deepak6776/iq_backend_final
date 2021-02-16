from iqoptionapi.stable_api import IQ_Option
import logging
import time
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
Iq=IQ_Option("hackeratheart@gmail.com","aswdkl;123")

Iq.connect()#connect to iqoption
# ACTIVES="EURUSD"
# duration=1#minute 1 or 5
# amount=1
# action="call"#put

# print("__For_Binary_Option__")
# _,id=Iq.buy(amount,ACTIVES,action,duration)
# while Iq.get_async_order(id)==None:
#     pass
# print(Iq.get_async_order(id))
# print("\n\n")
#
# print("__For_Digital_Option__spot")
# _,id=Iq.buy_digital_spot(ACTIVES,amount,action,duration)
# while Iq.get_async_order(id)==None:
#     pass
# order_data=Iq.get_async_order(id)
# print(Iq.get_async_order(id))
# print("\n\n")

instrumentid_tmp = "BTCUSD"
instrumenttype_tmp = "crypto"
direction_tmp = "buy"
leverage_tmp = 3
# starttimehour_tmp = ""
# starttimeminute_tmp = ""
# stoptimehour_tmp = ""
# stoptimeminute_tmp = ""
# day_str =
amount_tmp = 712
print("Instrument ID: {} Instrument Type: {} Buy/Sell: {} Leverage: {} Amount: {}".format(instrumentid_tmp, instrumenttype_tmp, direction_tmp, leverage_tmp, amount_tmp))
print("__For_Forex_Stock_Commodities_Crypto_ETFs")
# instrument_type="crypto"
# instrument_id="BTCUSD"
# side="buy"
# amount=1.23
# leverage=3

instrument_type = instrumenttype_tmp
instrument_id = instrumentid_tmp
side = direction_tmp
amount = amount_tmp
leverage = leverage_tmp

type="market"
limit_price=None
stop_price=None
stop_lose_kind="percent"
stop_lose_value=95
take_profit_kind=None
take_profit_value=None
use_trail_stop=True
auto_margin_call=False
use_token_for_commission=False
print("instrument_type: {},"
      "instrument_id: {},"
      "side: {},"
      "leverage: {},"
      "type: {},"
      "limit_price: {},"
      "stop_price: {},"
      "stop_lose_value: {},"
      "take_profit_value: {},"
      "take_profit_kind: {},"
      "use_trail_stop: {},"
      "auto_margin_call: {},"
      "use_token_for_commission: {}".format(instrument_type,instrument_id,side,amount,leverage,
                                            type,limit_price,stop_price,stop_lose_value,stop_lose_kind,
                                            take_profit_value,take_profit_kind,use_trail_stop,auto_margin_call,
                                            use_token_for_commission))
check,id=Iq.buy_order(instrument_type=instrument_type, instrument_id=instrument_id,
            side=side, amount=amount,leverage=leverage,
            type=type,limit_price=limit_price, stop_price=stop_price,
            stop_lose_value=stop_lose_value, stop_lose_kind=stop_lose_kind,
            take_profit_value=take_profit_value, take_profit_kind=take_profit_kind,
            use_trail_stop=use_trail_stop, auto_margin_call=auto_margin_call,
            use_token_for_commission=use_token_for_commission)
while Iq.get_async_order(id)==None:
    pass
order_data=Iq.get_async_order(id)
print(Iq.get_async_order(id))