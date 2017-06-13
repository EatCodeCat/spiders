from apscheduler.schedulers.blocking import BlockingScheduler


sch = BlockingScheduler()

sch.add_job(lambda :print('1'))

sch.start()

sch.add_job(lambda :print('2'))
sch.start()
