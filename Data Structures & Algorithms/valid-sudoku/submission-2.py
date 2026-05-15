class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        # init hash maps
        for i in range(9):
            cols[i] = []
            rows[i] = []
            squares[i] = []
        
        for y in range(9):
            for x in range(9):
                value = board[y][x]
                if value == '.':
                    continue
                
                index = (x // 3) * 3 + (y // 3) # hash map for index of each square

                # duplicate check:
                if value in cols[x] or value in rows[y] or value in squares[index]:
                    return False

                # else, add value and carry on:
                cols[x].append(value)
                rows[y].append(value)
                squares[index].append(value)
        return True


        