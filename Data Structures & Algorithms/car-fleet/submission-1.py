class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # time = (target - current_location) / speed
        # 1. If a car catches up to another car, they become a fleet and go at same speed
        # 2. single car counts when at least one car is included
        # 3. if a car and a different car reach the location at the same time 
        # they are part of a single fleet
        
        n = len(position)
        stack = []
        speed_list = []
        answer = 0

        # Combine the two lists together using zip
        car_data = list(zip(position,speed))
        car_data.sort(reverse=True)
        print(car_data)

        # Create a speed list
        for i in range(n):
            x, mph = car_data[i]
            speed_list.append((target - x) / float(mph))

        print(speed_list)

        # Determine the number of car fleets
        # [3.0, 3.0, 4.5, 2.0] #2 fleets 
        for i in range(n):
            if stack:
                # if car in front has same speed dont add to stack
                # if car in front is slower speed then dont add to stack
                # if car in front has faster speed, then add to stack
                if stack[-1] < speed_list[i]:
                    stack.append(speed_list[i])
            else:
                stack.append(speed_list[i])


        print(stack)
        return len(stack)