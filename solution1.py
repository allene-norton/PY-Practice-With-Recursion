# Write code for algorithm 1 below
def countdown(n):
    if n>0:
        print(n)
        countdown(n-1)
n=8
countdown(n)