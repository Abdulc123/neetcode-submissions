public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        
        // A car can't pass another car ahead of it, once it catches up to car in front of it, it will now have that same speed
        // Car fleet = non empty set of cars driving at the same position and same speed (traffic jam)
        // If car catches up to a fleet, the same moment fleet reaches the destination it becomes part of the fleet.
            // car can only catch up to another car if it is behind the fleet
        // Return number of different car fleets that will arrive at destination

        Stack<double> fleets = new Stack<double>();

        // Sort the positions array descendingly
        var combined = position.Zip(speed, (pos, spd) => (pos, spd)).ToList();
        combined.Sort((tup1, tup2) => tup2.pos.CompareTo(tup1.pos));
        position = combined.Select(x => x.pos).ToArray();
        speed = combined.Select(x => x.spd).ToArray();

        // Time it takes for a car to arrive is the (target - current position) / speed
        // Stack will contain the times, if the current time <= stack top, (it joins same fleet) don't add to the stack
        // Else when the top is greater than the stack top add it to the stack since it will be creating its own new fleet
        for (int i = 0; i < position.Length; i++)
        {
            double time = (double)(target - position[i]) / speed[i];
            Console.WriteLine($"Car {i} at position {position[i]} with speed {speed[i]}. Reaches destination in {time} seconds");
            
            if (fleets.Count == 0)
                fleets.Push(time);
            else if (time > fleets.Peek())
            {   
                fleets.Push(time);
            }   
        }

        return fleets.Count;
    }
}
