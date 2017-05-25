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
    import random
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
  import random
  global gDict
  whichEvent = (random.randint(0, len(events)-1))
  theEvent = list(events.keys())[whichEvent]
  print(("\tRandomExecution attempting to emit: "  + theEvent))
  gDict["fnRandomExecution"] = theEvent
  if theEvent != "Event_Win" and theEvent != "Event_Start" and theEvent != "Event_Boom":
    Emit(theEvent, whichEvent)
    Emit(theEvent, whichEvent)
  else:
    print("\t\tI aint emitting that!")
  print(gDict)
  
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
    AddListener('Event_Start', fnDynamite)
    AddListener('Event_Start', vowelLimiter)
    AddListener('Event_Boom', fnRandomExecution)
    
    # EXAMPLE: AddListener('Event_Example', fnExample)

    # DO NOT TOUCH
    Emit('Event_Start')
    print("No one won the game!");

if __name__ == "__main__":
    main()

