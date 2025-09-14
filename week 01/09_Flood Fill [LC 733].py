class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        curr_color = image[sr][sc]

        if curr_color == color:
            return image

        def dfs( i, j):
            # checking boundary condition
            if i< 0 or j < 0 or i >= len(image) or j >= len(image[i]):
                return
            if image[i][j] != curr_color : 
                return 
            image[i][j] = color
            
            dfs(i-1, j) # top
            dfs(i, j+1) # right
            dfs(i+1, j) # down
            dfs(i, j-1) # left

        dfs(sr,sc)
        return image
