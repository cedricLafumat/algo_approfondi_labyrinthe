labyrinthe = [[0, 1, 0, 0, 0, 0, 0],
              [0, 1, 0, 1, 1, 0, 1],
              [0, 1, 0, 1, 'G', 0, 0],
              [0, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 1, 0]]


def displaylaby(labyrinthe):
    for y in range(0, 6):
        print(labyrinthe[y])


def move(actualposition):
    if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
        print("j'ai gagné")
        return
    if actualposition[0] + 1 > len(labyrinthe) - 1 or (labyrinthe[actualposition[0] +1][actualposition[1]] != 0 and
                                                       labyrinthe[actualposition[0] +1][actualposition[1]] != 'G'):
        
#
# def move(actualposition, movecount, crossroad):
#     if labyrinthe[actualposition[0]][actualposition[1]] == 'G':
#         print("j'ai gagné")
#         return
#     print("je n'ai pas gagné")
#     movecount += 1
#     labyrinthe[actualposition[0]][actualposition[1]] = movecount
#     displaylaby(labyrinthe)
#     possiblePath = checkAllDirection(actualposition)
#     if len(possiblePath) > 1:
#         crossroad.append(actualposition)
#         print("je me déplace à l'emplacement : {}".format(possiblePath[0]))
#         while len(possiblePath) > 1:
#             actualposition = possiblePath[0]
#             move(actualposition, movecount, crossroad)
#             del possiblePath[0]
#     elif len(possiblePath) == 1:
#         print("je me déplace à l'emplacement : {}".format(possiblePath[0]))
#         actualposition = possiblePath[0]
#         move(actualposition, movecount, crossroad)
#     if len(possiblePath) == 0:
#         return
#
#
#
#
#     # print(actualposition)
#     # if labyrinthe[actualposition[0]][actualposition[1]] == 2 & len(possiblePath) == 2:
#     #     labyrinthe[actualposition[0]][actualposition[1]] = 1
#     # if len(possiblePath) == 1:
#     #     labyrinthe[actualposition[0]][actualposition[1]] = 1
#     #     actualposition = possiblePath[0]
#     #     print(actualposition)
#     #     possiblePath = checkAllDirection(actualposition)
#     #     move(actualposition, possiblePath)
#     # else:
#     #     labyrinthe[actualposition[0]][actualposition[1]] = 2
#     #     actualposition = possiblePath[0]
#     #     possiblePath = checkAllDirection(actualposition)
#     #     move(actualposition, possiblePath)
#
#
#
# def checkAllDirection(coord):
#     possiblePath = []
#     # bloc Sud
#     if coord[0] +1 > len(labyrinthe) - 1 or (labyrinthe[coord[0] +1][coord[1]] != 0 and labyrinthe[coord[0] +1][coord[1]] != 'G'):
#         S = None
#     else:
#         S = [coord[0] +1, coord[1]]
#
#     # bloc Est
#     if coord[1] +1 > len(labyrinthe[0]) -1 or (labyrinthe[coord[0]][coord[1]+1] != 0 and labyrinthe[coord[0]][coord[1]+1] != 'G'):
#         E = None
#     else:
#         E = [coord[0], coord[1] + 1]
#
#     # bloc Nord
#     if coord[0] - 1 < 0 or (labyrinthe[coord[0]-1][coord[1]] != 0 and labyrinthe[coord[0]-1][coord[1]] != 'G'):
#         N = None
#     else:
#         N = [coord[0] -1, coord[1]]
#
#     # bloc Ouest
#     if coord[1] - 1 < 0 or (labyrinthe[coord[0]][coord[1] -1] != 0 and labyrinthe[coord[0]][coord[1] -1] != 'G'):
#         O = None
#     else:
#         O = [coord[0], coord[1] -1]
#
#     if S != None:
#         possiblePath.append(S)
#     if E != None:
#         possiblePath.append(E)
#     if N != None:
#         possiblePath.append(N)
#     if O != None:
#         possiblePath.append(O)
#
#     print("chemin possible depuis la case {} : {}".format(coord, possiblePath))
#     return possiblePath


if __name__ == '__main__':
    displaylaby(labyrinthe)
    startposition = [0, 0]
    move(startposition)
    # crossroad = []
    # movecount = 0
    # move(startposition, movecount, crossroad)
