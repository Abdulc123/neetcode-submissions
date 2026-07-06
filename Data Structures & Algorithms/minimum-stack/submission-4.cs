public class MinStack
{
    private List<int> stack {get; set;}
    private Stack<int> minStack {get; set;} // Min will always be at the top

    public MinStack()
    {
        // Use a List Structure, append to the end, and pop from the end
        stack = new List<int>();
        minStack = new Stack<int>();
    }
    
    public void Push(int val) 
    {
        stack.Add(val);
        if (minStack.Count ==  0)
            minStack.Push(val);
        else if (val <= minStack.Peek())
            minStack.Push(val);
    }
    
    public void Pop() 
    {
        if (stack.Count != 0)
        {
            if (minStack.Peek() == Top())
                minStack.Pop();
            stack.RemoveAt(stack.Count - 1);
        }
    }
    
    public int Top()
    {
        return stack[stack.Count - 1];
    }
    
    public int GetMin()
    {
        // Need to keep track of the min index as we go along, so we can always just return the index its at
        return minStack.Peek();
    }
}
