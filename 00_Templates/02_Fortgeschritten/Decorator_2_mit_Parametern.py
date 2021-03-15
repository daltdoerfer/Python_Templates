# https://www.youtube.com/watch?v=09ip47kGvn4&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=8

def repeat_decorator(x): # Funktion soll x-Mal ausgeführt werden
    def decorator(func):
        def decorate(*args, **kwargs):
            for i in range(x):
                func(*args, **kwargs) # Aufruf der main loop Funktion
        return decorate
    return decorator

@repeat_decorator(5)
def print_that(a):
    print(a)

print_that('Hallo Welt')