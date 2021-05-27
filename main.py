import Genetic_Algoritm


def print_population(population):
    schedules = population.get_chromosomes()

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
            ['math', 4], ['ang', 3], ['history', 1], ['polish', 2], ['IT', 2], ['Physic', 1]
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
        group7 = Group('VA')
        group8 = Group('VB')
        group9 = Group('VIA')
        group10 = Group('VIB')
        self.groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10]

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

genetic = Genetic_Algoritm.GA(mutation_ratio=0.01, population_size=50, no_elite_chromosomes=1,
                              size_of_tournament_selection=3, data=data)
population = Genetic_Algoritm.Population(genetic.population_size, data)
population.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
print_population(population)

while population.get_chromosomes()[0].get_fitness() != 1.0:
    population = genetic.evolve(population)
    population.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
    print_population(population)
    print()

best_table = population.get_chromosomes()[0].get_classes()
classes = data.groups
