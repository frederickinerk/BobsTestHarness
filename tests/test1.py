import logging


import context
import dataWrangler

import testDataDocFile
import testDataDocStorage

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
logger.info('test1: initialisation starting...')

def test1():
    logger.info("Running test 1")
    theContext = context.setContextObj(testDataDocFile)

    dataWrangler.makeOutput(theContext, "member", "member-root", "12345678")

    logger.info("test 1 complete")

    return True


test1()
