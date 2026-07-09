class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse = True)

        

        fleet = []
        
        for car in cars:
            time = (target - car[0]) / car[1] # (time = target - pos) / speed

            if len(fleet) == 0:
                fleet.append(time)
            elif time > fleet[-1]:
                fleet.append(time)
            else:
                continue
 
        return len(fleet)
