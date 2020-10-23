from apscheduler.schedulers.background import BackgroundScheduler
from cita.update import update_somthing

from apscheduler.triggers.cron import CronTrigger
trigger = CronTrigger(hour='12', minute='00')

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_somthing, trigger, replace_existing=True, max_instances=1, id='reminder1')
    scheduler.start()
