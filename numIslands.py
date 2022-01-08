class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Time | Space: O()
        count islands 

        1. loop through grid 
            - dfs when grid[r][c] == '1' & increment count
        2. dfs: 
            - transform current cell grid[i][j] = 0 
            - offsets array 
            - loop through offsets array and make dr, dc 
                - dr, dc = i+offsets[0], j+offsets[1]
                - if out of bounds continue
                - dfs if grid[dr][dc] == 1
        '''
        def dfs(i, j): 
            
            grid[i][j] = '0' 
            
            offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            
            for offset in offsets: 
                dr, dc = i+offset[0], j+offset[1]
                if dr<0 or dc<0 or dr>=len(grid) or dc>=len(grid[0]): continue
                if grid[dr][dc] == '0': continue 
                dfs(dr, dc)

        numOfIslands=0
        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == '1': 
                    numOfIslands += 1
                    dfs(row, col) # transforms all connected '1' -> '0'
                    
        return numOfIslands
