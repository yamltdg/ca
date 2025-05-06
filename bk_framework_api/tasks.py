from celery import current_app


# 使用 current_app.task 定义任务
@current_app.task
def multiply(x, y):
    return x * y


@current_app.task
def add(x, y):
    z = x + y
    return z
