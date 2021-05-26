import random
import numpy


def print_population(population):
    schedules = population.get_schedules()

    x = str(round(schedules[0].get_fitness(), 3)) + " " + str(schedules[0].get_numberOfConflicts()) + " " + str(
        print_group(schedules[0].get_classes()))

    print(x)


def print_group(table):
    x = "[ "
    a = 0

    for i in range(len(table) - 1):
        x = x + str(table[i]) + ", "
        a = i + 1

    x = x + str(table[a]) + " ]"

    return x


class GA:

    def __init__(self, mutation_ratio, population_size, no_elite_chromosomes, size_of_tournament_selection):
        self.mutation_ratio = mutation_ratio
        self.population_size = population_size
        self.no_elite_chromosomes = no_elite_chromosomes
        self.size_of_tournament_selection = size_of_tournament_selection

    def evolve(self, pop):
        return self.mutate_population((self.crossover_population(pop)))

    def crossover_population(self, population):
        population_to_crossover = Population(0)

        for i in range(self.no_elite_chromosomes):
            population_to_crossover.get_schedules().append(population.get_schedules()[i])

        i = self.no_elite_chromosomes

        while i < self.population_size:
            chromosome1 = self.select_tournament_population(population).get_schedules()[0]
            chromosome2 = self.select_tournament_population(population).get_schedules()[0]
            population_to_crossover.get_schedules().append(self.crossover_chromosome(chromosome1, chromosome2))
            i += 1
        return population_to_crossover

    def crossover_chromosome(self, chromosome1, chromosome2):
        new_chromosome = Schedule().init()

        for i in range(len(new_chromosome.get_classes())):
            if random.random() % 2 == 0:
                new_chromosome.get_classes()[i] = chromosome1.get_classes()[i]
            else:
                new_chromosome.get_classes()[i] = chromosome2.get_classes()[i]

        return new_chromosome

    def mutate_population(self, population):

        for i in range(self.no_elite_chromosomes, self.population_size):
            self.mutate_chromosome(population.get_schedules()[i])

        return population

    def mutate_chromosome(self, chromosome_to_mutate):
        chromosome = Schedule().init()

        for i in range(0, len(chromosome_to_mutate.get_classes())):
            if self.mutation_ratio > random.random():
                chromosome_to_mutate.get_classes()[i] = chromosome.get_classes()[i]

        return chromosome_to_mutate

    def select_tournament_population(self, pop):

        tournament_pop = Population(0)
        i = 0

        while i < self.size_of_tournament_selection:
            tournament_pop.get_schedules().append(pop.get_schedules()[random.randrange(0, self.population_size)])
            i += 1

        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

        return tournament_pop


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
        groups_hash_map = data.get_group_hashmap()
        subject_counter_tab = []

        for i in range(len(data.groups)):
            subject_counter_tab.append(data.get_subject_for_fitness())

        for i in range(0, len(classes)):
            z = 0

            index_group = groups_hash_map[classes[i].group.name]
            index_lesson = data.subject_hasmap_tab[classes[i].lesson]

            subject_counter_tab[index_group][index_lesson] -= 1

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

        for j in range(len(data.groups)):
            for i in range(len(subject_counter_tab[j])):
                self.numberOfConflicts += abs(subject_counter_tab[j][i])

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
            ['math', 4], ['ang', 3], ['history', 1], ['polish', 2], ['IT', 1], ['Physic', 1]
        ]

        self.subject_hasmap_tab = {
            'math': 0, 'ang': 1, 'history': 2, 'polish': 3, 'IT': 4, 'Physic': 5
        }

        classroom1 = Classroom(1)
        classroom2 = Classroom(2)
        classroom3 = Classroom(3)
        classroom4 = Classroom(4)
        classroom5 = Classroom(5)
        classroom6 = Classroom(6)
        classroom7 = Classroom(7)
        classroom8 = Classroom(8)
        classroom9 = Classroom(9)
        self.classrooms = [classroom1, classroom2, classroom3, classroom4, classroom5, classroom6, classroom7,
                           classroom8, classroom9]

        teacher1 = Teacher('Jhon', ['math', 'geo'])
        teacher2 = Teacher('Mike', ['ang', 'Physic', 'history'])
        teacher3 = Teacher('Alex', ['ang', 'history'])
        teacher4 = Teacher('Alice', ['math', 'Physic', 'geo'])
        teacher5 = Teacher('Hector', ['math', 'geo'])
        teacher6 = Teacher('Annie', ['math', 'geo', 'IT'])
        teacher7 = Teacher('Max', ['ang', 'history'])
        teacher8 = Teacher('Victor', ['ang', 'history', 'polish'])
        teacher9 = Teacher('Maximus', ['math', 'Physic', 'polish'])
        teacher10 = Teacher('Ann', ['polish', 'ang', 'IT'])
        teacher11 = Teacher('Annie', ['polish', 'Physic', 'ang', 'IT'])
        teacher12 = Teacher('Mathieu', ['polish', 'Physic', 'ang', 'IT'])
        teacher13 = Teacher('Max', ['polish', 'Physic', 'ang', 'IT'])
        self.teachers = [teacher1, teacher2, teacher3, teacher4, teacher5, teacher6, teacher7, teacher8, teacher9,
                         teacher10, teacher11, teacher12, teacher13]

        group1 = Group('IA')
        group2 = Group('IB')
        group3 = Group('IIA')
        group4 = Group('IIB')
        group5 = Group('IIIA')
        group6 = Group('IIIB')
        self.groups = [group1, group2, group3, group4, group5, group6]

    def get_time(self):
        return self.time

    def get_group_hashmap(self):
        hashmap = {}

        for i in range(len(self.groups)):
            hashmap[self.groups[i].name] = i

        return hashmap

    def get_subject_for_fitness(self):
        tab = []

        for i in range(len(self.subjects)):
            tab.append(self.subjects[i][1])

        return tab


data = Configuration()

genetic = GA(mutation_ratio=0.01, population_size=50, no_elite_chromosomes=2, size_of_tournament_selection=6)
population = Population(genetic.population_size)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
print_population(population)

while population.get_schedules()[0].get_fitness() != 1.0:
    population = genetic.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    print_population(population)
    print()
