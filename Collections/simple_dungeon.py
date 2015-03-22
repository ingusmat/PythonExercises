import random

CELLS = [(0, 0), (1, 0), (2, 0),
         (0, 1), (1, 1), (2, 1),
         (0, 2), (1, 2), (2, 2)]


def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if monster == door or door == start or start == monster:
        return get_locations()

    return monster, door, start


def draw_room(player, monster, door):
    print("-------------------")
    print("|     |     |     |")
    tile = "  {}  "
    for idx, cell in enumerate(CELLS):
        if player == cell:
            symbol = "*"
        elif monster == cell:
            symbol = "M"
        else:
            symbol = " "

        if cell[0] == 0:
            print("|", end="")
        else:
            print(" ", end="")

        if cell[0] == 2:
            print(tile.format(symbol) + "|")
            print("|     |     |     |")
            if cell[1] == 2:
                print("-------------------")
            else:
                print("--   ---   ---   --")
            if cell[1] != 2:
                print("|     |     |     |")
        else:
            print(tile.format(symbol), end="")


def move_monster(monster):
    moves = get_moves(monster)
    moves.append('STAY')
    move = random.choice(moves)
    return move_player(monster, move)

def move_player(player, move):
    x, y = player

    if move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1
    elif move == "UP":
        y -= 1
    elif move == "DOWN":
        y += 1

    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    if player[0] == 0:
        moves.remove('LEFT')
    if player[0] == 2:
        moves.remove('RIGHT')
    if player[1] == 0:
        moves.remove('UP')
    if player[1] == 2:
        moves.remove('DOWN')

    return moves


print("Welcome to the dungeon")
monster, door, player = get_locations()

while True:
    monster = move_monster(monster)
    draw_room(player, monster, door)
    moves = get_moves(player)
    print("You are currently in room {}".format(player))  # use player position
    print("You can move {}".format(moves)) # use available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == "QUIT":
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print("** Ouch!  You hit a wall")
        continue

    if player == door:
        print("You escaped!!")
        break
    elif player == monster:
        print("You were eaten by the groo!")
        break

