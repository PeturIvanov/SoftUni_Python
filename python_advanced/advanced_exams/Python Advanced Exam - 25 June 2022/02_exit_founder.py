SIZE = 6

players = input().split(", ")

maze = [input().split() for _ in range(SIZE)]

current_player = [players[0], [], True]
next_player = [players[1], [], True]

while True:
    coordinates = input()

    current_player[1] = [int(n) for n in coordinates if n.isdigit()]

    if not current_player[2]:
        current_player, next_player = next_player, current_player
        next_player[2] = True
        continue

    r, c = current_player[1]

    position = maze[r][c]

    if position == "E":
        print(f"{current_player[0]} found the Exit and wins the game!")
        break

    elif position == "T":
        print(f"{current_player[0]} is out of the game! The winner is {next_player[0]}.")
        break

    elif position == "W":
        print(f"{current_player[0]} hits a wall and needs to rest.")
        current_player[2] = False


    current_player, next_player = next_player, current_player
