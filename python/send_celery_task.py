import os

broker_url = os.getenv('REDIS_HOST', 'redis://default:llmapp123456@127.0.0.1:6379/1')
result_backend = os.getenv('REDIS_HOST', 'redis://default:llmapp123456@127.0.0.1:6379/1')

accept_content = ['json']
task_serializer = 'json'
timezone = 'UTC'
result_serializer = 'json'
enable_utc = True

task_acks_late = True
task_acks_on_failure_or_timeout = False
task_track_started = True
task_time_limit = 6010
task_soft_time_limit = 6000
task_default_exchange_type = 'direct'
broker_connection_retry_on_startup = True

----


from celery import Celery
from configs import celery_config


celery = Celery()
celery.config_from_object(celery_config)

celery.send_task('tasks.add', args=(2, 2), queue='tasks_add')
