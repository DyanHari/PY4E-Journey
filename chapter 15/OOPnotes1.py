class PartyAnimal:

    # This constructor method initializes the object. The object will now require one parameter, which is the name (z).
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, 'constructed')

    # This method will not just count but also print the name of the object that called it.
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

# Creating an instance of PartyAnimal with the name "Sally" and calling the party method.
s = PartyAnimal("Sally")
s.party()
print("")

# Creating another instance of PartyAnimal with the name "Jim" and calling the party method.
j = PartyAnimal("Jim")
j.party()
print("")

# Calling the party method again on the "Sally" instance.
s.party()
