import tabulate

def display_table(classes, groups):
    first_row = ['']

    for i in range(len(groups)):
        first_row.append(groups[i].name)

