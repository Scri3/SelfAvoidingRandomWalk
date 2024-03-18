
import random

print("\nPlease enter dimensions of the grid ")
r = int(input("\nEnter x: "))+1
c = int(input("\nEnter y: "))+1




L = [[False] * c for i in range(r)]

x , y = r // 2 , c // 2

print("\nx:",x,"   y:",y)
print("---------")  

while 0 < x < r-1 and 0 < y < c-1:
        
    if L[x+1][y] and L[x][y+1] and L[x-1][y] and L[x][y-1]:
        print("DEAD END! ")
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
    print("x:",x,"   y:",y)
    print("---------")       
    
if not (0 < x < r-1 and 0 < y < c-1):
    print("ESCAPE! ")
