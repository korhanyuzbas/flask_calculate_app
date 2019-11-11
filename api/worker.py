import os
from celery import Celery

CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL',
    'amqp://zixqbnan:5qjxmQD3rLrp-RzhcbVFvRLMdHy9wcxv@whale.rmq.cloudamqp.com/zixqbnan'
)

CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND',
    'amqp://zixqbnan:5qjxmQD3rLrp-RzhcbVFvRLMdHy9wcxv@whale.rmq.cloudamqp.com/zixqbnan'
)

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
