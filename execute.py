import time,functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kargs):
        start_time=time.time()
        result=fn(*args,**kargs)
        end_time=time.time()
        execute_time=end_time-start_time
        print('%s executed in %s ms'%(fn.__name__,execute_time*1000))
        return result
    return wrapper
@metric
def fast(x,y):
    time.sleep(0.0012)
    return x**y;
f=fast(234,12588)