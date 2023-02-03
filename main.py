# Future versions of LifeSim will add more items and features!

# ToADD: Menus, Gui, Inventory, Shops, Grammar Checks & Typos, More Stores, Item, Food Recipes, Body Health System, etc.

import easygui as eg
from easygui import *

health = 100  # Health of Character, [Default Value: 100]
age = 60  # Age of Character
money = 1000  # Money of Character, [Default Value: 1000]


# ------------------------------------------------------------------------------------------#

# Title Screen

def titleIntro():  # Welcome page explaining the current stage of life.
    global money, age, health
    title = "LifeSim (1.0.0) - Welcome to the Elderly Stage of Life"  # Title of Dialog Box, [Default Value: "LifeSim"]
    # Displays Stats of Character + Dialog
    stats = "\t\tYou have entered the Elderly Stage of your life.\n\t" \
            + "    Tasks will now become harder and more physically demanding.\n" \
            + "|------------------------------------------------------------------------------|" \
            + "\n\n\t\t\t\tMoney: $" + str(money) \
            + "\n\t\t\t\tHealth: " + str(health) + ' ' \
            + "hp" + "\n\t\t\t\tAge: " + str(age) + " years"
    eg.msgbox(stats, title, )


titleIntro()
print("titleIntro")


def titleHealth():  # Page explaining new challenges
    title = "LifeSim (1.0.0) - New Challenges "  # Title of Dialog Box, [Default Value: "LifeSim"]

    stats = "\t\t\t\tNew Challenges\n\n" \
            + " Heart Attacks - Having a heart attack increases your chance of dying early." \
            + " It may take years off your life, take away your max health, lower your health, or cause you to die instantly.\n\n" \
            + " Dementia - causes you to forget your tasks easier.\n\n" \
            + " Prone to illness - You catch illnesses faster & diseases last longer.\n\n" \
            + " Weak Joints - You are now unable to perform physically demanding activities.\n\n" \
            + " Decreased Awareness - Prone to more accidents & clumsiness."
    eg.msgbox(stats, title)


titleHealth()
print("titleHealth")


def titleLimbs():  # Page explaining the health system
    title = "LifeSim (1.0.0) - New Health System"

    stats = "\t\t\t\tNew Health System\n\n" \
            + " A new health system has been implemented into the game!" \
            + " All limbs now have their own health, and" \
            + " it is now possible to break or hurt limbs." \
            + " When you hurt a limb you can't perform certain tasks." \
            + " \n\nFor example, if you break a bone you can go to the hospital to get it fixed."
    eg.msgbox(stats, title)


titleLimbs()
print("titleLimbs")


def houseStarter():
    title = "HouseStarter"
    msgbox("Good luck!\n"
           + "If this project continues, there will be many more updates.\n"
           "You will be starting in your house.")


houseStarter()


def houseTransportMenu():
    pass


houseTransportMenu()


def houseRooms():  # Allows you to locate to different rooms in your house.
    pass


# ------------------------------------------------------------------------------------------#

# **MEDICAL AND HOSPITAL**

# If you don't purchase health insurance near the beginning stages of life you will have to pay a fee depending on the accident.

# Health Costs
hospitalVisit = 500  # Hospital fee.

physicalTherapy = 200  # Physical Therapy fee.
# Physical therapy can lead to a minor to major health increase after an accident.

doctorsOffice = 150  # A doctor's checkup can lead to the discovery of a(n) unknown disease or injury.

# Depending on what car you purchase, the more health it has. If you crash an expensive car you have to pay more to repair it.
# Elderly have a higher chance to get into car crashes based on your awareness and reaction time.

carAccident = 100  # Car crashes can lead to buying a new car, or paying for damage.
# If health < 25 before the accident, you will die immediately.
# Otherwise, you will have to pay a fee depending on the damage to your body.

# If you don't decide to continue driving, then you can hire people with your money.
# If you do not have a car or money you can decide to take a loan from the bank.

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


# ------------------------------------------------------------------------------------------#

def groceryStore():  # Saving for future use. | Can be used in other stages of life.
    global money  # Imports the global variable money to the grocery store function.

    # ____ = 0 ?   0 = placeholder price

    # Purchasable items from the grocery store.

    # ---------------------------------------------#

    # Drinks & Liquids Isle {

    # Liquids {
    water = 0
    lemonJuice = 0
    limeJuice = 0

    # ---------------------------------------------#

    # Produce Isle

    # Vegetables {
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

    # ---------------------------------------------#

    # Bakery Isle

    # Breads {
    bread = 0
    bagel = 0
    baguette = 0
    donut = 0

    # Grain {
    wheat = 0
    flour = 0
    oats = 0
    rice = 0
    barley = 0

    # ---------------------------------------------#

    # Meats Isle

    # Meat {
    chicken = 0
    beef = 0
    turkey = 0
    lamb = 0
    pork = 0

    # ---------------------------------------------#

    # Seafood Isle

    # Crustaceans {
    shrimp = 0
    crab = 0
    clam = 0
    muscle = 0
    lobster = 0

    # Fish & Misc {
    tilapia = 0
    squid = 0
    octopus = 0
    salmon = 0
    sardine = 0
    trout = 0
    grouper = 0

    # ---------------------------------------------#

    # Spice Isle

    # Spices {
    salt = 0
    pepper = 0
    basil = 0
    cumin = 0
    garlicPowder = 0
    thyme = 0
    cinnamon = 0
    chiles = 0
    cloves = 0
    driedHerbs = 0
    fennel = 0
    ginger = 0
    mustardSeed = 0
    vanilla = 0

    # ---------------------------------------------#

    # Dairy Isle

    # Dairy {
    milk = 0
    eggs = 0
    butter = 0
    creamer = 0
    dehydratedMilk = 0

    # Cheese {
    parmesan = 0
    threeCheeseBlend = 0
    cheddar = 0
    mozzerella = 0

    # ---------------------------------------------#

    # Pasta Isle

    # Pasta {
    angelHair = 0
    speghetti = 0
    elbow = 0
    bowtie = 0

    # Sauce {
    redSauce = 0

    # ---------------------------------------------#
