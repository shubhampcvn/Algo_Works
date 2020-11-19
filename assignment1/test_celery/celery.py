from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/1',
             include=['test_celery.tasks',])
