health = 100    # Health of Character, [Default Value: 100]
age = 60    # Age of Character

print("You have entered the Elderly Stage of your life.")   # The last stage of your life.

print("Tasks will now become harder and more physically demanding. After completing these tasks, you will have a chance to have a Heart Attack.")
print("Having a heart attack increases your chance of dying early. It may take years off you life, take away your max health, lower your health, or cause you to die instantly.")

print("You are now " + str(age) + " years old.")    # Displays the current age of your character.
print("You have " + str(health) + " health.")   # Displays the current health of your character.

# Health Costs
# If you don't purchase health insurance near the beggining stages of life you will have to pay a large fee depending on the accident.
 
heartAttack = 300    # Hospital fee.
carCrash = 1000  # Car crashes can lead to buying a new car, or paying for damage.
# If health < 25, you will die immediately. Otherwise you will have to pay a large fee depending on the damage to your body.

physicalTherapy = 100  # Physical therapy can lead to buying a new car

# Depending on what car you purchase, the more health it has. If you crash an expensive car you have to pay more to repair it.
# Elderly have a higher chance to get into car crashes based on your awareness or age.

# If you don't decide to continue driving, then you can hire people with your money. If you do not have a car or money you can decide to take a loan from the bank.

# Upper body health.
head = 100
neck = 100

leftArm = 100
rightArm = 100
chest = 100

stomache = 100
hip = 100

leftLeg = 100
rightLeg = 100

leftFoot = 100
rightFoot = 100
