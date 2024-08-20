petSpecies = input("Enter pet species: ")
age = int(input("Enter age of your pet: "))

if(petSpecies.lower() == "dog"):
    if(age < 2):
        petFood = "Puppy Food"
    else:
        petFood = "Dog Food"
elif(petSpecies.lower() == 'cat'):
    if(age > 5):
        petFood = "Senior Cat Food"
    else:
        petFood = "Milk and paste food"

print("For your pet the suitable food will be", petFood)