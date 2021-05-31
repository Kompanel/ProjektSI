import Usefull_classes
#strip()

def teacher_tab():
    tab = []

    teacher_file = open("teachers.txt")

    lines = teacher_file.readlines()

    for i in range(len(lines)):
        line = lines[i].split(':')
        line[1] = line[1].strip()
        subjects = line[1].split(',')

        tab.append(Usefull_classes.Teacher(line[0], subjects))


    teacher_file.close()

    return tab

def groups_tab():
    tab = []

    groups_tab = open("groups.txt")

    groups = groups_tab.readline()

    group = groups.split(',')

    for i in range(len(group)):
        tab.append(Usefull_classes.Group(group[i]))

    groups_tab.close()

    return group


def rooms_tab():
    tab = []

    rooms_tab = open("rooms.txt")

    rooms = rooms_tab.readline()

    room = rooms.split(',')

    for i in range(len(room)):
        tab.append(Usefull_classes.Classroom(room[i]))


    rooms_tab.close()

    return tab