####################################################
#                 RULES                            #
####################################################
#
# 1. Add one function on your turn
# 2. No touching of other functions
# 3. May only add listeners in main()
# 4. If the test run following your commit fails, you lose
# 5. If the test run following your commit calls the winEvent() function, you win
#

####################################################
#                 DONT TOUCH                       #
####################################################

# Seed the randomness so that each run is deterministic...sorta
import random
random.seed(7)

gDict = {}
events = {}
def winEvent(data):
    print("The game has been won!")
    exit()

def AddListener(event, fn):
    global events
    if event not in events:
        events[event] = []
    events[event].append(fn)

def Emit(e, data=None):
    if e in events:
        for event in events[e]:
            event(data)

####################################################
#                 Add Functions                    #
####################################################
def fnStart(data):
    print("Start!")

def fnDynamite(data):
    odds = (random.randint(1,100))
    if odds <= 20:
        print("Dynamite blew!")
        Emit("Event_Boom")

def vowelLimiter(data):
  vowelcount = 0;
  for key in gDict:
    vowelcount += key.lower().count('a')
    vowelcount += key.lower().count('e')
    vowelcount += key.lower().count('i')
    vowelcount += key.lower().count('o')
    vowelcount += key.lower().count('u')
    vowelcount -= key.lower().count('y')
  if vowelcount > 40:
    Emit('Event_Win')

def fnRandomExecution(data):
  global gDict
  whichEvent = (random.randint(0, len(events)-1))
  theEvent = sorted(list(events.keys()))[whichEvent]
  print(("\tRandomExecution attempting to emit: "  + theEvent))
  gDict["fnRandomExecution"] = theEvent
  if theEvent != "Event_Win" and theEvent != "Event_Start" and theEvent != "Event_Boom":
    Emit(theEvent, whichEvent)
    Emit(theEvent, whichEvent)
  else:
    print("\t\tI aint emitting that!")
  print(gDict)
  
gDict["hits"] = None
def fnShitGetsCrayFoSheezey(data):
  global gDict
  if gDict["hits"] is None:
    gDict["hits"] = 0
  gDict["hits"] += 1
  import string
  newRandos = random.randint(1,5)
  print("Creating " + str(newRandos) + " new DY NO MITE events! "
      + "Getting cray fo sheezey (iteration " + str(gDict["hits"]) + ")")
  for r in range(0, newRandos):
    rando = ''.join(random.choice(sorted(string.ascii_uppercase)) for _ in range(10))
    AddListener(rando, fnShitGetsCrayFoSheezey)
    AddListener(rando, fnDynamite)
    if ((gDict["hits"] > 10) and (random.randint(1,100) > 60)):
      print("\tSPECIAL BONUS!!! EVENT " + rando + " WINS!!!")
      AddListener(rando, winEvent)

def buildFortress(data):
  global gDict
  firstNames = ['Asen','Bomrek','Feb','Ingiz','Meng','Urdim','Olon','Kol','Vucar','Zaneg']

  lastNames  = ['Saziregul', 'Agmelbil', 'Medenlorbam', 'Umstizkadol', 'Dumnish', 'Songobok', 'Iloltar', 'Urdimoslan', 'Olinuker', 'Zaludatir']

  skills = ['Miner', 'Mason', 'Brewer', 'Cook', 'Grower', 'Fisherdwarf', 'Armorsmith', 'Metalsmith', 'Weaponsmith', 'Leatherworker',
            'Stone crafter', 'Wood crafter', 'Mechanic', 'Appraiser',  'Armor user', 'Axeman', 'Crossbowman', 'Dodger', 'Hammerman', 'Swordsman']

  wildlife = ['Bird', 'Elk', 'Carp', 'Turtle', 'Elephant', 'Earthworm', 'Cow', 'Moose', 'Lion', 'Polar bear',
              'Fox', 'Raven', 'Dog', 'Cat', 'Naked Mole Dog', 'Camel', 'Cheetah', 'Buzzard', 'Badger', 'Alligator']

  threats = ['Weregecko', 'Reacher', 'Ghost', 'Deamon', 'Dingo', 'Dragon', 'Giant Eagle', 'Vampire', 'Wolf', 'Fire Imp',
              'Beaver Man', 'Adder', 'Magma Crab', 'Carp', 'Troll', 'Bogeymen', 'Zombie', 'Miasma', 'Giant', 'Bryant']

  fortress = {}
  fortress['dwarves'] = {}
  # put everything in a sub-dictionary so not polute the global dictionary
  gDict['Fortress'] = fortress
  # make some dorfs
  for i in range(0, 100):
    name = 'Urist-' + firstNames[random.randint(0, 9)] + " " + lastNames[random.randint(0, 9)]
    fortress['dwarves'][name] = {'skills' : []}
    # give them some random skills
    for j in range(1, 14):
      skill = skills[random.randint(0,len(skills)-1)]
      # break into multiple calls so the aptitude is ceter weighted
      aptitude = random.randint(0,5) + random.randint(0,5) + random.randint(0,5) + random.randint(0,5)
      fortress['dwarves'][name]['skills'].append({skill: aptitude})

  # add some passive wildlife
  fortress['wildlife'] = []
  for i in range(0,70):
    fortress['wildlife'].append(wildlife[random.randint(0,len(wildlife)-1)])

  # make a few threats
  fortress['threats'] = []
  for i in range(0,20):
    fortress['threats'].append(threats[random.randint(0,len(threats)-1)])

# # Example:
# # NOTE: function must take a data argument, this could be any type
# def fnExample(data):
#   # NOTE: You can Emit() other events from your new function
#   # NOTE: We should make all event names in this format: "Event_<something>"
#   # NOTE: If event doesn't exist yet, this will fail!
#   Emit("Event_New", data?)

#   # NOTE: printing to screen
#   print("Example!")

####################################################
#                 Add Listeners                    #
####################################################
def main():
    AddListener('Event_Start', fnStart)
    AddListener('Event_Win', winEvent)
    
    # ONLY ADD/MOVE LISTERNS UNDER HERE!
    AddListener('Event_Start', buildFortress)
    AddListener('Event_Start', fnShitGetsCrayFoSheezey)
    AddListener('Event_Start', fnDynamite)
    AddListener('Event_Start', vowelLimiter)
    AddListener('Event_Boom', fnRandomExecution)
    
    # EXAMPLE: AddListener('Event_Example', fnExample)

    # DO NOT TOUCH
    Emit('Event_Start')
    print("No one won the game!");

if __name__ == "__main__":
    main()

