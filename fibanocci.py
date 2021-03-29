# Find 40th number of fibanocci sequence
# Fibanocci problem 
def fib(n, dict ={}):
    if (n in dict):
        return dict[n]
    if(n<=2):
        return 1
    dict[n] = fib(n-1,dict)+fib(n-2,dict)
    return dict[n]

print(fib(6))
print(fib(40))
print(fib(500))

# Time Complexity : O(n)
# Space Complexity : O(n)