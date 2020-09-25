labyrinthe = [[00, -1, 00, 00, 00, 00, 00],
              [00, -1, 00, -1, -1, 00, -1],
              [00, -1, 00, -1, 'G', 00, 00],
              [00, 00, 00, 00, -1, -1, 00],
              [00, -1, 00, -1, 00, 00, 00],
              [00, -1, 00, 00, 00, -1, 00]]


movecount = 0


def displaylaby(labyrinthe):
    for y in range(0, 6):
        print(labyrinthe[y])


def move(actualposition, nextposition):
    global movecount

    if movecount == 0:
        movecount += 1
        labyrinthe[actualposition[0]][actualposition[1]] = movecount
        print("je commence à la position {}".format(actualposition))
        displaylaby(labyrinthe)

    while labyrinthe[actualposition[0]][actualposition[1]] != 'G':
        # si la case au SUD est dans le labyrinthe et que la case est vide ou G
        if actualposition[0] + 1 <= len(labyrinthe) - 1 and ((labyrinthe[actualposition[0] +1][actualposition[1]] == 0) or
                                                             (labyrinthe[actualposition[0] +1][actualposition[1]] == 'G')):
            # déplacement au SUD
            nextposition = actualposition[0]+1, actualposition[1]
            print("je me déplace à la position {}".format(nextposition))
            actualposition = nextposition
            movecount += 1
            if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
                print("j'ai gagné en {} coups à la position {}".format(movecount, actualposition))
                break
            # marquage du passage
            labyrinthe[actualposition[0]][actualposition[1]] = movecount
            displaylaby(labyrinthe)

        # si la case à l'EST est dans le labyrinthe et que la case est vide ou G
        elif actualposition[1] + 1 <= len(labyrinthe[0]) - 1 and ((labyrinthe[actualposition[0]][actualposition[1] + 1] == 0) or
                                                                (labyrinthe[actualposition[0]][actualposition[1] + 1] == 'G')):
            # déplacement à l'EST
            nextposition = actualposition[0], actualposition[1] +1
            print("je me déplace à la position {}".format(nextposition))
            actualposition = nextposition
            movecount += 1
            if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
                print("j'ai gagné en {} coups à la position {}".format(movecount, actualposition))
                break
            # marquage du passage
            labyrinthe[actualposition[0]][actualposition[1]] = movecount
            displaylaby(labyrinthe)

        # si la case au NORD est dans le labyrinthe et que la case est vide ou G
        elif actualposition[0] - 1 >= 0 and ((labyrinthe[actualposition[0] - 1][actualposition[1]] == 0) or
                                           (labyrinthe[actualposition[0] - 1][actualposition[1]] == 'G')):
            # déplacement au NORD
            nextposition = actualposition[0] -1, actualposition[1]
            print("je me déplace à la position {}".format(nextposition))
            actualposition = nextposition
            movecount += 1
            if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
                print("j'ai gagné en {} coups à la position {}".format(movecount, actualposition))
                break
            # marquage du passage
            labyrinthe[actualposition[0]][actualposition[1]] = movecount
            displaylaby(labyrinthe)

        # si la case à l'OUEST est dans le labyrinthe et que la case est vide ou G
        elif (actualposition[1] - 1) >= 0 and ((labyrinthe[actualposition[0]][actualposition[1] - 1] == 0) or
                                             (labyrinthe[actualposition[0]][actualposition[1] - 1] == 'G')):
            # déplacement à l'OUEST
            nextposition = actualposition[0], actualposition[1] -1
            print("je me déplace à la position {}".format(nextposition))
            actualposition = nextposition
            movecount += 1
            if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
                print("j'ai gagné en {} coups à la position {}".format(movecount, actualposition))
                break
            # marquage du passage
            labyrinthe[actualposition[0]][actualposition[1]] = movecount
            displaylaby(labyrinthe)
    return


if __name__ == '__main__':
    startposition = [0, 0]
    nextposition = [0, 0]
    displaylaby(labyrinthe)
    move(startposition, nextposition)
