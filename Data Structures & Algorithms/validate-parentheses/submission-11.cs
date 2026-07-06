public class Solution {
    public bool IsValid(string s) {

        // Store in a stack since most recent closing parantheses should have its matching open one stored in stack
        // Valid if the stack is empty at the end, since alll of them found a match

        Stack<char> stack = new Stack<char>();
        Dictionary<char, char> complement = new Dictionary<char, char> 
        {
            {')' , '('}, 
            {'}' , '{'}, 
            {']' , '['}
        };

        foreach (char bracket in s)
        {
            PrintStack(stack);

            if (complement.ContainsValue(bracket)) // Open Bracket
                stack.Push(bracket);
            else // Closed bracket
            {
                if (stack.Count != 0 && stack.Peek() == complement[bracket]) // If the top of the stack is the open bracket, when a closing one is seen
                    stack.Pop();
                else
                    return false;
            }
        }

        void PrintStack(Stack<char> stack)
        {
            stack.ToList().ForEach(bracket => Console.Write($"{bracket}"));
            Console.WriteLine();
        }

        return stack.Count == 0;
        
    }
}
