class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        def dfs(a, b):
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            grid[a][b] = " "
            for m1, m2 in dirs:
                newA = a + m1
                newB = b + m2
                if 0 <= newA < len(grid) and 0 <= newB < len(grid[0]) and grid[newA][newB] == "1":
                    dfs(newA, newB)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
