# usage:
#     with switch(element) as case:
#         if case('asdf'):
#             do stuff
#         elif case([1, 2, 3]):
#             do other stuff
#         else:
#             default
# source:
#     https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python

class Switch:
    '''Provide switch statement in python'''
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return False # Allows a traceback to occur

    def __call__(self, *values):
        return self.value in values
