def sumar(*args: list):
    return sum(args)


print(sumar(1, 2))
print(sumar(1, 2, 3))


def saludar(**kwargs):
    if kwargs["tiempo"] == "mañana":
        print("Buenos dias,", end=" ")
    if kwargs["tiempo"] == "tarde":
        print("Buenas tardes,", end=" ")
    if kwargs["tiempo"] == "noche":
        print("Buenas noches,", end=" ")

    print(kwargs["persona"])


saludar(tiempo="mañana", persona="Luca")
saludar(persona="Maria", tiempo="noche")
