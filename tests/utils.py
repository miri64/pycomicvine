import logging
import ssl
import urllib2

TRIES=3

class TimeoutError(Exception):
    pass

def test_3times_then_fail(func, *args, **kwargs):
    log = logging.getLogger("tests")
    for i in range(TRIES):
        try:
            return func(*args, **kwargs)
        except urllib2.HTTPError, e:
            if e.code == 500:
                log.debug("Internal server error (try=%d)" % i)
                if i == TRIES-1:
                    raise TimeoutError('To many HTTP-Errors')
        except ssl.SSLError, e:
            print e.__dict__
            if e.msg == "The read operation timed out":
                log.debug("Timeout error (try=%d)" % i)
                if i == TRIES-1:
                    raise TimeoutError('To many HTTP-Timeouts')
