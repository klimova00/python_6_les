class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой!')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом!')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером!')


my_title = Stationery('paints')
my_title.draw()
print()

my_title = Pen('pen')
my_title.draw()
print()

my_title = Pencil('pencil')
my_title.draw()
print()

my_title = Handle('handle')
my_title.draw()
print()
