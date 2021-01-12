# allow test mode or real mode. Context determines what is active

def setContextObj(dataObj):

    theContext = {}
    theContext['persistObj'] = dataObj
    
    return theContext

def getPersistObj(theContext):
    return theContext['persistObj']

