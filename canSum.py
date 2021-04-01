# canSum Problem
# Write a function canSum(targetSum,numbers) that takes in a targetSum and an array of numbers as arguments. The   function should return a boolean indicating whether or not it's possible to generate the targetSum using numbers from the array. You may use an element of the array as many as times as needed. You may assume that all input numbers are non-negative. 

def canSum(targetSum,numbers,dict = {}):
    if(targetSum in dict):
        return dict[targetSum]
    if(targetSum is 0):
        return True
    if (targetSum<0):
        return False
    for num in numbers:
        remainder = targetSum - num
        print(remainder)
        if(canSum(remainder,numbers,dict)==True):
            dict[targetSum] = True
            return True
    dict[targetSum] = False
    return False

print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(300,[7,14]))
