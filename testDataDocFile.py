# Get the test document that matches the doc type and key

import json
import logging
import csv

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler())
logger.info('testDataDocFile: initialisation starting...')

def getDocument(baseEntity, theKey):
    logger.info('testDataDocFile: Entry - getDocument for baseEntity: ' + baseEntity + ' with key ="' + theKey + '"')

    filename = f'data/data-{baseEntity}-{theKey}.json'
    logger.info(f'testDataDocFile: getDocument filename = "{filename}"')
    with open(filename) as json_file:
        doc = json.load(json_file)
        logger.info(f'testDataDocFile: getDocument loaded {str(doc)}')

    logger.info('testDataDocFile: getDocument Exit')
    return doc

def getMappingDocument(msgType):
    logger.info(f'testDataDocFile: getMappingDocument for msgType: {msgType}')

    mapDoc = ""

    filename = f'data/mapping-{msgType}.csv'
    logger.info(f'testDataDocFile: getMappingDocument filename = "{filename}"')
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            for key in row.keys():
                print(f'row[{str(line_count)} ][{key}] = {str(row[key])}')
            line_count += 1
        print(f'Processed {line_count} lines.')
        
        #logger.info('testDataDocFile: getDocument loaded ' + str(doc))

    logger.info('testDataDocFile: getMappingDocument Exit')

    return mapDoc

def getTemplateDocument(msgType):
    logger.info(f'testDataDocFile: getTemplateDocument for msgType: {msgType}')

    templateDoc = ""

    filename = f'data/template-{msgType}.json'
    logger.info(f'testDataDocFile: getTemplateDocument filename = "{filename}"')

    with open(filename) as json_file:
        templateDoc = json.load(json_file)
        logger.info(f'testDataDocFile: getTemplateDocument loaded {str(templateDoc)}')

    logger.info('testDataDocFile: getTemplateDocument Exit')

    return templateDoc
