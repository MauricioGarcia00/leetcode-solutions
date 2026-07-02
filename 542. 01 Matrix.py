# Mauricio Garcia
# This was my first medium-level matrix problem and also one of my first applications of Breadth-First Search (BFS).
# I found it challenging because I had to carefully visualize how the queue propagated distances throughout the matrix.
# Breaking the algorithm down step by step and mapping out the traversal on paper helped me understand why BFS naturally computes the shortest distance to each cell.
# This problem gave me a much better intuition for grid traversal and BFS.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #mat = [
        #       [0,0,0],
        #       [0,1,0],
        #       [0,0,0]]
        if not mat:
            return mat
        
        rows = len(mat)
        columns = len(mat[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        infMatrix = [[float('inf') for _ in range(columns)] for _ in range(rows)]
        queue = deque()

        for i in range(rows):
            for j in range(rows):
                if mat[i][j] == 0:
                    infMatrix[i][j] = 0
                    queue.append((i,j))

        while queue:
            x, y = queue.popleft()
            for dx,dy in directions:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < rows and 0 <= ny < columns: # Checking if we are inside matrix
                    if infMatrix[nx][ny] > infMatrix[x][y] + 1:
                        infMatrix[nx][ny] = infMatrix[x][y] + 1
                        queue.append((nx,ny))
        return infMatrix




        
