class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self, amount):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        self.hunger -= amount
        print(f"{self.name} has been fed.")

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
for i in range(3):
    my_pet.feed(1)
    print(f"Fluffy's hunger level: {my_pet.hunger}")