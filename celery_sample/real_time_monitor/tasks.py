import time
from celery.decorators import task

@task
def run():
    time.sleep(10)
    print('処理　おわた')
    return 'おわったよ'


@task
def calc(a, b):
    return a+b
