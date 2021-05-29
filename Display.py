from tabulate import tabulate


def display_table(tab_schedule, groups, time, group_hashmap, time_hasmap):
    tab = []

    first_row = ['']

    for i in range(len(groups)):
        first_row.append(groups[i].name)

    tab.append(first_row)

    for i in range(len(time)):
        row =[]

        row.append(time[i])
        for j in range(len(groups)):
            row.append("")

        tab.append(row)

    for clas in tab_schedule:
        indexy = group_hashmap[clas.group.name] + 1
        indexx = time_hasmap[clas.meeting_time] + 1
        string = clas.lesson + "\n" + clas.teacher.name + "\n" + str(clas.classroom.number_of_classroom)

        tab[indexx][indexy] = string

    print(tabulate(tab, headers="firstrow", tablefmt="grid"))