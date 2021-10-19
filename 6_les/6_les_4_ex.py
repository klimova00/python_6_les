class Car:
    is_police = False
    sport_car = False

    def __init__(self, name, color, speed):
        self.speed = speed
        self.color = color
        self.name = name
        print(f'My_car: {self.name} color: {self.color}, police - {self.is_police}')

    def go(self, speed):
        self.speed = speed
        print(f"My car went at a speed: {self.speed} ")

    def stop(self):
        self.speed == 0
        print(f'My car {self.name} stop')

    def turn(self, direction):
        if self.speed != 0:
            if direction == 0:
                print(f'My car turn right')
            else:
                print(f'My car turn left')
        else:
            print(f"\033[1;31m My car is standing Can't turn\033[0m")

    def show_speed(self, speed):
        return f'My car {self.name} speed = {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\033[31mMy car {self.name} speed {self.speed}.  OVERSPEED!!!!\033[0m '
        else:
            return f'\033[32m My car {self.name} speed {self.speed}\033[0m'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\033[31mMy car {self.name} speed {self.speed}.  OVERSPEED!!!!\033[0m'
        else:
            return f'\033[32m My car {self.name} speed {self.speed}\033[0m'


class SportCar(Car):
    sport_car = True


class PoliceCar(Car):
    is_police = True


work_car = WorkCar('ZIL', 'Red', 50)
work_car.go(54)
print(work_car.show_speed())
work_car.turn(1)
work_car.stop()
work_car.go(0)
work_car.turn(0)
print()

police_car = PoliceCar('BMW', 'Blue', 100)
police_car.go(100)
print(police_car.show_speed(100))
print()

town_car = TownCar('Kia', 'White', 60)
town_car.go(61)
print(town_car.show_speed())
town_car.go(40)
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()
print()
