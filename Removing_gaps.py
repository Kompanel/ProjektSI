def single_one(table, clas, day):
    for i in range(8):

        if table[clas][day * 8 + i - 1] == 0:

            if table[clas][day * 8 + i] != 0:
                if i + 1 < 8:
                    if table[clas][day * 8 + i + 1] != 0:

                        while table[clas][day * 8 + i]:
                            if i + 1 < 8:
                                i += 1
                            else:
                                break
                    else:
                        return day * 8 + i

    return -1


def find_last_one(table, clas, day):
    for i in reversed(range(8)):
        if table[clas][day * 8 + i] != 0:
            return day * 8 + i

    return -1


def zero(table, clas, day):
    for i in range(7):
        if table[clas][day * 8 + i] != 0:
            if table[clas][day * 8 + i + 1] == 0:
                x = find_last_one(table=table, clas=clas, day=day)
                if day * 8 + i < x:
                    return day * 8 + i + 1
    return -1


def remove_gaps(tab, clas, day, timehasmap):

    while zero(table=tab, clas=clas, day=day) != -1:

        index_of_gap = zero(table=tab, clas=clas, day=day)
        index_of_one = single_one(table=tab, clas=clas, day=day)

        if index_of_one == -1:
            index_of_one = find_last_one(table=tab, clas=clas, day=day)

        x = tab[clas][index_of_one]
        tab[clas][index_of_one] = 0
        tab[clas][index_of_gap] = x
        tab[clas][index_of_gap].meeting_time = timehasmap[index_of_gap]