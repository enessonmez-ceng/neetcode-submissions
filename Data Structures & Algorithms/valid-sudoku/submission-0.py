class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # i will use three hashmap
        rows = defaultdict(set) # row index -> set
        cols = defaultdict(set) # col index -> set
        cells = defaultdict(set) # (cell_row,cell_col) -> set

        for i in range(len(board)):
            for j in range(len(board[0])):
                n = board[i][j]
                cell = (i//3,j//3)
                if  n != ".":
                    if n in rows[i] or n in cols[j] or n in cells[cell]:
                        return False
                    else:
                        rows[i].add(n)
                        cols[j].add(n)
                        cells[cell].add(n)
            
        return True