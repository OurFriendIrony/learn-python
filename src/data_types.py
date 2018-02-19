#!/usr/bin/env python


def just(t):
    return str(t).ljust(20)


def print_type(t):
    print("%s is of %s" % (just(t), type(t)))


print_type(False)
print_type(1)
print_type(1.0)
# longs are redunant in python3
print_type("hello world")
print_type([1, 2, 3])
print_type(("one", "two"))
print_type({"Key": "Value"})
