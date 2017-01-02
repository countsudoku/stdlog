# stdlog

A class to redirect sdout to a logging Logger.

## How to use stdlog

You can use stdlog in two ways:

* as a decorator for a function


```python
@stdlog(logging.Logger, loglevel)
def function(*args, **kwargs):
```

* as a drop in replacement for stdout

```python
sys.stdout = stdlog(logging.Logger, loglevel)
```
