# Write code for algorithm 3 below
def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1)+fib(n-2))

n = 6
for i in range(n):
    print(fib(i))