class Monster:
    def __init__(self):
        self.name = ""
        self.health = 100

    def decrease_health(self, amount):
        self.health = self.health - amount

        if self.health <= 0:
                print("The creature has died! ")
        else:
                print(f"The creature has {self.health} left")

def main():



    monstru = Monster()

    while monstru.health >= 0:
        damage = int(input("Amount of damage u dealt: "))
        monstru.decrease_health(damage)


main()
