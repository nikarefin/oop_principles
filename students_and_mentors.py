class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.rates = {}
        self.avg_rate = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.avg_rate}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершённые курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_rate < other.avg_rate
        else:
            return 'Ошибка'

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.rates and rate in range(1, 11):
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

        rates_sum = 0
        rates_num = 0
        for rate_values in lecturer.rates.values():
            for value in rate_values:
                rates_sum += sum(rate_values)
                rates_num += len(rate_values)
        lecturer.avg_rate = round(rates_sum / rates_num, 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}
        self.avg_rate = 0

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avg_rate}\n'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate < other.avg_rate
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, rate):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.rates:
                student.rates[course] += [rate]
            else:
                student.rates[course] = [rate]
        else:
            return 'Ошибка'

        rates_sum = 0
        rates_num = 0
        for rates_values in student.rates.values():
            for value in rates_values:
                rates_sum += sum(rates_values)
                rates_num += len(rates_values)
        student.avg_rate = round(rates_sum / rates_num, 2)


def students_avg_rate(students, course):
    students_rates_sum = 0
    for student in students:
        if course in student.courses_in_progress:
            students_rates_sum += student.avg_rate
    return round(students_rates_sum / len(students), 2)


def lecturers_avg_rate(lecturers, course):
    lecturers_rates_sum = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            lecturers_rates_sum += lecturer.avg_rate
    return round(lecturers_rates_sum / len(lecturers), 2)


severus = Lecturer('Severus', 'Snape')
severus.courses_attached = ['Potions', 'DADA']

minerva = Lecturer('Minerva', 'McGonagall')
minerva.courses_attached = ['Transfiguration']

harry = Student('Harry', 'Potter', 'male')
harry.courses_in_progress = ['Potions', 'Transfiguration', 'DADA']
harry.finished_courses = ['Spells']
harry.rate_lecturer(severus, 'Potions', 8)
harry.rate_lecturer(severus, 'DADA', 6)
harry.rate_lecturer(minerva, 'Transfiguration', 9)

hermione = Student('Hermione', 'Granger', 'female')
hermione.courses_in_progress = ['Potions', 'Transfiguration', 'Spells']
hermione.finished_courses = ['DADA']
hermione.rate_lecturer(severus, 'Potions', 10)
hermione.rate_lecturer(minerva, 'Transfiguration', 8)

albus = Reviewer('Albus', 'Dumbledore')
albus.courses_attached = ['Potions', 'Transfiguration', 'DADA']
albus.rate_student(harry, 'Potions', 4)
albus.rate_student(harry, 'Transfiguration', 2)
albus.rate_student(harry, 'DADA', 5)
albus.rate_student(hermione, 'Potions', 5)
albus.rate_student(hermione, 'Transfiguration', 5)

voldemort = Reviewer('Tom', 'Riddle')
voldemort.courses_attached = ['Spells']
voldemort.rate_student(hermione, 'Spells', 3)

print(albus)
print(voldemort)
print(severus)
print(minerva)
print(harry)
print(hermione)
