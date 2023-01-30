import easygui as eg

health = 100  # Health of Character, [Default Value: 100]
age = 60  # Age of Character
money = 1000  # Money of Character, [Default Value: 100]
#################################################################################################################################################################################

# Dialog Boxes

print("You have entered the Elderly Stage of your life.")  # The last stage of your life.

print(
    "Tasks will now become harder and more physically demanding. After completing these tasks, you will have a chance to have a Heart Attack.")
print(
    "Having a heart attack increases your chance of dying early. It may take years off you life, take away your max health, lower your health, or cause you to die instantly.")

print("You are now " + str(age) + " years old.")  # Displays the current age of your character.
print("You have " + str(health) + " health.")  # Displays the current health of your character.
#################################################################################################################################################################################

# **MEDICAL AND HOSPITAL**

# If you don't purchase health insurance near the beginning stages of life you will have to pay a fee depending on the accident.

# Health Costs
heartAttack = 300  # Hospital fee.
carCrash = 1000  # Car crashes can lead to buying a new car, or paying for damage.
# If health < 25 before the accident, you will die immediately. Otherwise, you will have to pay a fee depending on the damage to your body.
physicalTherapy = 100  # Physical therapy can lead to buying a new car

# Depending on what car you purchase, the more health it has. If you crash an expensive car you have to pay more to repair it.
# Elderly have a higher chance to get into car crashes based on your awareness and reaction time.

# If you don't decide to continue driving, then you can hire people with your money. If you do not have a car or money you can decide to take a loan from the bank.

# If the health of your head or neck are less than 25 hp then you will suffer diminishing returns.
head = 100
neck = 100

# If the health of your arms are less than 25 hp then you will suffer diminishing returns.
leftArm = 100
rightArm = 100

# If the health of your chest, stomach, or hip is less than 25 hp then you will suffer diminishing returns.
chest = 100
stomach = 100
hip = 100

# If the health of your legs are less than 25 hp then you will suffer diminishing returns.
leftLeg = 100
rightLeg = 100

# If the health of your feet are than 25 hp then you will suffer diminishing returns.
leftFoot = 100
rightFoot = 100


#################################################################################################################################################################################
def groceryStore():
    global money  # Imports the global variable money to the grocery store function.

    # Purchasable items from the grocery store.

    # Produce Isle
    lettuce = 0
    onion = 0
    tomato = 0
    apple = 0
    orange = 0
    lemon = 0
    pear = 0
    grapes = 0
    peppers = 0
    pickles = 0
    carrot = 0
    potato = 0
    radish = 0
    squash = 0
    strawberry = 0
    blueberry = 0
    blackberry = 0
    squash = 0

    # Bakery Isle
    bread = 0
    bagel = 0
    baguette = 0
    donut = 0

    # Meats Isle
    chicken = 0
    beef = 0
    turkey = 0
    lamb = 0
    pork = 0

    # Seafood Isle
    shrimp = 0
    crab = 0
    clam = 0
    muscle = 0
    tilapia = 0
