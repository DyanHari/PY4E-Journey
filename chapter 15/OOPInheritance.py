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

# Now let's create another class called FootBallFan which will inherit characteristics from PartyAnimal
class FootBallFan(PartyAnimal):

    # This constructor method initializes the FootBallFan object.
    # 'nam' is the parameter that will be passed for the name.
    def __init__(self, nam):
        # super().__init__(nam) calls the constructor of the parent class (PartyAnimal).
        # This sets up the name and initializes x to 0, just like in PartyAnimal.
        super().__init__(nam)
        self.points = 0  # Initialize points to 0

    # This method will increase points by 7, call the party method, and print the points.
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

# Create an instance of PartyAnimal with the name "Sally"
s = PartyAnimal("Sally")
s.party()  # Call the party method for Sally, increments x and prints the count
print("")

# Create an instance of FootBallFan with the name "Jim"
j = FootBallFan("Jim")
j.party()  # Call the party method for Jim, inherited from PartyAnimal
j.touchdown()  # Call the touchdown method for Jim, increments points, calls party, and prints points
