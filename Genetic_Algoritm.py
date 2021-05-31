import random


class GA:

    def __init__(self, mutation_ratio, population_size, no_elite_chromosomes, size_of_tournament_selection, data):
        self.mutation_ratio = mutation_ratio
        self.population_size = population_size
        self.no_elite_chromosomes = no_elite_chromosomes
        self.size_of_tournament_selection = size_of_tournament_selection
        self.data = data

    def evolve(self, pop):
        return self.mutate_population((self.crossover_population(pop)))

    def crossover_population(self, population):
        population_to_crossover = Population(0, self.data)

        for i in range(self.no_elite_chromosomes):
            population_to_crossover.get_chromosomes().append(population.get_chromosomes()[i])

        i = self.no_elite_chromosomes

        while i < self.population_size:
            chromosome1 = self.select_tournament_population(population).get_chromosomes()[0]
            chromosome2 = self.select_tournament_population(population).get_chromosomes()[0]
            population_to_crossover.get_chromosomes().append(self.crossover_chromosome(chromosome1, chromosome2))
            i += 1
        return population_to_crossover

    def crossover_chromosome(self, chromosome1, chromosome2):
        new_chromosome = Chromosome(self.data).init()

        for i in range(len(new_chromosome.get_classes())):
            if random.random() % 2 == 0:
                new_chromosome.get_classes()[i] = chromosome1.get_classes()[i]
            else:
                new_chromosome.get_classes()[i] = chromosome2.get_classes()[i]

        return new_chromosome

    def mutate_population(self, population):

        for i in range(self.no_elite_chromosomes, self.population_size):
            self.mutate_chromosome(population.get_chromosomes()[i])

        return population

    def mutate_chromosome(self, chromosome_to_mutate):
        chromosome = Chromosome(self.data).init()

        for i in range(0, len(chromosome_to_mutate.get_classes())):
            if self.mutation_ratio > random.random():
                chromosome_to_mutate.get_classes()[i] = chromosome.get_classes()[i]

        return chromosome_to_mutate

    def select_tournament_population(self, pop):

        tournament_pop = Population(0, self.data)
        i = 0

        while i < self.size_of_tournament_selection:
            tournament_pop.get_chromosomes().append(pop.get_chromosomes()[random.randrange(0, self.population_size)])
            i += 1

        tournament_pop.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)

        return tournament_pop


class Chromosome:

    def __init__(self, data):
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
        groups_hash_map = self.data.get_group_hashmap()
        subject_counter_tab = []

        for i in range(len(self.data.groups)):
            subject_counter_tab.append(self.data.get_subject_for_fitness())

        for i in range(0, len(classes)):
            z = 0

            index_group = groups_hash_map[classes[i].group]
            index_lesson = self.data.subject_hasmap_tab[classes[i].lesson]

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

        for j in range(len(self.data.groups)):
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

    def __init__(self, size, data):
        self.size = size
        self.data = data
        self.chromosomes = []

        for i in range(size):
            self.chromosomes.append(Chromosome(self.data).init())

    def get_chromosomes(self):
        return self.chromosomes


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
