import random

POPULATION_SIZE = 9
NUMBER_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1


def print_group(table):
    x = "[ "
    a = 0

    for i in range(len(table) - 1):
        x = x + str(table[i]) + ", "
        a = i + 1

    x = x + str(table[a]) + " ]"

    return x


# klasa jako pomieszczenie
class Classroom:

    def __init__(self, number_of_classroom, type_of_classroom='all'):
        self.number_of_classroom = number_of_classroom  # numer klasy
        self.type_of_classroom = type_of_classroom  # typ klasy, jakie zajecia tam moga byc

    def __str__(self):
        return str(self.number_of_classroom)


# klasa w sensie grupa
class Group:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)


# nauczyciel
class Teacher:

    def __init__(self, name, subjects):
        self.name = name  # imie nauczyciela
        self.types_of_subjects = []  # jakie typy lekcji naucza

        for subject in subjects:
            self.types_of_subjects.append(subject)

    def __str__(self):
        return str(self.name)

    def get_subject(self):
        return self.types_of_subjects


# zajecia jako wydarzenie
class Class:

    def __init__(self, class_id):
        self.class_id = class_id  # id wydarzenia
        self.teacher = None  # nauczyciel
        self.classroom = None  # klasa gdzie to wystepuje
        self.lesson = None  # jaka lekcja
        self.meeting_time = None  # kiedy
        self.group = None  # jaka klasa

    def set_teacher(self, teacher):
        self.teacher = teacher

    def set_classroom(self, classroom):
        self.classroom = classroom

    def set_lesson(self, lesson):
        self.lesson = lesson

    def set_meeting_time(self, meeting_time):
        self.meeting_time = meeting_time

    def set_group(self, group):
        self.group = group

    def __str__(self):
        return "[ " + str(self.group) + ", " + str(self.classroom) + ", " + str(self.lesson) + ", " + str(
            self.teacher) + ", " + self.meeting_time + " ]"


# nazwa lekcji
class Lesson:

    def __init__(self, name):
        self.name = name


class Configuration:

    def __init__(self):
        self.classrooms = []
        self.teachers = []
        self.groups = []
        self.time = ['mon1', 'mon2', 'mon3', 'mon4', 'mon5', 'mon6', 'mon7', 'mon8',
                     'tue1', 'tue2', 'tue3', 'tue4', 'tue5', 'tue6', 'tue7', 'tue8',
                     'wed1', 'wed2', 'wed3', 'wed4', 'wed5', 'wed6', 'wed7', 'wed8',
                     'thu1', 'thu2', 'thu3', 'thu4', 'thu5', 'thu6', 'thu7', 'thu8',
                     'fri1', 'fri2', 'fri3', 'fri4', 'fri5', 'fri6', 'fri7', 'fri8']

        self.subjects = [
            ['math', 4], ['geo', 3], ['ang', 3], ['history', 2]
        ]

        classroom1 = Classroom(1)
        classroom2 = Classroom(2)
        classroom3 = Classroom(3)
        self.classrooms = [classroom1, classroom2, classroom3]

        teacher1 = Teacher('Jhony', ['math', 'geo'])
        teacher2 = Teacher('Mike', ['ang', 'history'])
        self.teachers = [teacher1, teacher2]

        group1 = Group('IA')
        group2 = Group('IB')
        group3 = Group('IC')
        self.groups = [group1, group2, group3]

    def get_time(self):
        return self.time


class Schedule:

    def __init__(self):
        self.data = data
        self.classes = []
        self.numberOfConflicts = 0
        self.fitness = -1
        self.numberOfClasses = 0
        self.classNumber = 0
        self.fitnessChanged = True

    def get_classes(self):
        self.fitnessChanged = True
        return self.classes

    def get_numberOfConflicts(self):
        return self.numberOfConflicts

    def get_fitness(self):
        if self.fitnessChanged:
            self.fitness = self.calculate_fitness()
            self.fitnessChanged = False
        return self.fitness

    def init(self):

        for subject in self.data.subjects:
            self.numberOfClasses += subject[1]

        self.numberOfClasses *= len(self.data.groups)  # classes puste

        for i in range(self.numberOfClasses):
            newClass = Class(self.classNumber)
            newClass.set_meeting_time(self.data.time[random.randrange(0, len(self.data.time))])
            newClass.set_classroom(self.data.classrooms[random.randrange(0, len(self.data.classrooms))])
            newClass.set_teacher(self.data.teachers[random.randrange(0, len(self.data.teachers))])
            newClass.set_group(self.data.groups[random.randrange(0, len(self.data.groups))])
            newClass.set_lesson(self.data.subjects[random.randrange(0, len(self.data.subjects))][0])
            self.classes.append(newClass)
        return self

    def calculate_fitness(self):
        self.numberOfConflicts = 0
        classes = self.get_classes()

        for i in range(0, len(classes)):
            z = 0

            teacher_types_of_subject = classes[i].teacher.get_subject()

            for j in range(len(teacher_types_of_subject)):
                if classes[i].lesson == teacher_types_of_subject[j]:
                    z += 1

            if z == 0:
                self.numberOfConflicts += 1

            for j in range(0, len(classes)):
                if classes[i].meeting_time == classes[j].meeting_time and classes[i].class_id != classes[j].class_id:
                    if classes[i].classroom == classes[j].classroom:
                        self.numberOfConflicts += 1
                    if classes[i].teacher == classes[j].teacher:
                        self.numberOfConflicts += 1

        return 1 / (1.0 * self.numberOfConflicts + 1)

    def __str__(self):
        string = ""

        for i in range(0, len(self.classes) - 1):
            string += str(self.classes[i]) + ", "
        string += str(self.classes[len(self.classes) - 1])

        return string


class Population:

    def __init__(self, size):
        self.size = size
        self.data = data
        self.schedules = []

        for i in range(size):
            self.schedules.append(Schedule().init())

    def get_schedules(self):
        return self.schedules


class Display:

    def print_generation(self, population):
        schedules = population.get_schedules()

        for i in range(len(schedules)):
            x = str(round(schedules[i].get_fitness(), 3)) + " " + str(schedules[i].get_numberOfConflicts()) + " " + str(
                print_group(schedules[i].get_classes()))

            print(x)

    def print_schedule_as_table(self):
        return None

#
# class GA:
#
#     def evolve(self, population):
#         return self.mutate_population(self.crossover_population(population))
#
#     def crossover_population(self, pop):
#         crossover_population = Population(0)
#
#         for i in range(NUMBER_OF_ELITE_SCHEDULES):
#             crossover_population.get_schedules().append(pop.get_schedules()[i])
#         i = NUMBER_OF_ELITE_SCHEDULES
#
#         while i < POPULATION_SIZE:
#             schedule1 = self.select_tournament_population(pop).get_schedules()[0]
#             schedule2 = self.select_tournament_population(pop).get_schedules()[0]
#             crossover_population.get_schedules().append(self.crossover_schedule(schedule1, schedule2))
#             i += 1
#
#         return crossover_population
#
#     def mutate_population(self, population):
#         for i in range(NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE):
#             self.mutate_schedule(population.get_schedules()[i])
#         return population
#
#     def crossover_schedule(self, schedule1, schedule2):
#         crossoverSchedule = Schedule().init()
#
#         for i in range(0, len(crossoverSchedule.get_classes())):
#             if random.random() > 0.5:
#                 crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
#             else:
#                 crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
#
#         return crossoverSchedule
#
#     def mutate_schedule(self, mutateSchedule):
#         schedule = Schedule.init()
#
#         for i in range(0, len(mutateSchedule.get_classes())):
#             if MUTATION_RATE > random.random():
#                 mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
#
#         return mutateSchedule
#
#     def select_tournament_population(self, pop):
#         tournament_pop = Population(0)
#         i = 0
#
#         while i < TOURNAMENT_SELECTION_SIZE:
#             tournament_pop.get_schedules().append(pop.get_schedules()[random.randrange(0, POPULATION_SIZE)])
#             i += 1
#
#         tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
#
#         return tournament_pop


data = Configuration()
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

display = Display()
display.print_generation(population)


