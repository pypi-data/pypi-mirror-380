# completime - Powerful numbers conversion library
# Copyright (c) 2025 Treizd
#
# This file is part of numersys.
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the MIT License. See the LICENSE file for details.


from functools import wraps
import datetime

def timer(output: bool = True):
    """
    Timer decorator. Only for sync functions.
    
    :param output: Should the time of completion be printed or only returned.
    :type output: :obj:`bool`
    
    :return: Time of completion.
    :rtype: :obj:`datetime.timedelta`
    
    """
    
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs) -> datetime.timedelta:
            time_start = datetime.datetime.now()
            result = f(*args, **kwargs)
            time_end = datetime.datetime.now()
            duration = time_end - time_start
            
            if output:
                print(f"Function {f.__name__} took {duration}")
            
            return duration
        return wrapper
    return decorator


def async_timer(output: bool = True):
    """
    Timer decorator. Only for async functions.
    
    :param output: Should the time of completion be printed or only returned.
    :type output: :obj:`bool`
    
    :return: Time of completion.
    :rtype: :obj:`datetime.timedelta`
    
    """
    
    def decorator(f):
        @wraps(f)
        async def wrapper(*args, **kwargs) -> datetime.timedelta:
            time_start = datetime.datetime.now()
            result = await f(*args, **kwargs)
            time_end = datetime.datetime.now()
            duration = time_end - time_start
            
            if output:
                print(f"Function {f.__name__} took {duration}")
            
            return duration
        return wrapper
    return decorator