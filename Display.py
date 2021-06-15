from tabulate import tabulate


def display_table(tab_schedule, groups, time, group_hashmap, time_hasmap, time_hasmap_to_string):
    tab = []

    first_row = ['']

    for i in range(len(groups)):
        first_row.append(groups[i])

    tab.append(first_row)

    for i in range(len(time)):
        row =[]

        row.append(time_hasmap_to_string[time[i]])
        for j in range(len(groups)):
            row.append("")

        tab.append(row)

    for clas in tab_schedule:
        indexy = group_hashmap[clas.group] + 1
        indexx = time_hasmap[clas.meeting_time] + 1
        string = clas.lesson + "\n" + clas.teacher.name + "\n" + str(clas.classroom.number_of_classroom)

        tab[indexx][indexy] = string

    print(tabulate(tab, headers="firstrow", tablefmt="grid"))

    file = open("Class_table.txt", "w")
    file.write(tabulate(tab, headers="firstrow", tablefmt="grid"))
    file.close()
