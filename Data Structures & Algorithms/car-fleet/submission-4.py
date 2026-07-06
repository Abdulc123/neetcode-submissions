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

        # Combine the two lists together using zip
        car_data = list(zip(position,speed))
        car_data.sort(reverse=True)

        # Determine the number of car fleets
        for i in range(n):
            pos, mph = car_data[i]
            stack.append((target - pos) / mph)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                # if car in front has faster speed, then remove the car you just added
                # since the top of the stack, will just combine into a fleet with car in front of it
                stack.pop()

        return len(stack)