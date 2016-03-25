def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    return lambda x: f(x)

def two(f):
    return lambda x: f(f(x))
                                                                                                                                                                                                                                     
def increment(n):
    return n + 1

def mul(x,y):
    return x*y
"""def pow_church(m,n):
	return n(m)"""

def pow_church(m,n):
	return n(lambda x: mul_church(m,x))(one)

def pow_church(m,n):
	return n(m(successor))(zero)

"""def add_church(m, n):
	return n(successor)(m)"""

def mul_church(m,n):
	return n(lambda x: add_church(m,x))(zero)
"""def mul_church(m,n):
	return lambda f: n(m(f))"""

"""def powpow (n, m, f):
	return n(m(f))"""
