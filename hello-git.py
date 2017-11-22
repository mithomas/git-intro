print("Hello git!")

def sum(n):
    sum = 0
    for i in xrange(n):
        if i%5 or i%3:
            sum += i

def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)

print (sum(1000))
print (fib(0))
print (fib(1))
print (fib(10))
print (fib(30))
