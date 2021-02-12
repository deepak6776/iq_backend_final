from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from pytz import utc
import datetime

def test(jobname):
    print("{}: Hi from {}".format(datetime.datetime.now(), jobname))


if __name__ == "__main__":
    scheduler = BlockingScheduler({'apscheduler.timezone': 'UTC'})
    # scheduler.add_jobstore(jobstore='mongodb', database='iqoption')
    scheduler.add_job(test,'cron',day='*',hour='9',minute='18',args=['test'])
    scheduler.start()