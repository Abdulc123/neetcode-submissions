public class TimeMap {

    Dictionary<string, List<string[]>> Times;

    public TimeMap() {
        Times = new Dictionary<string, List<string[]>>();
    }
    
    public void Set(string key, string value, int timestamp) {
        // Stores the key with the value at the given timestamp
        if (!Times.ContainsKey(key))
            Times.Add(key, new List<string[]>());

        Times[key].Add(new string[] {timestamp.ToString(), value});
    }
    
    public string Get(string key, int timestamp) {
        // Returns most recent value of key if the set was previously called on it 
        // AND most recent timestamp for that key (prev_timestamp) <= given timestamp
        // if no values return ""
        if (Times.ContainsKey(key))
        {
            if (Times[key][0][0] == timestamp.ToString())
                return Times[key][0][1];
            else 
            {
                // Binary Search to find the index of the target time stamp so previous = target - 1
                int targetTimeStampIndex = BinarySearch(0, Times[key].Count - 1, timestamp, Times[key]);
                
                if (targetTimeStampIndex == -1)
                    return "";
                
                return Times[key][targetTimeStampIndex][1]; // Return the previous time stamp
            }
        }


        return ""; // Not found
    }
    
    public int BinarySearch(int l, int r, int targetTimeStamp, List<string[]> values)
    {
        while (l <= r)
        {
            int mid = (l + r) / 2;
            if (int.TryParse(values[mid][0], out int currentTimeStamp))
            {
                if (currentTimeStamp < targetTimeStamp)
                    l = mid + 1;
                else if (currentTimeStamp > targetTimeStamp)
                    r = mid -1;
                else
                {
                    // We currently found the target index, return that so its previous timestamp can be found
                    return mid;
                }
            }   
        }
        return r; // When a previous time is not found just return the most previous one which is to the right of m aka r
    }
}
