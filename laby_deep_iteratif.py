labyrinthe = [[00, -1, 00, 00, 00, 00, 00],
              [00, -1, 00, -1, -1, 00, -1],
              [00, -1, 00, -1, 'G', 00, 00],
              [00, 00, 00, 00, -1, -1, 00],
              [00, -1, 00, -1, 00, 00, 00],
              [00, -1, 00, 00, 00, -1, 00]]


def displaylaby(labyrinthe):
    for y in range(0, 6):
        print(labyrinthe[y])


def move(actualposition):
    movecount = 0
    historic = []

    if movecount == 0:
        print("je commence à la position {}".format(actualposition))

    while labyrinthe[actualposition[0]][actualposition[1]] != 'G':

        # si ma position à un marqueur, je reviens à ma position précédente
        if (labyrinthe[actualposition[0]][actualposition[1]]) != 0:
            del historic[len(historic) - 1]
            actualposition = historic[len(historic) - 1]
            print("je reviens à la position {} ".format(actualposition))
        # sinon je mets un marqueur
        else:
            movecount += 1
            labyrinthe[actualposition[0]][actualposition[1]] = movecount
            displaylaby(labyrinthe)

        # si la case au SUD est dans le labyrinthe et que la case est vide ou G
        if actualposition[0] + 1 <= len(labyrinthe) - 1 and ((labyrinthe[actualposition[0] +1][actualposition[1]] == 0) or
                                                             (labyrinthe[actualposition[0] +1][actualposition[1]] == 'G')):
            # déplacement au SUD
            nextposition = actualposition[0]+1, actualposition[1]
            print("je me déplace à la position {}".format(nextposition))
            actualposition = nextposition
            historic.append(actualposition)
            if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
                print("j'ai gagné en {} coups à la position {}".format(movecount, actualposition))
                print("historique de déplacement : {}".format(historic))
                break

        # si la case à l'EST est dans le labyrinthe et que la case est vide ou G
        elif actualposition[1] + 1 <= len(labyrinthe[0]) - 1 and ((labyrinthe[actualposition[0]][actualposition[1] + 1] == 0) or
                                                                (labyrinthe[actualposition[0]][actualposition[1] + 1] == 'G')):
            # déplacement à l'EST
            nextposition = actualposition[0], actualposition[1] +1
            print("je me déplace à la position {}".format(nextposition))
            actualposition = nextposition
            historic.append(actualposition)
            if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
                print("j'ai gagné en {} coups à la position {}".format(movecount, actualposition))
                print("historique de déplacement : {}".format(historic))
                break

        # si la case au NORD est dans le labyrinthe et que la case est vide ou G
        elif actualposition[0] - 1 >= 0 and ((labyrinthe[actualposition[0] - 1][actualposition[1]] == 0) or
                                           (labyrinthe[actualposition[0] - 1][actualposition[1]] == 'G')):
            # déplacement au NORD
            nextposition = actualposition[0] -1, actualposition[1]
            print("je me déplace à la position {}".format(nextposition))
            actualposition = nextposition
            historic.append(actualposition)
            if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
                print("j'ai gagné en {} coups à la position {}".format(movecount, actualposition))
                print("historique de déplacement : {}".format(historic))
                break

        # si la case à l'OUEST est dans le labyrinthe et que la case est vide ou G
        elif (actualposition[1] - 1) >= 0 and ((labyrinthe[actualposition[0]][actualposition[1] - 1] == 0) or
                                             (labyrinthe[actualposition[0]][actualposition[1] - 1] == 'G')):
            # déplacement à l'OUEST
            nextposition = actualposition[0], actualposition[1] -1
            print("je me déplace à la position {}".format(nextposition))
            actualposition = nextposition
            historic.append(actualposition)
            if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
                print("j'ai gagné en {} coups à la position {}".format(movecount, actualposition))
                print("historique de déplacement : {}".format(historic))
                break
    return


if __name__ == '__main__':
    startposition = [0, 0]
    displaylaby(labyrinthe)
    move(startposition)
