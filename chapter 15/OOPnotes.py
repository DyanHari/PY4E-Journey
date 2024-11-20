#lets create a class called Party Animal
class PartyAnimal:
    #This function is called the constructor method. This will run we if create an object derived from the class.
    #example a = PartyAnimal() meaning this method will be called.
    def __init__(self):
        # 'self' is like saying 'this object'. It lets you work with the specific instance you're creating.
        # 'self.x' means the variable 'x' that belongs to this particular object.
        self.x = 0
        print('I am constructed')

    #now this method is like one of the characteristics of the PartyAnimal class that we created
    def party(self):
        #the function of this method is to increment the value of the self or x everytime we call it and it will also print
        #So far
        self.x = self.x + 1
        print("So far", self.x)

    #now this is what we called the destructor method. Everytime we overwrite the variable that we assign the class to.
    #this block of code will execute
    def __del__(self):
        print('I am destructed', self.x)


#now lets pass the characteristics of PartyAnimal to an
an = PartyAnimal()

#now an can use the method party inside the PartyAnimal class
an.party()

#now lets check what type of variable now is an
print("type: ", type(an))

#now lets check what are the characteristics of an or what it can do
print("Dir: ", dir(an))

#now lets find out about what is an.party()
print("type: ", type(an.party))

#now lets find out about what is an.x
print("type: ", type(an.x))

#now lets check if the deconstructor will work if we overwrite the variable an to be an int now
an = 43
print('an is', an)