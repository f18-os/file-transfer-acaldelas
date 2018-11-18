from sys import argv
import sys, re

progName = "()"
if len(argv):
    progName = argv[0]
    del argv[0]

switchesVarDefaults = ()

def parseParams(_switchesVarDefaults):
    global switchesVarDefaults
    paramMap = {}
    switchesVarDefaults = _switchesVarDefaults
    swVarDefaultMap = {}       # map from cmd switch to param var name
    for switches, param, default in switchesVarDefaults:
        for sw in switches:
            swVarDefaultMap[sw] = (param, default)
        paramMap[param] = default # set default values
    try:
        while len(argv):#This will go through the arguments deleting them.. and mapping
            print("Printing the sw val")
            sw = argv[0]; del argv[0]
            print(sw)
            #Deletes the first argument and assigns it to sw for now
            #paramVar has the params we entered and defaultval is what is going to be changed
            #which is picked from an associative array
            
            if (defaultVal):
                val = argv[0]; del argv[0]
                #delete the arg and change the mapped value to the new one
                #Only works on the non-boolean if we see that we are changing the map for
                #a boolean then just assume it's true
                paramMap[paramVar] = val
            else:
                paramMap[paramVar] = True
    except Exception as e:
        print("Problem parsing parameters (exception=%s)" % e)
        usage()
    return paramMap #returns an dictionary 
        
def usage():
    print("%s usage:" % progName)
    for switches, param, default in switchesVarDefaults:
        for sw in switches:
            if default:
                print(" [%s %s]   (default = %s)" % (sw, param, default))
            else:
                print(" [%s]   (%s if present)" % (sw, param))
    sys.exit(1)

