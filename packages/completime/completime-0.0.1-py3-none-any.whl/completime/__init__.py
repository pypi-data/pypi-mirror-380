# completime - Powerful numbers conversion library
# Copyright (c) 2025 Treizd
#
# This file is part of numersys.
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the MIT License. See the LICENSE file for details.


from .time import timer, async_timer

__version__ = "0.0.1"
__all__ = ["timer", "async_timer"]

def __dir__():
    return ["timer", "async_timer", "__all__", "__builtins__", "__cached__", "__doc__", "__file__", "__loader__", "__name__", "__package__", "__path__", "__spec__", "__version__"]