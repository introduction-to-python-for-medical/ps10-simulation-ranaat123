import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    up_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]
                if 2 in neighbors:
                    up_grid[i][j] = 2

    return up_grid

