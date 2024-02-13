# Mazes problems like snake ans ladders, nxn workspaces etc.

# Q.1) in an nxn matrix return the number of ways to reach a point from a given point. 
# --> 
# X1,y1 are the starting points the processed strings in recursive call, x2,y2 are the final points the
# unprocessed strings of the recursive call.
# import sys

# sys.setrecursionlimit(10000) 

def Maze(x1,y1):
    if (x1 == 1 or y1 == 1):
        return 1
    else:
        
        right = Maze(x1-1, y1)
        down = Maze(x1, y1-1)
        return right + down


# print(Maze(3,3))

# Print the Path i.e RDDDR etc.
def Mazepath(x, y):
    def mazepath_helper(x, y, p):
        if x == 1 and y == 1:
            print(p)
            return
        else:
            if x > 1:
                pr = p + "R"
                mazepath_helper(x, y - 1, pr)
            if y > 1:
                pd = p + "D"
                mazepath_helper(x - 1, y, pd)

    mazepath_helper(x, y, "")

# Mazepath(3,3)
    
# Maze with obstacles. 

Maze = [['T', 'T', 'T'],    # The boolean maze .with False at the obstacle position.
        ['T', 'T', 'T'],
        ['T', 'F', 'T']] 

def Mazerestrictions(r,c, maze, p = ""):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        print(p)
        return
    
    if maze[r][c] == 'F':
        return
    
    if r < len(maze) - 1:
        pd = p + "D"
        Mazerestrictions(r+1, c, maze, pd)
    if c < len(maze[0]) - 1:
        pr = p + "R"
        Mazerestrictions(r, c + 1, maze, pr)

# Mazerestrictions(0,0,Maze)


# Maze with all the directions.
# Actual Backtracking algorithm.

Maze = [['T', 'T', 'T'],   
        ['T', 'T', 'T'],
        ['T', 'T', 'T']] 

def Mazeallpaths(r,c, maze, p = ""):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        print(p)
        return
    
    if maze[r][c] == 'F':
        return
    
    # Here i reach a current block. I'll mark it False i.e visited so as to Backtrack.
    maze[r][c] = 'F'

    if r < len(maze) - 1:
        pd = p + "D"
        Mazeallpaths(r+1, c, maze, pd)
    if c < len(maze[0]) - 1:
        pr = p + "R"
        Mazeallpaths(r, c + 1, maze, pr)
    if c > 0:
        pl = p + "L"
        Mazeallpaths(r, c-1, maze, pl)
    if r > 0:
        pu = p + "U"
        Mazeallpaths(r-1, c, maze, pu)
    
    # Backtrack to the point where i marked the cell false and removing the changes. i.e making it True.
    maze[r][c] = 'T'

Mazeallpaths(0,0, Maze)