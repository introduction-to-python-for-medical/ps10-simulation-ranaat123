import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    up_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                if (i>0 and [grid[i-1][j]==2) or (i<(grid_size-1) and [grid[i+1][j]==2) or (j>0 and [grid[i][j-1]==2) or (j<(grid_size-1) and [grid[i][j+1]==2):
                    up_grid[i][j] = 2

    return up_grid
