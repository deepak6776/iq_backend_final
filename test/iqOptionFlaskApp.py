from flask import Flask
from pytz import utc
import logging
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.jobstores.mongodb import MongoDBJobStore
from datetime import datetime, timedelta
import os


def myfunction(jobid, name):
    logging.info("{}: jobId, {}: name".format(jobid, name))


def alarm(time):
    print('Alarm! This alarm was scheduled at %s.' % time)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    scheduler = BlockingScheduler()
    scheduler.add_jobstore(database='iqoption',collection='jobs',jobstore='mongodb')
    # scheduler.add_jobstore('mongodb', collection='example_jobs')
    if len(sys.argv) > 1 and sys.argv[1] == '--clear':
        scheduler.remove_all_jobs()

    alarm_time = datetime.now() + timedelta(seconds=10)
    scheduler.add_job(alarm, 'interval', seconds=5, args=[datetime.now()])
    print('To clear the alarms, run this example with the --clear argument.')
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass