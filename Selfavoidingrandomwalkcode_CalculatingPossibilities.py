
import random

r = int(input("Enter x: "))+1
c = int(input("Enter y: "))+1
t = int(input("How many times do you want the test to run?? "))

dead_ends = 0


for i in range(t): 

    L = [[False] * c for i in range(r)]

    x , y = r // 2 , c // 2

    while 0 < x < r-1 and 0 < y < c-1:
        
        if L[x+1][y] and L[x][y+1] and L[x-1][y] and L[x][y-1]:
            dead_ends+=1
            break

        L[x][y] = True
        a = random.random()
        if a <= 0.25 and not L[x+1][y]:
            x +=1
        elif a <= 0.5 and not L[x][y+1]:
            y+=1
        elif a <= 0.75 and not L[x-1][y]:
            x-=1
        elif a <= 1 and not L[x][y-1]:
            y-=1
        
    

res = (dead_ends/t)*100
print ("Possibility for Dead Ends:",res,"%")






