import math
class house:
    def find_total_area(*args):
        total_area = 0
        for room in args:
            name,length,width = room
            area = length*width
            total_area = total_area + area
        return total_area
    def circle(radius):
        return 2*math.pi*radius
print(house.circle(10))
room1 = ('Living Room',10,12)
room2 = ('Dining Room',20,21)
room3 = ('Master bed room',20,10)
print(house.find_total_area(room1,room2,room3))