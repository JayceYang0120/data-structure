import numpy as np

maze = [[0,1,1,1,1,1,1],
        [0,0,0,0,0,0,1],
        [1,0,1,0,1,0,0],
        [0,0,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,0,1,0,0],
        [1,0,1,1,1,1,0]]

'''maze = [[0,1,1,1,1,1],
        [0,0,0,0,0,0],
        [1,0,1,0,1,0],
        [0,0,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,1,1,0,0]]'''
        
def goRight(location, limitOfMaze):
     if(location[1] == limitOfMaze):
         return False
     else:
         nextLocation = [location[0], location[1] + 1]
         if nextLocation in passRoute:
             return False       
         elif maze[nextLocation[0]][nextLocation[1]] == 1:
             return False
         else:
             correctRoute.append(nextLocation)
             passRoute.append(nextLocation)
             return True
         
def goLeft(location, limitOfMaze):
     if(location[1] == 0):
         return False
     else:
         nextLocation = [location[0], location[1] - 1]
         if nextLocation in passRoute:
             return False       
         elif maze[nextLocation[0]][nextLocation[1]] == 1:
             return False
         else:
             correctRoute.append(nextLocation)
             passRoute.append(nextLocation)
             return True
         
def goDown(location, limitOfMaze):
     if(location[0] == limitOfMaze):
         return False
     else:
         nextLocation = [location[0] + 1, location[1]]
         if nextLocation in passRoute:
             return False       
         elif maze[nextLocation[0]][nextLocation[1]] == 1:
             return False
         else:
             correctRoute.append(nextLocation)
             passRoute.append(nextLocation)
             return True      

def goUp(location, limitOfMaze):
     if(location[0]== 0):
         return False
     else:
         nextLocation = [location[0] - 1, location[1]]
         if nextLocation in passRoute:
             return False
         elif maze[nextLocation[0]][nextLocation[1]] == 1:
             return False
         else:
             correctRoute.append(nextLocation)
             passRoute.append(nextLocation)
             return True
            
correctRoute = [[0, 0]]
passRoute = [[0, 0]]
location = [0, 0]
limitOfMaze = len(maze) - 1

while correctRoute[len(correctRoute) - 1] != [limitOfMaze, limitOfMaze]:
    if goRight(location, limitOfMaze):
        location = correctRoute[len(correctRoute) - 1]
        continue
     
    if goLeft(location, limitOfMaze):
        location = correctRoute[len(correctRoute) - 1]
        continue
     
    if goDown(location, limitOfMaze):
        location = correctRoute[len(correctRoute) - 1]
        continue
     
    if goUp(location, limitOfMaze):
        location = correctRoute[len(correctRoute) - 1]
        continue
    
    correctRoute.pop()
    location = correctRoute[len(correctRoute) - 1]
    
print("Maze:")
print(np.array(maze))

print("Passroute: ")
print(passRoute)
i = 0
while i < len(passRoute):
    maze[passRoute[i][0]][passRoute[i][1]] = 3
    i = i + 1
print(np.array(maze))

print("最短路線: ")
for i in range(len(correctRoute)):
    print("第",i,"步:",correctRoute[i])
    
correctRoute.reverse()
print("終點到起點: ")
for i in range(len(correctRoute)):
    print("第",i,"步:",correctRoute[i])
