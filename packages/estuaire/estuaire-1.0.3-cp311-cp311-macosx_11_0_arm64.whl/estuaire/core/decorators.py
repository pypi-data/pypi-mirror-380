# Copyright (c) 2009 J-Pascal Mercier
#
#
# vim: ts=4 sw=4 sts=0 noexpandtab:
import logging
import os
import time

from functools import wraps

import numpy

logger = logging.getLogger(__name__)

class buggy(object):
    """
    This is a decorator which can be used to mark functions
    as not implemented. It will result in a warning being emitted when
    the function is called.
    """
    def __init__(self, date):
        self.date = date

    def __call__(self, fct):
        @wraps(fct)
        def wrapper(*args, **kwargs):
            logger.warning(
                "%s is buggy, use at your own risk. Expected fix : %s",
                fct.__name__,
                self.date,
            )
            try:
                return_value = fct(*args, **kwargs)
            except Exception:
                logger.exception("%s crashed: the function is marked buggy.", fct.__name__)
                raise
            return return_value
        return wrapper


class unimplemented(object):
    """
    This is a decorator which can be used to mark functions
    as not implemented. It will result in a warning being emitted and 
    the function is never called.
    """
    def __init__(self, date):
        self.date = date

    def __call__(self, fct):
        @wraps(fct)
        def wrapper(*args, **kwargs):
            logger.warning(
                "%s is not implemented; expected availability: %s",
                fct.__name__,
                self.date,
            )
        return wrapper


class broken(object):
    """
    This is a decorator which can be used to mark functions
    as broken. It will result in a warning being emitted and 
    the function is never called.
    """
    def __init__(self, date):
        self.date = date

    def __call__(self, fct):
        @wraps(fct)
        def wrapper(*args, **kwargs):
            logger.critical(
                "%s is broken -- DON'T USE IT. Expected fix : %s",
                fct.__name__,
                self.date,
            )
        return wrapper


def deprecated(fct):
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    """
    @wraps(fct)
    def wrapper(*args, **kwargs):
        logger.warning("Call to deprecated function %s.", fct.__name__)
        return fct(*args, **kwargs)
    return wrapper


def loggedcall(fct):
    """
    This is a decorator which log function call.
    """
    @wraps(fct)
    def wrapper(*args, **kwargs):
        logger.info(
            "Function -- %s--  called with arguments -- %s -- and keywords -- %s --",
            fct.__name__,
            args,
            kwargs,
        )
        return_value = fct(*args, **kwargs)
        logger.info("Function -- %s -- returned -- %s --", fct.__name__, return_value)
        return return_value
    return wrapper


def addmethod(instance):
    def decorator(fct):
        setattr(instance, fct.__name__, fct)
        return fct
    return decorator


class memoizehd(object):
    """
    This is a decorator wich is designed to cache to a file the 
    result of a function. This function calculate a hash from the
    function and the parameters and store the result in a designed
    file. ONLY WORK WITH SCIPY/NUMPY ARRAY AND WITH HASHABLE PARAMETERS
    """
    def __init__(self, basepath = '/tmp'):
        basepath = basepath[1:] if basepath.startswith('/') else basepath
        basepath = os.path.join("/tmp", basepath)
        try:
            os.stat(basepath)
        except OSError:
            os.mkdir(basepath)
        self.basepath = basepath
        logger.debug("memoizehd cache base path: %s", self.basepath)

    def __call__(self, fct):
        cachebase = os.path.join(self.basepath, str(hash(fct)) + "_" + str(os.getpid()))
        @wraps(fct)
        def wrapper(*args, **kwargs):
            cachefile = cachebase + ''.join(str(hash(arg)) for arg in args)
            cachefile += '_'.join(str(hash(kwargs[key])) for key in sorted(kwargs)) + ".npy"
            try:
                os.stat(cachefile)
                logger.info(
                    "Parameters hash matched calling -- %s --, reading cached return from file",
                    fct.__name__,
                )
                return_value = numpy.load(cachefile, allow_pickle=True)
            except OSError:
                return_value = fct(*args, **kwargs)
                numpy.save(cachefile, return_value, allow_pickle=True)
            return return_value
        return wrapper

def memoize(fct):
    """Cache the result of a function based on positional arguments."""

    return_dict = {}

    @wraps(fct)
    def wrapper(*args, **kwargs):
        if kwargs:
            key = (args, tuple(sorted(kwargs.items())))
        else:
            key = args
        if key not in return_dict:
            return_dict[key] = fct(*args, **kwargs)
        return return_dict[key]

    return wrapper


def timedcall(fct):
    @wraps(fct)
    def wrapper(*args, **kwargs):
        t = time.time()
        return_value = fct(*args, **kwargs)
        logger.info("Function -- %s -- called : TIME -- %.4f --", fct.__name__, time.time() - t)
        return return_value
    return wrapper
