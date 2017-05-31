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
    if odds <= 1120:
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

''' Hash gDict keys and values'''
def HashThisShit(data):
    # Python hashing module
    import hashlib
    global gDict 

    # Add encryption tag to gDict
    gDict["encrypted"] = True
    tempDict = {}

    # Hash every key in the dictionary to confuse everyone!
    for k in gDict:
        tempDict[hashlib.sha512(k.encode('utf-8')).hexdigest()] = hashlib.sha512(str(gDict[k]).encode('utf-8')).hexdigest()
    
    # Overwrite dictionary with new, hashed one
    gDict = tempDict

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
    AddListener('Event_Start', fnShitGetsCrayFoSheezey)
    AddListener('Event_Start', fnDynamite)
    AddListener('Event_Start', HashThisShit)
    AddListener('Event_Start', vowelLimiter)
    AddListener('Event_Boom', fnRandomExecution)
    

    # EXAMPLE: AddListener('Event_Example', fnExample)

    # DO NOT TOUCH
    Emit('Event_Start')
    print("No one won the game!");

if __name__ == "__main__":
    main()

