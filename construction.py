"""
Suppose you run a contruction company. Each house is built using the same hous plan as designed by the architect.
A drawing = class. The house = an instance of the class or object. House-oriented-bulding=Object-oriented-programming
Polymorphism -Ability of an object to take many forms
Inheritance -Child classes acquire properties from parent classes
Encapsulation - Protects data and methods from outside misuse by binding them together
Abstraction -Handles complexity by hiding unnecessary details from the user.
"""
class House:
    
    company_name = "Maryland Contruction Company"
    inflation_coefficient = 5
     # python constructor
    #a class with attributes
    #self keyword lets you know that a certain attribute changes from object to object.
    def __init__(self, address, town, alarm, price,street, bedrooms, bathrooms, square_footage):
        self.address = address
        self.town = town
        self.alarm = alarm
        self._price = price # Use _price as the private variable to avoid a name conflict with the property itself
        self.street = street
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_footage = square_footage
        self.completeAddress = f"{address} {street} {town}"
    
    def correctPriceMethod(self):
        self._price = self._price * self.inflation_coefficient

    def __str__(self):
        return f"House at {self.completeAddress}\n" \
               f"Price: Ksh.{self._price}\n" \
               f"Bedrooms: {self.bedrooms}\n" \
               f"Bathrooms: {self.bathrooms}\n" \
               f"Square Footage: {self.square_footage}\n" \
               
    @classmethod
    def set_inflation_coefficient(cls, new_coefficient):
        cls.inflation_coefficient = new_coefficient

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Price cannot be negative")

    def calculate_property_tax(self, tax_rate):
        #Calculate property tax based on the given tax rate.
        return(self._price * tax_rate) / 100
    
    def estimate_utility_cost(self):
        #Estimate utility cost based on square footage.
        return self.square_footage * 10 # Assuming Ksh.10 per square foot


house1 = House(1234, "Meru",False, 150000 ,"Forthstreet", 3, 2, 2000)
house2 = House(5432, "Nakuru", True, 225000, "Ngara road", 4, 3, 2500)


print(house1.address)
print(house1.town)
print(house1.alarm)

# Access and print the additional attributes
print(house1.bedrooms)
print(house1.bathrooms)
print(house1.square_footage)

print(house1.price)
house1.correctPriceMethod()
print(house1.price)
print(house1.street)
print(house1.completeAddress)

# Print the custom string representation
print(house1)

# Access and print the initial inflation_coefficient
print("Initial inflation_coefficient:", House.inflation_coefficient)

# Set a new inflation_coefficient using the class method
House.set_inflation_coefficient(6)

# Access and print the updated inflation_coefficient
print("Updated inflation_coefficient:", House.inflation_coefficient)

# Access and print the initial price using the getter method
print("Initial price:", house1.price)

# Set a new price using the setter method
house1.price = 160000

# Access and print the updated price using the getter method
print("Updated price:", house1.price)



# Calculate and print property tax for house1
property_tax_rate = 9  # Example tax rate (15%)
property_tax1 = house1.calculate_property_tax(property_tax_rate)
print(f"Property tax for house1: Ksh.{property_tax1}")

# Estimate and print utility cost for house2
utility_cost1 = house1.estimate_utility_cost()
print(f"Estimated utility cost for house1: Ksh.{utility_cost1}")

#expected output
#1234
#Meru
#False
#3
#2
#2000
#150000
#750000
#Forthstreet
#1234 Forthstreet Meru
#House at 1234 Forthstreet Meru
#Price: Ksh.750000
#Bedrooms: 3
#Bathrooms: 2
#Square Footage: 2000

#Initial inflation_coefficient: 5
#Updated inflation_coefficient: 6
#Initial price: 750000
#Updated price: 160000
#Property tax for house1: Ksh.14400.0
#Estimated utility cost for house1: Ksh.20000
