#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ax = tuple_a[0] if len(tuple_a) >= 1 else 0
    ay = tuple_a[1] if len(tuple_a) >= 2 else 0
    bx = tuple_b[0] if len(tuple_b) >= 1 else 0
    by = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (ax + bx, ay + by)
