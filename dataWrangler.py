# Pieces together a response based on a name and input key
import logging

#import testDataDoc
import context

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler())
logger.info('dataWrangler: initialisation starting...')

def makeOutput(theContext, baseEntity, inputMsgName, inputKey):
    logger.info(f'dataWrangler: makeOutput entry - baseEntity - {baseEntity}')
    retStr = ""

    docObject = context.getPersistObj(theContext).getDocument(baseEntity, inputKey)
    mapObject = context.getPersistObj(theContext).getMappingDocument(inputMsgName)
    #templateObj = context.getPersistObj(theContext).getTemplateDocument(inputMsgName)

    logger.info(f'dataWrangler: makeOutput exit - result = "{retStr}"')

    return retStr


def getMappingObject(theContext, inputMsgName):

    return