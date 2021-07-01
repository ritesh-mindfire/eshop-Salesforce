from celery import shared_task

@shared_task(name='custom_add')
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y
