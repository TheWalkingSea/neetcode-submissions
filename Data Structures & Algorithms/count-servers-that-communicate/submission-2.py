class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        columns = [0] * len(grid[0])
        rows = [0] * len(grid)

        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                item = grid[i][j]
                if (item):
                    columns[j] += 1
                    rows[i] += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] > 0 and (rows[i] > 1 or columns[j] > 1)):
                    total += 1

        return total