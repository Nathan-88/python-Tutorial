def my_logger(origin_func):
    import logging
    logging.basicConfig(filename="{}.log".format(origin_func.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args:{}, and kwargs: {}".format(args, kwargs))
        return origin_func(*args, **kwargs)
    return wrapper

@my_logger
def display_info(name, age):
    print("display_info ran with arguments ({} , {})".format(name, age))

display_info("john", 12)

"""
This is a python code that implements a decorator named my_logger that can be used to log information about a function.

A decorator is a wrapper function that adds or modifies the behavior of an existing function. The decorator my_logger adds logging functionality to the function it decorates.

Here, my_logger takes a function origin_func as an argument, sets up basic logging using the logging module and returns a new function wrapper.

The wrapper function logs the arguments passed to the decorated function origin_func using the logging.info() method. It then calls origin_func with the same arguments and returns its result.

The display_info function is decorated with my_logger by using the @my_logger syntax. When display_info is called, it will log information about its arguments in a file named display_info.log.

For example, in a real world project, you could use this decorator to log information about function calls to help you track the behavior of your code and debug issues.

For instance, if you have a function that performs some important computation, you can use the my_logger decorator to log information about the arguments passed to the function and the result it returns. This can help you understand how the function behaves under different conditions.
"""      