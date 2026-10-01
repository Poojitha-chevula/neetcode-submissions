class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                n=board[i][j]
                if n in row[i]:
                    return False
                row[i].add(n)
                if n in col[j]:
                    return False
                col[j].add(n)
                b=(i//3)*3+(j//3)
                if n in box[b]:
                    return False
                box[b].add(n)
        return True