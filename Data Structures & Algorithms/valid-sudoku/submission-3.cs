public class Solution {
    public bool IsValidSudoku(char[][] board) {

        void PrintBoard(){
            foreach (var row in board)
            {
                foreach (char tile in row)
                {
                    Console.Write($"{tile} ");
                }
                Console.WriteLine();
            }
            Console.WriteLine();
        }

        PrintBoard();

        HashSet<char> rowSet;
        Dictionary<int, HashSet<char>> columns = new Dictionary<int, HashSet<char>>(); // row : Column rowSet
        Dictionary<int, HashSet<char>> subBoxes = new Dictionary<int, HashSet<char>>();
        int size = board.Length;
        char tile;

        for (int row = 0; row < size; row++)
        {
            rowSet = new HashSet<char>();

            for (int col = 0; col < size; col++) {
                tile = board[row][col];
                // Row Validation
                if (tile != '.')
                {
                    if (rowSet.Contains(tile))
                        return false;
                    else
                        rowSet.Add(tile);

                    // Populating column Dictionary if row has not been seen yet
                    if (!columns.ContainsKey(col))
                        columns.Add(col, new HashSet<char>());
                    
                    // Column Validation
                    if (columns[col].Contains(tile))
                        return false;
                    else
                        columns[col].Add(tile);


                    int tileIndex = (row / 3) * 3 + (col / 3);
                    // Populating the SubBoxes Dictionary with entries
                    if (!subBoxes.ContainsKey(tileIndex)) 
                        subBoxes.Add(tileIndex, new HashSet<char>());
                    
                    // SubBox Validation
                    if (subBoxes[tileIndex].Contains(tile))
                        return false;
                    else
                        subBoxes[tileIndex].Add(tile);

                }
                
            }

            Console.WriteLine();

        }
        

        return true;
    }
}
