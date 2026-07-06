public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {

        // Row: Sorted in increasing order
        // First integer of every row is larger than the last integer of the previous row

        // Use the first number in each row to calc which row to explore via binary search


        (int rowLocation, int targetIndex) = MatrixBinarySearch(matrix, target);
        bool result = (targetIndex != -1) ? true : false;
        Console.WriteLine($"Target: {target} is located in Row:[{rowLocation}] At Index:[{targetIndex}]");

        return result;

        (int, int) MatrixBinarySearch(int[][] matrix, int target)
        {
            int l = 0;
            int r = matrix.Length - 1;

            while (l <= r)
            {
                int mid  = (l + r) / 2;
                int[] row = matrix[mid];
                int lastIndex = row.Length - 1;

                if (row[0] < target && target > row[lastIndex])
                    l = mid + 1;
                else if (row[0] > target)
                    r = mid - 1;
                else
                    return (mid, BinarySearch(row, target));
            }   

            return (-1, -1);

        }

        int BinarySearch(int[] row, int target)
        {
            int l = 0;
            int r = row.Length - 1;

            while (l <= r)
            {
                int mid = (l + r) / 2;
                
                if (row[mid] < target)
                    l = mid + 1;
                else if (row[mid] > target)
                    r = mid - 1;
                else
                    return mid;
            }

            return -1;
        }
        
    }
}
