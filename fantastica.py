#!/usr/bin/python3
# A simple RPG game loosely based off "The Neverending Story"
import os
import sys
import pyfiglet
from time import sleep
import requests
import random

def clearScreen():
    #windows computers
    if os.name == 'nt':
        _ = os.system('cls')
    #linux/mac computers
    else:
        _ = os.system('clear')   
        
def showInstructions():
    #print the main menu and available commands
    print('''
        Welcome to The Neverending Story Game
        **************************************
        
        Commands:
            go [direction]
            get [item]
            look
            
        To display insructions:
            help
                
        To Quit Game:
            q
            quit
    ''')

def showStatus():
  # display the player's current status
  print('---------------------------')
  print('You are at the ' + currentLocation)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in locations[currentLocation]:
      # logic to print "an" or "a" depending on word
      if locations[currentLocation]['item'][0] in 'aeiou':
          print('You see an ' + locations[currentLocation]['item'])
      else:
          print('You see a ' + locations[currentLocation]['item'])
  print("---------------------------")

def showIntro():
    asciiIntro = pyfiglet.figlet_format("The Never Ending Story", font = "5lineoblique")
    print(asciiIntro)
    sleep(5)
    clearScreen()
    print('''
            Turn around, look at what you see...
            In her face, the mirror of your dreams...
            Make believe I'm everywhere, hidden in the lines...
            Written on the pages is the answer to a Never Ending Story...
            Ahhh Ahhh Ahhhhhhh Ahhh Ahhh Ahhhhhhh Ahhh Ahhh Ahhhhhhh
            A Never Ending Story......
          ''')
    print('''
            You are Atreyu, a Greenskin warrior from the Grassy Ocean in Fantastica.
            The Childlike Empress is dying and it is up to you, and you alone to find
            a cure. She left you with an Auryn, a powerful medallion to protect the 
            wearer from harm. Be careful what you wish for...
            
            Quickly now, the fate of Fantastica is in your hands! Off you go!
             ''')
    sleep(5)
    clearScreen()
    
    
# player inventory-starts with an Auryn
inventory = ["Auryn"]

#a dictionary linking a location to other locations
#TODO:make separate file for locations
locations = {
    'Grassy Ocean' : {
        'south' : 'Swamp of Sadness'
    },
    'Swamp of Sadness': {
        'north' : 'Grassy Ocean',
        'south' : 'No-Key Gate',
        'west' : 'Sea of Possibilities',
        'east' : 'Desert of Shattered Hopes',
        'item' : 'artax',
        'desc' : '''
        You are now surrounded by a barren swampland of quicksand-like mud pools. An 
        overwhelming sense of dread and sadness washes over you. Don't linger too long...
        '''
    },
    'Sea of Possibilities' : {
        'south' : 'Sphinx Gate',
        'east' : "Swamp of Sadness",
        'item' : 'mural',
        'desc' : '''
        Waves crash angrily on the rocky shores around you. The sky is dark and
        your mind is weary. Many paths lie ahead...a sea of possibilities...
        '''
    },
    'Desert of Shattered Hopes' : {
        'south' : 'Mirror Gate',
        'east' : 'Swamp of Sadness',
        'item' : 'gmork',
        'desc' : '''
        The ground is harsh and littered with broken promises and tears of sorrow. Tread carefully...
        Only scary beasts lie here...One visit is surely enough...
        '''
    },
    'Sphinx Gate' : {
        'north' : 'Sea of Possibilities',
        'south' : 'Crystal Cave',
        'east' : 'No-Key Gate',
        'item' : 'cat fact',
        'desc' : '''
        You see a tall, ornate gate with a golden yellow sphinx staring down at you.
        Her eyes glisten in the sun as she flicks her tail side to side...
        '''
    },
    'No-Key Gate' : {
        'north' : 'Swamp of Sadness',
        'south' : 'Ivory Tower',
        'east' : 'Mirror Gate',
        'west' : 'Sphinx Gate',
        'item' : 'clue',
        'desc' : '''
        You see a gate with no key? How to enter? Decide not to enter...
                    '''
    },
    'Mirror Gate' : {
        'north' : 'Desert of Shattered Hopes',
        'south' : 'Mountains of Destiny',
        'west' : 'No-Key Gate',
        'item' : 'mirror',
        'desc' : '''
        Another gate! This one seems different though.
        Everything appears SDRAWKCAB...
        '''
    },
    'Crystal Cave' : {
        'north' : 'Sphinx Gate',
        'east' : 'Ivory Tower',
        'item' : 'fortune',
        'desc' : '''
        Spelunking you are! The inter-play of sunlight, sea-water, and crystalline rock formations
        leave you speachless in this magical cavern. 
        '''
    },
    'Ivory Tower' : {
        'north' : 'No-Key Gate',
        'east' : 'Mountains of Destiny',
        'west' : 'Crystal Cave',
        'item' : 'geode',
        'desc' : '''
        You see the imperial capital of Fantastica--home of the Childlike Empress.
        Have you completed your quest? Atreyu, she is depending on you!
        Only you can bring her the cure before The Nothing swallows everything whole!
        '''
    },
    'Mountains of Destiny' : {
        'north' : 'Mirror Gate',
        'west' : "Ivory Tower",
        'item' : 'young child',
        'desc' : '''
        You are surrounded by towering vertical walls, sheer cliffs, and breath-taking beauty.
        In the distance you see the Wandering mountain, the highest point in all of Fantastica.
        '''
    }
}

#game starts at the 'Grassy Ocean'
currentLocation = 'Grassy Ocean'
# display intro to player
showIntro()
# display instructions to player
showInstructions()

# loop forever
while True:
    showStatus()

    #get the player's next 'move', .split() breaks it up into an list array
    #eg typing 'go east' would give the list: ['go','east']
    move = ''
    while move == '':
        move = input('> ')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    
    clearScreen() # clear the screen between moves
    
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in locations[currentLocation]:
            #set the current room to the new room
            currentLocation = locations[currentLocation][move[1]]
    #there is no door (link) to the new room
        else:
            print('You can\'t go that way! Try a different direction!')

    #if they type 'get' first
    if move[0] == 'get':    
        #if the room contains an item, and the item is the one they want to get (logic for all other items)
        if "item" in locations[currentLocation] and move[1] in locations[currentLocation]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the location
            del locations[currentLocation]['item'] 
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    #if they type 'look' first-display the location's description        
    if move[0] == 'look':
        if 'desc' in locations[currentLocation]:
            print(locations[currentLocation]['desc']) #print locations description
        else:
            print("Nothing to see here, move along...")
    
    #Secret command to use Falkor to teleport        
    if move[0] == 'call' and move[1] == 'luck dragon':
        newLocation = input("You summoned Falkor! Where would you like him to fly you to?\n> ")
        currentLocation = newLocation
        
   # display instructions if player needs help
    elif move[0] == 'help':
        showInstructions()
        
    #exit game if player wants to quit
    elif move[0] in ['q', 'quit']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass 
        

    #logic to save Artax!!
    if currentLocation == 'Swamp of Sadness' and 'artax' in inventory and 'Auryn' in inventory:
        print("A truly kind soul you are--you've saved Artax from the Swamp of Sadness.")
        print("This did not come without a price, you sacrificed your Auryn. Tread carefully...")
        inventory.remove('Auryn') # remove Auryn from inventory
        
    #logic for random cat fact if player has a cat fact in their inventory
    if currentLocation == 'Sphinx Gate' and 'cat fact' in inventory:
        url = "https://cat-fact.herokuapp.com/facts" #cat fact api
        response = requests.get(url).json() #get api response and convert to json
        catFacts = [] #empty list to hold the cat facts
        for fact in response:
            catFacts.append(fact.get("text")) #append each fact to the cat fact list
        print("\nThe mighty sphinx has blessed you with this random cat fact to guide you on your quest:\n", random.choice(catFacts))
    
    #Mirror Gate logic to reflect a phrase
    if currentLocation == 'Mirror Gate' and 'mirror' in inventory:
        answer = input("You have the mirror. Do you want to reflect a phrase? Y/N\n> ")
        if answer in ["Y", "y"]:
            phrase = input("Enter a phrase to reflect: ")
            reflected = phrase[::-1]
            print(reflected)
        elif answer in ["N", "n"]:
            print("Ok! Bye!")
        else:
            answer = input("Please enter Y or N\n> ")
          
    ## Define how a player can win
    if currentLocation == 'Ivory Tower' and 'young child' in inventory:
        print('You have brought a child, Bastian Balthazar Bux, to the Ivory Tower!')
        newName = input("Quick! What is the Empress' new name!\n> ").lower()
        if newName in ["moon child", "moonchild"]:
            print('''Congratulations! You saved Fantastica! 
              The Empress has presened you with a single grain of sand,
              the sole remnant of fantasia. You have the power to bring back Fantastica
              at any time with the power of your imagination.''')
            break
        else:
            newName = input("Hmmm...That's not quite right, try again.\n> ")

    ## If a player goes to location with Gmork
    elif 'item' in locations[currentLocation] and 'gmork' in locations[currentLocation]['item']:
        if 'Auryn' in inventory:
            print("Awooooooooo!!!! A wild Gmork has reared his head! Lucky for you, the Auryn protective powers saved you from an early demise!")
            print("But nothing in life is free, and your Auryn is gone, lost to the shards of shattered hopes and dreams.")
            inventory.remove("Auryn")
        else:
            print('GRRRRR!!! That wild wolf Gmork strikes again!! Bu this time you have no Auryn for protection. GAME OVER!!')
            break
