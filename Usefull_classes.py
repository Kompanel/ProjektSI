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
