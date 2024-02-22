from icecream import ic
from functools import wraps, update_wrapper
import time
from django.db import connection, reset_queries


def countQueriesDecorator(view_func):
    @wraps(view_func)
    def wrapped_function(*args, **kwargs):
        reset_queries()
        response = view_func(*args, **kwargs)
        for query in connection.queries:
            ic(query['sql'], "\n")
        ic(len(connection.queries))
        return response
    return wrapped_function


def timeCountDecorator(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        startTime = time.perf_counter()
        response = view_func(request, *args, **kwargs)
        endTime = time.perf_counter()
        executionTime = endTime - startTime
        ic(executionTime)  # ic(view_func.__name__, executionTime)
        return response
    return wrapped_view


def combinedCheckTimeAndSqlDecorator(func):
    # @countQueriesDecorator
    @timeCountDecorator
    def wrapper(*args, **kwargs):
        ic(func.__name__)
        return func(*args, **kwargs)
    return wrapper
