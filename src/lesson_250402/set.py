a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a) # {1, 2, 3, 4, 5, 6}
print(type(a)) # <class 'set'>
b = {2, 3, 3, 6, 7}
print(b) # {2, 3, 6, 7}
print(a - b) # {1, 4, 5}
print(b - a) # {7}
print(a & b) # {2, 3, 6}
print(a | b) # {1, 2, 3, 4, 5, 6, 7}
print(a ^ b) # {1, 4, 5, 7}