import cython
from libc.math cimport sqrt

def do_something(end: cython.int, s: cython.int=1):
    x1: cython.int = s
    x2: cython.int  = 1000 * 1000

    with nogil:
        while x1 < end:
            sqrt((x1 - x2) - (x1 - x2))
            x1 += 1


            
