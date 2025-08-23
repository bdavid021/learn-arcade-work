import random
import arcade

numar = random.randint(1, 100)  # include atât 1 cât și 100
print(numar)




for i in range(5):
    raspuns = int(input("La ce numar ma gandesc? "))
    if raspuns == numar:
        print("Felicitari ai gasit numarul la care ma gandesc!")

    elif raspuns < numar:
        print("Numarul la care ma gandesc e mai mare")
    elif raspuns > numar:
        print("Numarul la care ma gandesc e mai mic")

print("ai ramas fara vieti")