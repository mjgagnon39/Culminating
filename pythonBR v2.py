#Python: Text Based Royale
from random import randint

#item list
'''
bigLaser = 10
mediumLaser = 11
smallLaser = 12
shieldPotion = 13
healthPotion = 14
'''
#Damage Values
'''
big laser = 100dmg 
medium laser = 50dmg
small laser = 25dmg
shield potion += 50 #Only if health is over 100 
healh potion += 50 #Only if health is under 100 
'''

#Location List


def locMenu():
	'''displays menu for locations'''
	print("Select a drop location")
	print("1. Togie Town")
	print("2. Stangie Skyscrapers")
	print("3. Luke's Landing")
	print("4. Kyle's Kingdom")
	

  


def itemRNG(dmg):
	''' a function determining what items you find'''
	item = randint(10, 12)

	if item == 10:
		print("You found a Big Laser!")
		#dmg = dmg + 100

	if item == 11:
		print("You found a Medium Laser")
    #dmg = dmg + 50
    
	if item == 12:
		print("You found a small laser")
    #dmg = dmg + 25
	
	

def menu ():
  '''function that displays the players actions'''
  print ("Select what you would like to do")
  print ("1. Fight an enemy nearby")
  print ("2. Heal")
  print ("3. Loot")
  print ("4. Move to the next area")
  
def fightMenu ():
  ''' a function that displays your options while in a fight'''
  print ("Select what you would like to do")
  print ("1. Shoot")
  print ("2. View Health")
  print ("3. View enemy Health")
  print ("4. Run Away")

health = 100
enemyHealth = 100
dmg = 0
for i in range(0, 1):
	locMenu()
	locChoice = input("Where we dropping boys?")
	

	if locChoice == "1":
		enemyCount = randint(1, 3)
		itemRNG(dmg)
		print("There are", enemyCount, "enemies around")

	elif locChoice == "2":
		enemyCount = randint(4, 8)
		itemRNG(dmg)
		print("There are", enemyCount, "enemies around")

	elif locChoice == "3":
		enemyCount = randint(1, 4)
		itemRNG(dmg)
		print("There are", enemyCount, "enemies around")

	elif locChoice == "4":
		enemyCount = randint(2, 8)
		itemRNG(dmg)
		print("There are", enemyCount, "enemies around")

while True:
  menu()
  actChoice = input("What would you like to do?")
  if actChoice == "1":
    while True: 
      fightMenu ()
      fightChoice = input("What would you like to do?")
      if fightChoice == "1":
        enemyHealth = enemyHealth - dmg 
      
