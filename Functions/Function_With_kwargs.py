def printSupes(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printSupes(name = "Homelander", power = "Laser eyes")
printSupes(name = "Starlight")
printSupes(name = "A-Train", power = "Super speed", enemy = "Vought")