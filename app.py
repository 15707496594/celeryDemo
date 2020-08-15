from celery import Celery

app = Celery(
    'demo',
    broker='redis://:admin@localhost:6379/2',
    backend='redis://:admin@localhost:6379/1',
    include=[
        'sms.tasks',
    ]
)

app.conf.update(
    result_expires=3600,
)


if __name__ == '__main__':
    app.start()
