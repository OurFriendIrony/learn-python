#!/usr/bin/env python

def just(t):
    return str(t).ljust(20)

def printType(t):
    print("%s is of %s" % (just(t), type(t)) )

printType(False)
printType(1)
printType(1.0)
printType(1L)
printType("hello world")
printType([1,2,3])
printType(("one","two"))
printType({"Key":"Value"})

