from optparse import Option
import pygame
import time
import random
from disjoint_set import DisjointSet
from collections import deque

# set up pygame window
WIDTH = 500
HEIGHT = 600
FPS = 80

# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)

# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 20                   # width of cell
grid = []
visited = []
stack = []
solution = {}

def find_edges():
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    edges = set()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            for d in range(4):
                if (x + dx[d], y + dy[d]):
                    x1 = x * HEIGHT + y
                    x2 = (x + dx[d]) *HEIGHT + (y + dy[d])
                if x1 < x2:
                    x1, x2 = x2, x1
                    edges.add((x1, x2))
    return edges

# build the grid
def build_grid(x, y, w):
    for i in range(1,21):
        x = 20                                                            # set x coordinate to start position
        y = y + 20                                                        # start a new row
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           # left of cell
            grid.append((x,y))                                            # add cell to grid list
            x = x + 20                                                    # move cell to new position


def push_up(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1, 19, 39), 0)         # draw a rectangle twice the width of the cell
    pygame.display.update()                                              # to animate the wall being removed


def push_down(x, y):
    pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 19, 39), 0)           # draw a rectangle twice the width of the cell
    pygame.display.update()                                              # to animate the wall being removed


def push_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 39, 19), 0)          # draw a rectangle twice the width of the cell   
    pygame.display.update()                                              # to animate the wall being removed


def push_right(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 39, 19), 0)             # draw a rectangle twice the width of the cell 
    pygame.display.update()                                             # to animate the wall being removed


def single_cell( x, y):
    pygame.draw.rect(screen, GREEN, (x +1, y +1, 18, 18), 0)          # draw a single width cell
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 18, 18), 0)        # used to re-colour the path after single_cell
    pygame.display.update()                                        # has visited cell


def solution_cell(x,y):
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)             # used to show the solution
    pygame.display.update()                                        # has visited cell


def carve_out_maze(x,y):
    single_cell(x, y)                                              # starting positing of maze
    stack.append((x,y))                                            # place starting cell into stack
    visited.append((x,y))                                          # add starting cell to visited list
    while len(stack) > 0:                                          # loop until stack is empty
        time.sleep(.07)                                            # slow program now a bit
        cell = []                                                  # define cell list
        if (x + w, y) not in visited and (x + w, y) in grid:       # right cell available?
            cell.append("right")                                   # if yes add to cell list

        if (x - w, y) not in visited and (x - w, y) in grid:       # left cell available?
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     # down cell available?
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:      # up cell available?
            cell.append("up")

        if len(cell) > 0:                                          # check to see if cell list is empty
            cell_chosen = (random.choice(cell))                    # select one of the cell randomly

            if cell_chosen == "right":                             # if this cell has been chosen
                push_right(x, y)                                   # call push_right function
                solution[(x + w, y)] = x, y                        # solution = dictionary key = new cell, other = current cell
                x = x + w                                          # make this cell the current cell
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))                                # place current cell on to stack

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            single_cell(x, y)                                     # use single_cell function to show backtracking image
            time.sleep(.05)                                       # slow program down a bit
            backtracking_cell(x, y)                               # change colour to green to identify backtracking path


def plot_route_back(x,y):
    solution_cell(x, y)                                          # solution list contains all the coordinates to route back to start
    while (x, y) != (20,20):                                     # loop until cell position == start position
        x, y = solution[x, y]                                    # "key value" now becomes the new key
        solution_cell(x, y)                                      # animate route back
        time.sleep(.1)


x, y = 20, 20                     # starting position of grid
build_grid(40, 0, 20)             # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
carve_out_maze(x,y)               # call build the maze  function
plot_route_back(400, 400)         # call the plot solution function

def solver(self, s, e, option):
        """Solve the maze"""
        frontier = deque()  # front search
        frontier.append(s)
        visited = set()  # visited nodes
        visited.add(s)
        prev = {s: None}  # for each node the previus one
        while frontier:  # while front search is not empty
            if option == "bfs":
                current_node = frontier.popleft()
            for next_node in self.adjacency_map[current_node]:
                if not next_node in visited:  # if next node isn't in visited nodes
                    frontier.append(next_node)
                    visited.add(next_node)
                    prev[next_node] = current_node

        # create the path from e to s
        path = []
        at = e
        while at != None:
            path.append(at)
            at = prev[at]

        # reverse the path to create the final path that we want
        path = path[::-1]

        # if s and e are connected return path
        if path[0] == s:
            return path

        # else return an empty list
        return []
def __init__(
self
):
    if __name__ == "__main__":
        carve = carve_out_maze(x,y)
        edges = find_edges()   
        ds = DisjointSet()
        for i in range(x * y):
            ds.find(i)
    # ##### pygame loop #######
        running = True
        while running:
        # keep running at the at the right speed
            clock.tick(FPS)
        # process input (events)
            for event in pygame.event.get():
            # check for closing the window
                if event.type == pygame.QUIT:
                    running = False
        
    if len(list(ds.itersets())) == 1:
        solver(self, x, y, Option)
        pygame.screen(carve)
        pygame.time.delay(3000)
        

        e = random.sample(edges, 1)
        edges.remove((e[0][0], e[0][1]))
        u = ds.find(e[0][0])
        v = ds.find(e[0][1])
        if not ds.connected(u, v):
            stack.append((e[0][0], e[0][1]))
    ds.union(u, v)
    screen(carve, e[0][0], e[0][1])
    build_grid(carve)
