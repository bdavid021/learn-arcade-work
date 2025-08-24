class Room:
    def __init__(self, description, north, south, west, east):
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.south = south


def main():
    """
    functia main, care ruleaza clasa Room si creeaza descrierile pentru camere
    """
    current_room =  0

    room_list = []


    room = Room("Esti intr-un balcon spatios, te uiti la apusul frumos  de soare. Te simti obosit dupa o lunga zi de munca. La est este o alta incapere", None, None, None, 1)
    room_list.append(room)

    room = Room("Esti intr-o camera, cu un mic fotoliu, e mai cald in interior, dar esti tot obosit. La est este o alta incapere", None, None, None, 2)
    room_list.append(room)

    room = Room("Esti in holul casei, nimic prea special, la vest e bucataria, la nord e dormitorul", 4, 1, 3, None)
    room_list.append(room)

    room = Room("Esti in bucatarie, ai luat un mic snack inainte de culcare, la est e holul", None, None, None, 2)
    room_list.append(room)

    room = Room("Esti in dormitor, esti foarte obosit si iti vine sa dormi. Noapte buna", None, 2, None, None)
    room_list.append(room)

    done = False

    while done == False:
        print()
        print(room_list[current_room].description)
        choice = input("Unde vrei sa mergi? ")

        if choice == "e" or choice == "east":
            next_room = room_list[current_room].east
            current_room = next_room

        elif choice == "w" or choice == "west":
            next_room = room_list[current_room].west
            current_room = next_room

        elif choice == "n" or choice == "north":
            next_room = room_list[current_room].north
            current_room = next_room

        elif choice == "s" or choice == "south":
            next_room = room_list[current_room].south
            current_room = next_room


        elif choice == "quit":
            done = True

        else:
            print("Nu poti sa mergi pe acolo! ")
            continue












main()

print("mersi de joc")