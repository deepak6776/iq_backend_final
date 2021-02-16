from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource, reqparse
from src.common.database import Database
from iqoptionapi.stable_api import IQ_Option
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from datetime import datetime, timedelta
import os
import sys
from pytz import utc
import time


__author__ = 'Deepak'


app = Flask(__name__)
api = Api(app)

scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Kolkata'})
scheduler.add_jobstore(jobstore='mongodb', database='iqoption', collection='jobs')


@app.before_first_request
def initialize_database():
    Database.initialize()


def testfunc(jobid,
             email,
             password,
             instrumentid_tmp,
             instrumenttype_tmp,
             direction_tmp,
             leverage_tmp,
             starttimehour_tmp,
             starttimeminute_tmp,
             stoptimehour_tmp,
             stoptimeminute_tmp,
             day_str,
             amount_tmp):
    print("{}: JobId executing... current time {}".format(jobid, datetime.now()))
    print("{}: JobId parameters "
          "{}: email"
          "{}: password"
          "instrumentId: {} "
          "instrumentType: {} "
          "diection_tmp: {} "
          "leverage_tmp: {}"
          "starttimehour_tmp: {}"
          "starttimeminute_tmp: {}"
          "stoptimehour_tmp: {}"
          "stoptimeminute_tmp: {}"
          "day_str: {}"
          "amount_tmp: {}".format(jobid,email,password,instrumentid_tmp,
                                  instrumenttype_tmp,
                                  direction_tmp,
                                  leverage_tmp,
                                  starttimehour_tmp,
                                  starttimeminute_tmp,
                                  stoptimehour_tmp,
                                  stoptimeminute_tmp,
                                  day_str,
                                  amount_tmp))
    if instrumenttype_tmp == 'BINARY' or instrumenttype_tmp == 'binary':
        print("In binary")
        Iq = IQ_Option(email=email, password=password)
        # Iq = IQ_Option("hackeratheart@gmail.com", "aswdkl;123")
        Iq.connect()
        print(Iq.connect())
        # Money = 1
        # ACTIVES = "EURUSD"
        Money = int(amount_tmp)
        ACTIVES = instrumentid_tmp
        if direction_tmp == "BUY":
            ACTION = "call"  # or "put"
        else:
            ACTION = "put"
        expirations_mode = 1
        check, id = Iq.buy(Money, ACTIVES, ACTION, expirations_mode)
        if check:
            print("{}: JobId {} {} at {}".format(jobid,ACTIVES,ACTION ,datetime.now()))
        else:
            print("buy fail")
    elif instrumenttype_tmp == 'DIGITAL' or instrumenttype_tmp == 'digital':
        print("In digital!")
        Iq = IQ_Option(email=email, password=password)
        # Iq = IQ_Option("hackeratheart@gmail.com", "aswdkl;123")
        Iq.connect()
        print(Iq.connect())
        # Money = 1
        # ACTIVES = "EURUSD"
        Money = int(amount_tmp)
        ACTIVES = str(instrumentid_tmp)
        if direction_tmp == "BUY":
            ACTION = "call"  # or "put"
        else:
            ACTION = "put"
        DURATION = 1
        print("Money: {} ACTIVES: {} ACTION: {} expiration_mode: {}".format(Money,ACTIVES,ACTION,DURATION))
        # print(type(Money))
        # print(type(ACTIVES))
        # print(type(ACTION))
        # print(type(DURATION))
        check, id = Iq.buy_digital_spot(ACTIVES, Money, ACTION, DURATION)
        if check:
            print("{}: JobId {} {} at {}".format(jobid, ACTIVES, ACTION, datetime.now()))
        else:
            print("buy fail")
    else:
        Iq = IQ_Option(email=email, password=password)
        # Iq = IQ_Option("hackeratheart@gmail.com", "aswdkl;123")
        Iq.connect()
        print(Iq.connect())
        print("__For_Forex_Stock_Commodities_Crypto_ETFs")
        instrument_type = instrumenttype_tmp.lower()
        print(instrument_type)
        instrument_id = instrumentid_tmp
        if direction_tmp == "BUY":
            side = "buy"  # or "put"
        else:
            side = "sell"
        amount = int(amount_tmp)
        leverage = int(leverage_tmp)
        type = "market"
        limit_price = None
        stop_price = None
        stop_lose_kind = "percent"
        stop_lose_value = 95
        take_profit_kind = None
        take_profit_value = None
        use_trail_stop = True
        auto_margin_call = False
        use_token_for_commission = False
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
              "use_token_for_commission: {}".format(instrument_type, instrument_id, side, amount, leverage,
                                                    type, limit_price, stop_price, stop_lose_value, stop_lose_kind,
                                                    take_profit_value, take_profit_kind, use_trail_stop,
                                                    auto_margin_call,
                                                    use_token_for_commission))
        check, id = Iq.buy_order(instrument_type=instrument_type, instrument_id=instrument_id,
                                           side=side, amount=amount, leverage=leverage,
                                           type=type, limit_price=limit_price, stop_price=stop_price,
                                           stop_lose_value=stop_lose_value, stop_lose_kind=stop_lose_kind,
                                           take_profit_value=take_profit_value, take_profit_kind=take_profit_kind,
                                           use_trail_stop=use_trail_stop, auto_margin_call=auto_margin_call,
                                           use_token_for_commission=use_token_for_commission)
        # if check:
        #     print(check)
        # else:
        #     print("no check")
        if check:
            print("{}: JobId {} {} at {}".format(jobid, instrument_type, instrument_id, datetime.now()))
        else:
            print("buy fail")

        while Iq.get_async_order(id) == None:
            pass

        order_data = Iq.get_async_order(id)
        print(Iq.get_async_order(id))
        # while Iq.get_async_order(id) == None:
        #     pass
        # order_data = Iq.get_async_order(id)
        # print(Iq.get_async_order(id))
    # print(instrumentid_tmp)
    # print(instrumenttype_tmp)
    # print(direction_tmp)
    # print(leverage_tmp)
    # print(starttimehour_tmp)
    # print(starttimeminute_tmp)
    # print(stoptimehour_tmp)
    # print(stoptimeminute_tmp)
    # print(day_str)
    # print(amount_tmp)


class Hello(Resource):
    @staticmethod
    def get():
        return "hello!"


class Login(Resource):
    @staticmethod
    def __pos__():
        content = request.get_json(silent=True)
        print(content)
        Database.insert_one(collection="user", data=content)
        return "Success"


class CheckBalance(Resource):
    @staticmethod
    def post():
        content = request.get_json(silent=True)
        print(content)
        Database.insert_one(collection="user", data=content)
        print(content['email'])
        Iq = IQ_Option(content['email'],content['password'])
        Iq.connect()
        res = Iq.get_balance()
        print(res)
        return res
        # if content['deviceId'] == 'AABBCCDDEEFF':
        #     record = Database.find_one(collection="onboarding", query={"device_id": "AABBCCDDEEFF"})
        #     print(record)
        #     return record
        # else:
        #     return "invalid deviceId"


class PlaceBet(Resource):
    @staticmethod
    def post():
        content = request.get_json(silent=True)
        print(content)
        print(type(content))
        Database.insert_one(collection="bets", data=content)
        return "Success"
        # if content['deviceId'] == 'AABBCCDDEEFF':
        #     record = Database.find_one(collection="onboarding", query={"device_id": "AABBCCDDEEFF"})
        #     print(record)
        #     return record
        # else:
        #     return "invalid deviceId"


class PlaceSchedule(Resource):
    @staticmethod
    def post():
        content = request.get_json(silent=True)
        print(content)
        print(type(content))
        Database.insert_one(collection="schedule", data=content)
        starthour = content['startTimeHour'] + content['startTimeMinute']
        print(starthour)
        print(type(starthour))
        return "Success"
        # if content['deviceId'] == 'AABBCCDDEEFF':
        #     record = Database.find_one(collection="onboarding", query={"device_id": "AABBCCDDEEFF"})
        #     print(record)
        #     return record
        # else:
        #     return "invalid deviceId"


class PlacePanel(Resource):
    @staticmethod
    def post():
        content = request.get_json(silent=True)
        email = content['email']
        password = content['password']
        print(content)
        print(type(content))
        Database.insert_one(collection="panel", data=content)
        jobid = str(time.time())
        print(jobid)
        bet_record = Database.find_one(collection='bets', query={'betName':content['betName']})
        print(content['betName'])
        print("betrecord:{} ".format(bet_record))
        sch_record = Database.find_one(collection='schedule', query={'scheduleName':content['scheduleName']})
        print(sch_record)
        instrumentid_tmp = bet_record['instrumentId']
        instrumenttype_tmp = bet_record['instrumentType']
        print("betrecord:{} ".format(bet_record))
        print("instrument Type: {}".format(instrumenttype_tmp))
        print("instrument Id: {}".format(instrumentid_tmp))
        direction_tmp = bet_record['side']
        leverage_tmp = bet_record['leverage']
        starttimehour_tmp = sch_record['startTimeHour']
        starttimeminute_tmp = sch_record['startTimeMinute']
        stoptimehour_tmp = sch_record['stopTimeHour']
        stoptimeminute_tmp = sch_record['stopTimeMinute']
        print(sch_record['formDays'])
        tmp_arr = sch_record['formDays']
        print(tmp_arr)
        print(len(tmp_arr))
        len_arr = len(tmp_arr)
        day_str = ''
        for i in range(len_arr):
            tmp = tmp_arr[i]
            if i == len(tmp_arr) - 1:
                day_str = day_str + tmp[0:3]
            else:
                day_str = day_str + tmp[0:3] + ','
            print("{}: value {}, day string: {}".format(i, tmp_arr[i], day_str))
        # monday_tmp = sch_record['monday']
        # tuesday_tmp = sch_record['tuesday']
        # wednesday_tmp = sch_record['wednesday']
        # thursday_tmp = sch_record['thursday']
        # friday_tmp = sch_record['friday']
        # saturday_tmp = sch_record['saturday']
        # sunday_tmp = sch_record['sunday']
        amount_tmp = content['amount']
        # hour_str = starttimehour_tmp + starttimeminute_tmp + "-" + stoptimehour_tmp + stoptimeminute_tmp
        # hour_str = starttimehour_tmp + "-" + stoptimehour_tmp
        hour_str = starttimehour_tmp
        min_str = starttimeminute_tmp
        print("instrument Type: {}".format(instrumenttype_tmp))
        print("instrument Id: {}".format(instrumentid_tmp))
        # if monday_tmp:
        #     day_str = day_str + 'mon'
        # if tuesday_tmp:
        #     day_str = day_str + ',tue'
        # if wednesday_tmp:
        #     day_str = day_str + ',wed'
        # if thursday_tmp:
        #     day_str = day_str + ',thu'
        # if friday_tmp:
        #     day_str = day_str + ',fri'
        # if saturday_tmp:
        #     day_str = day_str + ',sat'
        # if sunday_tmp:
        #     day_str = day_str + ',sun'
        print(day_str)
        print('hour string: {}'.format(hour_str))

        scheduler.add_job(testfunc, 'cron',
                          hour=hour_str,
                          minute=min_str,
                          day_of_week=day_str,
                          month='*',
                          year='*',
                          id=jobid,
                          args=[
                              jobid,
                              email,
                              password,
                              instrumentid_tmp,
                              instrumenttype_tmp,
                              direction_tmp,
                              leverage_tmp,
                              starttimehour_tmp,
                              starttimeminute_tmp,
                              stoptimehour_tmp,
                              stoptimeminute_tmp,
                              day_str,
                              amount_tmp
                          ])

        # scheduler.add_job(testfunc, 'cron',
        #                   # hour=hour_str,
        #                   # minute=min_str,
        #                   # day_of_week=day_str,
        #                   # month='*',
        #                   # year='*',
        #                   # id=jobid,
        #                   next_run_time=datetime.now(),
        #                   args=[
        #                       jobid,
        #                       instrumentid_tmp,
        #                       instrumenttype_tmp,
        #                       direction_tmp,
        #                       leverage_tmp,
        #                       starttimehour_tmp,
        #                       starttimeminute_tmp,
        #                       stoptimehour_tmp,
        #                       stoptimeminute_tmp,
        #                       day_str,
        #                       amount_tmp
        #                   ])


        return "Success"

        # scheduler.add_job(testfunc,
        #                   'interval',
        #                   seconds=5,
        #                   id=jobid,
        #                   args=[
        #                       jobid,
        #                       instrumentid_tmp,
        #                       instrumenttype_tmp,
        #                       direction_tmp,
        #                       leverage_tmp,
        #                       starttimehour_tmp,
        #                       starttimeminute_tmp,
        #                       stoptimehour_tmp,
        #                       stoptimeminute_tmp,
        #                       monday_tmp,
        #                       tuesday_tmp,
        #                       wednesday_tmp,
        #                       thursday_tmp,
        #                       friday_tmp,
        #                       saturday_tmp,
        #                       sunday_tmp,
        #                       amount_tmp
        #                   ])
        # if content['deviceId'] == 'AABBCCDDEEFF':
        #     record = Database.find_one(collection="onboarding", query={"device_id": "AABBCCDDEEFF"})
        #     print(record)
        #     return record
        # else:
        #     return "invalid deviceId"


api.add_resource(CheckBalance, '/checkbalance')
api.add_resource(PlaceBet, '/placebet')
api.add_resource(PlaceSchedule, '/placeschedule')
api.add_resource(PlacePanel, '/placepanel')
api.add_resource(Hello, '/')
api.add_resource(Login, '/')


scheduler.start()
if __name__ == "__main__":
    app.run(debug=True)