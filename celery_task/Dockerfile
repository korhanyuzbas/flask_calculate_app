FROM python:3.7.4-alpine

ENV CELERY_BROKER_URL amqp://zixqbnan:5qjxmQD3rLrp-RzhcbVFvRLMdHy9wcxv@whale.rmq.cloudamqp.com/zixqbnan
ENV CELERY_RESULT_BACKEND amqp://zixqbnan:5qjxmQD3rLrp-RzhcbVFvRLMdHy9wcxv@whale.rmq.cloudamqp.com/zixqbnan
ENV C_FORCE_ROOT true

COPY . /queue
WORKDIR /queue

RUN pip install -r requirements.txt

ENTRYPOINT celery -A tasks worker --loglevel=info