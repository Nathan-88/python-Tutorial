class decorator_class:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwds):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwds) 

@decorator_class
def display():
    print('display function ran')

@decorator_class
def display_info(name, age):
    print("my name is {} and age is {}".format(name, age))

display_info('john', 12)
display()