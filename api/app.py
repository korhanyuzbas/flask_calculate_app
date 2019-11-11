import logging

from flask import Flask, request

from worker import celery

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    task = celery.send_task('tasks.calculate_numbers', kwargs=request.get_json())
    return str(task.id), 200


@app.route('/callback/<task_id>', methods=['GET'])
def callback(task_id):
    res = celery.AsyncResult(task_id)
    return str(res.result), 200
