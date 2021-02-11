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

scheduler = BackgroundScheduler()
scheduler.add_jobstore(jobstore='mongodb', database='iqoption', collection='jobs')

@app.before_first_request
def initialize_database():
    Database.initialize()


def testfunc(jobid,
             instrumentid_tmp,
             instrumenttype_tmp,
             direction_tmp,
             leverage_tmp,
             starttimehour_tmp,
             starttimeminute_tmp,
             stoptimehour_tmp,
             stoptimeminute_tmp,
             monday_tmp,
             tuesday_tmp,
             wednesday_tmp,
             thursday_tmp,
             friday_tmp,
             saturday_tmp,
             sunday_tmp,
             amount_tmp):
    print("Test function")
    print(instrumentid_tmp)
    print(instrumenttype_tmp)
    print(direction_tmp)
    print(leverage_tmp)
    print(starttimehour_tmp)
    print(starttimeminute_tmp)
    print(stoptimehour_tmp)
    print(stoptimeminute_tmp)
    print(monday_tmp)
    print(tuesday_tmp)
    print(wednesday_tmp)
    print(thursday_tmp)
    print(friday_tmp)
    print(saturday_tmp)
    print(sunday_tmp)
    print(amount_tmp)


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
        starthour = content['starttimehour'] + content['starttimeminute']
        print(starthour)
        print(type(starthour))
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
        print(content)
        print(type(content))
        Database.insert_one(collection="panel", data=content)
        jobid = str(time.time())
        print(jobid)
        bet_record = Database.find_one(collection='bets', query={'betname':content['betname']})
        sch_record = Database.find_one(collection='schedule', query={'schedulename':content['schedulename']})
        instrumentid_tmp = bet_record['instrumentid']
        instrumenttype_tmp = bet_record['instrumenttype']
        direction_tmp = bet_record['direction']
        leverage_tmp = bet_record['leverage']
        starttimehour_tmp = sch_record['starttimehour']
        starttimeminute_tmp = sch_record['starttimeminute']
        stoptimehour_tmp = sch_record['stoptimehour']
        stoptimeminute_tmp = sch_record['stoptimeminute']
        monday_tmp = sch_record['monday']
        tuesday_tmp = sch_record['tuesday']
        wednesday_tmp = sch_record['wednesday']
        thursday_tmp = sch_record['thursday']
        friday_tmp = sch_record['friday']
        saturday_tmp = sch_record['saturday']
        sunday_tmp = sch_record['sunday']
        amount_tmp = content['amount']
        hour_str = starttimehour_tmp + starttimeminute_tmp + "-" + stoptimehour_tmp + stoptimeminute_tmp
        day_str = ''
        if monday_tmp:
            day_str = day_str + 'mon'
        if tuesday_tmp:
            day_str = day_str + ',tue'
        if wednesday_tmp:
            day_str = day_str + ',wed'
        if thursday_tmp:
            day_str = day_str + ',thu'
        if friday_tmp:
            day_str = day_str + ',fri'
        if saturday_tmp:
            day_str = day_str + ',sat'
        if sunday_tmp:
            day_str = day_str + ',sun'
        print(day_str)
        print('hour string: {}'.format(hour_str))

        scheduler.add_job(testfunc, 'cron',
                          hour=hour_str,
                          day_of_week=day_str,
                          month='*',
                          year='*',
                          id=jobid,
                          args=[
                              jobid,
                              instrumentid_tmp,
                              instrumenttype_tmp,
                              direction_tmp,
                              leverage_tmp,
                              starttimehour_tmp,
                              starttimeminute_tmp,
                              stoptimehour_tmp,
                              stoptimeminute_tmp,
                              monday_tmp,
                              tuesday_tmp,
                              wednesday_tmp,
                              thursday_tmp,
                              friday_tmp,
                              saturday_tmp,
                              sunday_tmp,
                              amount_tmp
                          ])

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

scheduler.start()
if __name__ == "__main__":
    app.run(debug=True)