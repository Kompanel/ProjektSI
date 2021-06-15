def repair_day(tab, day, number_of_class, table_of_teacher):
    table_of_teachers_in_day = []

    for time in range(8):
        for clas in range(number_of_class):

            if tab[clas][day * 8 + time] != 0:

                teacher_exist = False

                for i in range(len(table_of_teachers_in_day)):

                    if table_of_teachers_in_day[i] == tab[clas][day * 8 + time].teacher:
                        teacher_exist = True
                        break

                if not teacher_exist:
                    table_of_teachers_in_day.append(tab[clas][day * 8 + time].teacher)
                else:
                    is_he_busy = False

                    for clas_again in range(number_of_class):

                        if tab[clas_again][day * 8 + time] != 0:
                            if clas_again != clas:
                                if tab[clas_again][day * 8 + time].teacher == tab[clas][day * 8 + time].teacher:
                                    is_he_busy = True
                                    break

                    if not is_he_busy:

                        for i in range(len(table_of_teacher)):
                            if table_of_teacher[i] == tab[clas][day * 8 + time]:

                                does_he_teach_lesson = False

                                for j in range(len(table_of_teacher[i][1])):
                                    if table_of_teacher[i][1][j] == tab[clas][day * 8 + time].lesson:
                                        does_he_teach_lesson = True
                                        break

                                if does_he_teach_lesson:
                                    tab[clas][day * 8 + time].teacher = table_of_teacher[i][0]
                                else:
                                    table_of_teachers_in_day.append(tab[clas][day * 8 + time])
                    else:
                        table_of_teachers_in_day.append((tab[clas][day * 8 + time]))