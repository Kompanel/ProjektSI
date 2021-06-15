import Genetic_Algoritm
import Display
import files


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

        self.time_hasmap = {
            'mon1': 'Monday\n8:00-8:45', 'mon2': 'Monday\n9:00-9:45', 'mon3': 'Monday\n10:00-10:45',
            'mon4': 'Monday\n11:00-11:45', 'mon5': 'Monday\n12:00-12:45', 'mon6': 'Monday\n13:00-13:45',
            'mon7': 'Monday\n14:00-14:45', 'mon8': 'Monday\n15:00-15:45',
            'tue1': 'Tuesday\n8:00-8:45', 'tue2': 'Tuesday\n9:00-9:45', 'tue3': 'Tuesday\n10:00-10:45',
            'tue4': 'Tuesday\n11:00-11:45', 'tue5': 'Tuesday\n12:00-12:45', 'tue6': 'Tuesday\n13:00-13:45',
            'tue7': 'Tuesday\n14:00-14:45', 'tue8': 'Tuesday\n15:00-15:45',
            'wed1': 'Wednesday\n8:00-8:45', 'wed2': 'Wednesday\n9:00-9:45', 'wed3': 'Wednesday\n10:00-10:45',
            'wed4': 'Wednesday\n11:00-11:45', 'wed5': 'Wednesday\n12:00-12:45', 'wed6': 'Wednesday\n13:00-13:45',
            'wed7': 'Wednesday\n14:00-14:45', 'wed8': 'Wednesday\n15:00-15:45',
            'thu1': 'Thursday\n8:00-8:45', 'thu2': 'Thursday\n9:00-9:45', 'thu3': 'Thursday\n10:00-10:45',
            'thu4': 'Thursday\n11:00-11:45', 'thu5': 'Thursday\n12:00-12:45', 'thu6': 'Thursday\n13:00-13:45',
            'thu7': 'Thursday\n14:00-14:45', 'thu8': 'Thursday\n15:00-15:45',
            'fri1': 'Friday\n8:00-8:45', 'fri2': 'Friday\n9:00-9:45', 'fri3': 'Friday\n10:00-10:45',
            'fri4': 'Friday\n11:00-11:45', 'fri5': 'Friday\n12:00-12:45', 'fri6': 'Friday\n13:00-13:45',
            'fri7': 'Friday\n14:00-14:45', 'fri8': 'Friday\n15:00-15:45'
        }

        self.subjects = [
            ['math', 5], ['ang', 3], ['history', 3], ['polish', 4], ['IT', 3], ['Physic', 3]
        ]

        self.subject_hasmap_tab = {
            'math': 0, 'ang': 1, 'history': 2, 'polish': 3, 'IT': 4, 'Physic': 5
        }

        self.classrooms = files.rooms_tab()
        self.teachers = files.teacher_tab()
        self.groups = files.groups_tab()

    def get_time(self):
        return self.time

    def get_group_hashmap(self):
        hashmap = {}

        for i in range(len(self.groups)):
            hashmap[self.groups[i]] = i

        return hashmap

    def get_time_hasmap(self):
        hashmap = {}

        for i in range(len(self.time)):
            hashmap[self.time[i]] = i

        return hashmap

    def get_reverse_time_hasmap(self):
        hashmap = {}

        for i in range(len(self.time)):
            hashmap[i] = self.time[i]

        return hashmap

    def get_subject_for_fitness(self):
        tab = []

        for i in range(len(self.subjects)):
            tab.append(self.subjects[i][1])

        return tab

    def get_time_hasmap_to_string(self):
        return self.time_hasmap


data = Configuration()

x = input("Do you want to use default param? [Y,N]")

mutation_ratio = 0.01
population_size = 50
no_elite_chromosomes = 1

if x == "N":
    print("Input values")
    mutation_ratio = input("mutation_ratio: ")
    population_size = input("population_size: ")
    no_elite_chromosomes = input("no_elite_chromosomes: ")


genetic = Genetic_Algoritm.GA(mutation_ratio=0.01, population_size=50, no_elite_chromosomes=1, data=data)

best_table = genetic.get_best_table()

Display.display_table(groups=data.groups, time=data.time, tab_schedule=best_table, group_hashmap=data.get_group_hashmap(),
                      time_hasmap=data.get_time_hasmap(), time_hasmap_to_string=data.get_time_hasmap_to_string())

