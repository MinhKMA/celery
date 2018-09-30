from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://admin:minhkma@192.168.100.65:5672/admin_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])
