class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Determine if the rows have duplicates so the nested list
        # Determine if the cols have duplciates so for each i in each nested list
        # Ensure each square itself doesn't have duplicated numbers

        # Frequency dicst for each of the options
        row_freq: dict[int, set()] = defaultdict(set)
        col_freq: dict[int, set()] = defaultdict(set)
        grid_freq: dict[int, set()] = defaultdict(set)

        for i in range(9):
            row = board[i]

            # Iterate over each column in row
            for j, entry in enumerate(row):
                if entry == ".":
                    continue
                
                # Add it to row freq
                if (entry in row_freq[i]
                    or entry in col_freq[j]
                    or entry in grid_freq[(i // 3), (j // 3)]):
                    return False

                row_freq[i].add(entry)
                col_freq[j].add(entry)
                grid_freq[(i // 3, j // 3)].add(entry)


        return True
                    

            


