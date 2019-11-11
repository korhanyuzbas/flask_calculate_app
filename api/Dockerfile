FROM python:3.7.4-alpine

ENV CELERY_BROKER_URL amqp://zixqbnan:5qjxmQD3rLrp-RzhcbVFvRLMdHy9wcxv@whale.rmq.cloudamqp.com/zixqbnan
ENV CELERY_RESULT_BACKEND amqp://zixqbnan:5qjxmQD3rLrp-RzhcbVFvRLMdHy9wcxv@whale.rmq.cloudamqp.com/zixqbnan
ENV C_FORCE_ROOT true

ENV DEBUG true
ENV FLASK_APP app
ENV FLASK_ENV development

COPY . /api
WORKDIR /api

# install requirements
RUN pip install -r requirements.txt

# expose the app port
EXPOSE 5001

CMD python -m flask run --host 0.0.0.0 --port 5001