# Grid Traveller Problem
# Say that you are a traveller on a 2D grid. You begin in the top left corner and your goal is to travel to 
# bottom right corner. You may only move down or right. In how many ways can you travel to the goal on a
# grid with dimensions m*n? Write a gridTraveller function that calculate's this?

def gridTraveller(m,n,dict={}):
    key = str(m) + "," + str(n)
    if (key in dict):
        return dict[key]
    if m == 1 and n == 1 :
        return 1
    if m == 0 or n == 0 :
        return 0
    dict[key] = gridTraveller(m-1,n,dict) + gridTraveller(m,n-1,dict)
    return dict[key]

print(gridTraveller(2,3))
print(gridTraveller(3,3))
print(gridTraveller(18,18))

