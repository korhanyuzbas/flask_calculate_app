import os
import traceback
import logging

from celery import Celery

logger = logging.getLogger(__name__)

CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL',
    'amqp://zixqbnan:5qjxmQD3rLrp-RzhcbVFvRLMdHy9wcxv@whale.rmq.cloudamqp.com/zixqbnan'
)

CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND',
    'amqp://zixqbnan:5qjxmQD3rLrp-RzhcbVFvRLMdHy9wcxv@whale.rmq.cloudamqp.com/zixqbnan'
)

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.calculate_numbers')
def calculate_numbers(first_number: float, second_number: float):
    # takes two floating numbers, multiply those numbers and returns result
    result = ''
    try:
        result = first_number * second_number
    except:
        logger.error(traceback.format_exc())
    return result
