import random
import time

class Human:
    def __init__(self):
        self.hp = 100
        self.base_attack = 10
        self.dodge_change = random.randint(1,5)

class Orc:
    def __init__(self):
        self.orc_hp = 150
        self.base_attack = random.randint(5, 15)

def dodge_chance_calculation(papuci):
    if papuci == 1:
        print("Ai dat dodge, ai scapat de data asta!")



def main():
    om = Human()
    orc = Orc()

    numarul_turei = 1

    print ("Bine ai venit la cel mai Simplu RPG")
    time.sleep(1.5)
    print ()
    print ("Aici te bati cu un Orc. Trebuie sa il bati, ca sa castigi comoara si sa salvezi regatul")
    time.sleep(2.5)
    print("-----")
    print(
        "Alege-ti echipamentul:\n 1- Sabia Magica (creste daunele provocate cu 5) \n 2- Papucii Fermecati (creste sansa de a evade cu 10%) \n 3- Armura fermecata (iti ofera cu 20 mai mult hp)")
    print("-----")

    alegere_echipament = int(input("Ce alegi? Orcul e pregatit de razboi "))

    if alegere_echipament == 1:
        om.base_attack = 15
    elif alegere_echipament == 2:
        suntTare = True
    elif alegere_echipament == 3:
        om.hp = 120


    while om.hp >= 0:

        # Tura omului

        print("Tasteaza \"y\" ca sa dai cu zarul, numerele pare iti dubleaza daunele provocate")
        input("Da cu zarul: ")
        print("-----")
        sansa = random.randint(1, 6)
        time.sleep(1.5)
        if sansa % 2 == 0:
            double_damage = om.base_attack * 2
            print(f"Ai dat {sansa} si ti-ai dublat atacul!")
            print(f" Ai atacat cu {double_damage} orcul")
            orc.orc_hp = orc.orc_hp - double_damage
            print(f"Orcul mai are acum {orc.orc_hp} hp")
            time.sleep(1.5)
        else:
            print(f"Ai dat {sansa}, insa nu ti-ai dublat atacul")
            print(f"Ai atacat cu {om.base_attack}")
            orc.orc_hp = orc.orc_hp - om.base_attack
            print(f"Orcul mai are acum {orc.orc_hp}")
            time.sleep(1.5)

        print()
        time.sleep(2)

        if orc.orc_hp <= 0:
            print(f"Ai invins orcul dupa {numarul_turei} ture si ai salvat comoara si regatul!")
            exit(0)

        print("-----")
        print("Tura Orcului...")
        if alegere_echipament == 2:
            dodge_chance = random.randint(1, 4)
        else:
            dodge_chance = random.randint(1, 6)

        print(f"Dodge number {dodge_chance}")

        if dodge_chance == 1:

            print("Te-ai ferit de data asta de atacul Orcului! A devenit mai nervos...")

        else:
            print("Orcul da cu zarul")
            time.sleep(3)
            orc.base_attack = random.randint(5, 15)

            orc_sansa = random.randint(1, 6)

            if orc_sansa % 2 == 0:

                orc_double_damage = orc.base_attack * 2
                print(f"Orcul a dat {orc_sansa} si si-a dublat damage-ul atacul acesta!!\n")

                if orc_double_damage >= 15:
                    print("Pfa... o lovitura colosala din partea Orcului")
                    time.sleep(4)

                print(f"Orcul te ataca cu {orc_double_damage} hp")
                om.hp = om.hp - orc_double_damage
                print(f"Mai ai {om.hp} hp!")
                time.sleep(1.5)

            else:
                print(f"Orcul te ataca cu {orc.base_attack} hp")
                om.hp = om.hp - orc.base_attack
                print(f"Mai ai {om.hp} hp!")
                time.sleep(1.5)
        numarul_turei = numarul_turei + 1
        print()
        print (f"----------------Tura {numarul_turei}, tine-te bine")
        print()



    print("Ai fost invins! data viitoare ii areti tu orcului cine-i mai tare!")

main()