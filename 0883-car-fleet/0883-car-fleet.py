class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_list = []
        car_fleet_stack = []

        for i in range(len(position)):
            car_list.append((position[i], speed[i]))

        car_list.sort(reverse = True)

        for pos, sp in car_list:
            time_taken = (target - pos) / sp
            if not car_fleet_stack:
                car_fleet_stack.append(time_taken)
            else:
                if time_taken > car_fleet_stack[-1]:
                    car_fleet_stack.append(time_taken)

        return len(car_fleet_stack)