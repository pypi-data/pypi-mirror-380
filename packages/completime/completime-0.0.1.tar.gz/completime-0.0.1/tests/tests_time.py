import os
import pytest
import sys
import time
import contextlib
import io

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if path not in sys.path:
    sys.path.insert(0, path)
    
from completime.time import *

def test_sync():
    @timer(output=False)
    def _some_func():
        time.sleep(1)
        
    assert _some_func().seconds == 1

def test_sync_no_brackets():
    with pytest.raises(TypeError):
        @timer
        def _some_func():
            time.sleep(1)
        
        _some_func()

def test_output():
    @timer()
    def _some_func():
        time.sleep(1)
        
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        _some_func()
        console_output = buf.getvalue()
    assert console_output.startswith("Function")

@pytest.mark.asyncio
async def test_async():
    @async_timer(output=False)
    async def _some_func():
        time.sleep(1)
        
    result = await _some_func()
    assert result.seconds == 1