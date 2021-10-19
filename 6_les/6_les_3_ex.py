class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Full Name: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Full Income: {sum(self._income.values())}'


# Пример проверка
my_worker = Position("Anna", "Klimova", "Student", 10000, 3000)
print(my_worker.get_full_name())
print(my_worker.get_total_income())
