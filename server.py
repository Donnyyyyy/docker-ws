from flask import Flask
from redis import Redis
from rq import Queue
from rq.job import Job
from rq.exceptions import NoSuchJobError

from task import process_user


redis = Redis.from_url('redis://service_redis:6379')
q = Queue(connection=redis)
app = Flask(__name__)

@app.route('/<uid>')
def enqueue(uid):
    job = q.enqueue(process_user, uid)
    return job.id

@app.route('/result/<job_id>')
def get_job_result(job_id):
    try:
        job = Job.fetch(job_id, connection=redis)
    except NoSuchJobError:
        return 'No such job'

    return job.result if job.result else 'Not yet completed'

app.run(host='0.0.0.0', port=8080)
