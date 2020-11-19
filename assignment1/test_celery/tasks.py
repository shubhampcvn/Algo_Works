from __future__ import absolute_import
from test_celery.celery import app
from celery.schedules import crontab
from redis import StrictRedis
import redis
import pickle


@app.task
def Task_A(n, child=False):
    fib = {0:0,1:1}
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        for i in range(2, n+1):
            fib[i]=fib[i-1]+fib[i-2]
    r = redis.StrictRedis()
    p_mydict = pickle.dumps(fib)
    r.set('mydict',p_mydict)
    if child:
        return Task_B()
    else:
        return 'Created Fibonacci Series'


@app.task
def Task_B():
    r = redis.StrictRedis()
    read_dict = r.get('mydict')
    res_dict = pickle.loads(read_dict)
    if res_dict:
        return res_dict
    else:
        return 'No fibonacci series found'


#To run at specifid time
app.conf.beat_schedule = {
    "run-me-on-monday": {
        "task": "tasks.Task_A",
        "schedule": crontab(hour=7, minute=30, day_of_week=1),
        "args":(10,)
 }
}

#TO run periodically
app.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
        "task": "tasks.Task_B",
        "schedule": 10.0
    }
}