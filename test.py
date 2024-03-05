import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Randomized Depth-First Search Maze")

# Function to draw the grid
def draw_grid(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Function for depth-first search maze generation
def generate_maze(grid, current_cell):
    row, col = current_cell
    grid[row][col] = 1  # Mark the current cell as visited

    # Possible directions to move
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE and grid[new_row][new_col] == 0:
            # If the neighbor is not visited, carve a path and recursively visit it
            grid[row + dr // 2][col + dc // 2] = 1
            generate_maze(grid, (new_row, new_col))

# Create a grid with all walls
maze_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Start DFS maze generation from the top-left corner
generate_maze(maze_grid, (0, 0))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze grid
    screen.fill(BLACK)
    draw_grid(maze_grid)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
