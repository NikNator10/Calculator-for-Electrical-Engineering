import os

def addieren(*args):
  sum = 0
  for x in args:
    sum = sum + x
  return sum

def subtrahieren(*args):
  dif = 0
  for x in args:
    dif = dif - x
  return dif

def multiplizieren(*args):
  prod = 0
  for x in args:
    prod = prod * x
  return prod

def dividieren(*args):
  quo = 0
  for x in args:
    quo = quo / x
  return quo
  
