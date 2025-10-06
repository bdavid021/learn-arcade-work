import random
import time

class Inventar:
    def __init__(self):
        self.hp_regen = 1
        self.piatra_de_slefuire = 1

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

def text_bine_ai_venit():
    print("Bine ai venit la cel mai Simplu RPG")
    time.sleep(1.5)
    print()
    print("Aici te bati cu un Orc. Trebuie sa il bati, ca sa castigi comoara si sa salvezi regatul")
    time.sleep(1.2)




def main():
    om = Human()
    orc = Orc()
    inventar = Inventar()

    numarul_turei = 1
    cheater = False
    text_bine_ai_venit()


    print("-----")
    print("Alege-ti echipamentul:\n 1- Sabia Magica (creste daunele provocate cu 5) \n 2- Papucii Fermecati (creste sansa de a evade cu 10%) \n 3- Armura fermecata (iti ofera cu 20 mai mult hp)")
    print("-----")


    alegere_echipament = int(input("Ce alegi? Orcul e pregatit de razboi "))

    if alegere_echipament == 1:
        om.base_attack = 15
    elif alegere_echipament == 2:
        sunttare = True
    elif alegere_echipament == 3:
        om.hp = 120



    while om.hp >= 0:

        # Tura omului
        print("-----")
        print("Tasteaza: \n 1- ca sa deschizi inventarul \n 2- pentru a folosi rapid o potiune de viata \n 3- pentru a folosi o piatra de slefuire in acest atac \n 4- pentru a iesi din meniu")
        actiune = int(input("Ce actiune vrei sa faci: "))



        while actiune != 4:
            if actiune == 1:
                print(f"In inventarul tau {inventar.hp_regen } ai potiuni de HP si {inventar.piatra_de_slefuire} pietre de slefuire")
            elif actiune == 2 and inventar.hp_regen > 0:
                om.hp = om.hp + 20
                inventar.hp_regen -= 1
                print(f"Gulp, Gulp, Gulp... nu stii de ce, dar te simti mai sanatos. Ti-ai crescut viata cu 20, acum ai {om.hp}")
            elif actiune == 3 and inventar.piatra_de_slefuire > 0:
                inventar.piatra_de_slefuire -= 1
                om.base_attack = om.base_attack + 5
                print("I-ai spus Orcului sa stea putin pana iti slefuiesti sabia. Acum ataci mai tare pentru 1 tura. Haide, Orcul nu mai are rabdare ")
            else:
                print("Incerci sa fentezi sistemul? ei bine smecherasule... vei devenii o testoasa slaba")
                om.hp = 10
                om.base_attack = 1
                print(f"Mai ai {om.hp} hp si ataci cu {om.base_attack}, deasemenea fiind foarte slab, ti-ai scapat itemele")
                inventar.hp_regen = 0
                inventar.piatra_de_slefuire = 0
                cheater = True

            print("-----")
            actiune = int(input("Ce actiune vrei sa mai faci: "))

        input("Apasa \"y\" ca sa dai cu zarul: ")

        sansa = random.randint(1, 6)
        print("-----")

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



        if dodge_chance == 1:

            print("Te-ai ferit de data asta de atacul Orcului! A devenit mai nervos...")

        else:
            print("Orcul da cu zarul")
            if cheater == True:
                print("Orcul se rade de tine!")
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

        if cheater != True:
            om.base_attack = 10


    print("Ai fost invins! data viitoare ii areti tu orcului cine-i mai tare!")

main()
