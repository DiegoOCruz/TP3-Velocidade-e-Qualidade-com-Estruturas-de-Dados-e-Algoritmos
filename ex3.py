def hanoi(disc, ori, dest, aux):
    if disc == 1:
        print('Move disco {} da torre {} para a torre {}'.format(disc, ori, dest))
        return

    hanoi(disc - 1, ori, aux, dest)
    print('Move disco {} da torre {} para a torre {}'.format(disc, ori, dest))
    hanoi(disc - 1, aux, dest, ori)

hanoi(3, 'A', 'B', 'C')