import pygame
import sys

# Rendering Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10  
FPS = 2        

COLOR_BG = (10, 10, 15)        
COLOR_GRID = (40, 40, 50)    
COLOR_DIE = (180, 50, 50)     
COLOR_ALIVE = (0, 255, 150)    

# Grid Size
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE


def count_neighbors(grid, r, c):
    """Counts the 8 living neighbors around a given cell (r, c)"""
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            neighbor_r = (r + i) % ROWS
            neighbor_c = (c + j) % COLS
            count += grid[neighbor_r][neighbor_c]
    return count


def update_grid(grid):
    """Apply Conways rules to generate the next state of the grid."""
    next_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]     # blank state
    
    for r in range(ROWS):
        for c in range(COLS):
            neighbors = count_neighbors(grid, r, c)
            
            if grid[r][c] == 1:
                # Rule 1 & 3: Underpopulation / Overpopulation dies
                # Rule 2: Lives on to next generation
                if neighbors in [2, 3]:
                    next_grid[r][c] = 1
            else:
                # Rule 4: Reproduction
                if neighbors == 3:
                    next_grid[r][c] = 1
                    
    return next_grid


def draw_grid(screen, grid):
    """Draws the current state of the cells."""
    screen.fill(COLOR_BG)
    
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                # Draw living cell
                pygame.draw.rect(
                    screen, 
                    COLOR_ALIVE, 
                    (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
                )
            else:
                pygame.draw.rect(
                    screen, 
                    COLOR_GRID, 
                    (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 
                    1
                )


def main():
    pygame.init()
    screen = pygame.display.set_subplots()[0] if hasattr(pygame, 'set_subplots') else pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life (Space to Pause, Click to Draw)")
    clock = pygame.time.Clock()

    # Initial state
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    
    paused = True  
    drawing = False
    erasing = False

    while True:
        clock.tick(FPS)
        
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    pygame.display.set_caption(
                        "Conway's Game of Life" + (" (PAUSED)" if paused else " (RUNNING)")
                    )
                elif event.key == pygame.K_c:
                    # Clear the grid
                    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
                    paused = True
                    pygame.display.set_caption("Conway's Game of Life (PAUSED)")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    drawing = True
                elif event.button == 3:  
                    erasing = True
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                elif event.button == 3:
                    erasing = False

        if drawing or erasing:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            c = mouse_x // CELL_SIZE
            r = mouse_y // CELL_SIZE
            if 0 <= r < ROWS and 0 <= c < COLS:
                grid[r][c] = 1 if drawing else 0

        # Logic Update
        if not paused:
            grid = update_grid(grid)

        # Render 
        draw_grid(screen, grid)
        pygame.display.flip()


if __name__ == "__main__":
    main()