from tkinter import *
from Logica import *
from functools import *
import time

def hi (a, b):
	return a * b

def hello (a, b):
	return hi(a, b + 1)

hello(2, 2)

print(hello(2,2))