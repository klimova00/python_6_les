class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._widht = width
    def massa_calc(self, weight = 10, thickness = 5):
        return f'Mass of Asphalt ' \
               f'(with lenght = {self._lenght}, ' \
               f'widht = {self._widht}, ' \
               f'weight = {weight}, ' \
               f'thickness = {thickness} ) ' \
               f' = {(self._lenght*self._widht * weight * thickness)} t.'

My_road = Road(1,1)
print(My_road.massa_calc())
