#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import logging
import sys

class stdlog(object):
    """ A class, which can be used as decorator or as replacement for
    sys.stdout. It redirects stdout to a logging instance

    Args:
    ====
        logger: a logging.Logger instance
            the logger to wich stdout gets redirected
        loglevel: loglevel
            set the logging loglevel

    Returns:
    ====
        the decorated function when called
    """

    def __init__(self, logger=None, loglevel='INFO'):
        if not logger:
            logger = logging

        if loglevel.lower() == 'critical':
            self.log_func = logger.critical
        elif loglevel.lower() == 'error':
            self.log_func = logger.error
        elif loglevel.lower() == 'warning':
            self.log_func = logger.warning
        elif loglevel.lower() == 'info':
            self.log_func = logger.info
        elif loglevel.lower() == 'debug':
            self.log_func = logger.debug
        else:
            raise TypeError('Loglevel {0} unknown!'.format(loglevel))

    def __call__(self, f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            stdout = sys.stdout
            sys.stdout = self
            f(*args, **kwargs)
            sys.stdout = stdout
        return wrapped

    def write(self, data):
        """ imitates the stdout write function, but writes to the log_func if
        the string is not empty or a newline """
        if data not in ['', '\n']:
            self.log_func(data.rstrip())

    def flush(self):
        """ imitates the stdout flush function, but isn't needed here"""
        pass
