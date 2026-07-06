public class Solution {
    public int EvalRPN(string[] tokens) {
        
        Stack<string> numbers = new Stack<string>();
        HashSet<string> operators = new HashSet<string> {"+", "-", "*", "/"};
        int result = 1;

        // Iterate through the array of tokens, if they are not an operator, add them to the numbers stack
        foreach (string val in tokens)
        {
            if (!operators.Contains(val))
                numbers.Push(val);
            // They are an operator, figure out witch one specifically using switch statements
            else if (numbers.Count >= 2)
            {
                int numberTwo = int.Parse(numbers.Pop());
                int numberOne = int.Parse(numbers.Pop());
                switch(val)
                {
                    case "+":
                        numbers.Push((numberOne + numberTwo).ToString());
                        break;

                    case "-":
                        numbers.Push((numberOne - numberTwo).ToString());
                        break;
                    
                    case "*":
                        numbers.Push((numberOne * numberTwo).ToString());
                        break;
                    
                    case "/":
                        numbers.Push((numberOne / numberTwo).ToString());
                        break;
                }
            }
        }

        // Once operator is figured out, only do the operations if the stack.Count is atleast 2, 

        // At the end stack will have one element in it so return that value as the result


        return int.Parse(numbers.Pop());

        
    }
}
