from celery import shared_task



@shared_task
def add(x, y):
    print(f'add({x}, {y}) = {x+y}')
    return x + y
