def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# The return value of map is iterator, so we use list to construct it 

def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))
#filer whatever values to true

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))