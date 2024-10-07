import random
from collections import deque
import tkinter as tk

CELL_SIZE = 20

def initialize_maze(width, height):
    maze = [['#'] * (width * 2 + 1) for _ in range(height * 2 + 1)]
    for i in range(height):
        for j in range(width):
            maze[i * 2 + 1][j * 2 + 1] = ' '
    return maze

def generate_maze_dfs(maze, width, height):
    stack = []
    visited = [[False] * width for _ in range(height)]
    stack.append((0, 0))
    visited[0][0] = True
    
    while stack:
        x, y = stack[-1]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        found_neighbor = False
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
                maze[y * 2 + 1 + dy][x * 2 + 1 + dx] = ' '
                visited[ny][nx] = True
                stack.append((nx, ny))
                found_neighbor = True
                break
                
        if not found_neighbor:
            stack.pop()

def solve_maze_bfs(maze, width, height):
    start = (1, 1)
    goal = (height * 2 - 1, width * 2 - 1)
    queue = deque([start])
    parent = {start: None}
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if maze[ny][nx] == ' ' and (nx, ny) not in parent:
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    
    path = []
    current = goal
    while current:
        path.append(current)
        current = parent[current]
    
    for x, y in path:
        maze[y][x] = '*'

def draw_maze(maze, width, height):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=(width * 2 + 1) * CELL_SIZE, height=(height * 2 + 1) * CELL_SIZE)
    canvas.pack()

    for y in range(height * 2 + 1):
        for x in range(width * 2 + 1):
            color = "black" if maze[y][x] == '#' else "white"
            if maze[y][x] == '*':
                color = "red"
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, 
                                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, 
                                    fill=color)

    root.mainloop()

def main_gui(width, height):
    maze = initialize_maze(width, height)
    generate_maze_dfs(maze, width, height)
    solve_maze_bfs(maze, width, height)
    draw_maze(maze, width, height)

if __name__ == "__main__":
    width = 10
    height = 10
    main_gui(width, height)
