#import pygame
import math


knownfib = [0,1,1]

def fib(n):
    if n < len(knownfib):
        return knownfib[n]
    else:
        knownfib.append(fib(n-1)+fib(n-2))
        return fib(n-1) + fib(n-2)

φ = (1+math.sqrt(5))/2
ψ = 1-φ

def efib(n):
    return (φ**n - ψ**n)/(φ - ψ)




