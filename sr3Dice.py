import math
import random

################################################################
# This file contains all the basic dice math-doing functions
#   that are used by the bot. Since this may be useful for
#   other projects separate from this specific Discord bot,
#   they have been entirely separated from the bot itself so as
#   to make them more easily portable/modifiable
################################################################

################################################################
# Just rolls a standard "exploding" d6
################################################################
def eD6(rollCap):
    result = random.randint(1,6)
    while( (result % 6 == 0) and (result < rollCap) ):
            result += random.randint(1,6)
    return result

################################################################
# Rolls an arbitrary number of "exploding" d6's up to a cap
#   as indicated by the value of rollCap
################################################################
def makeRoll(numDice, rollCap = 36):
    rawDice = []
    for roll in range(numDice):
        rawDice.append(eD6(rollCap))
    rawDice.sort(reverse = True)
    return rawDice

################################################################
# Calculates the number of standard "meets-or-beats" successes
#   on an array of integers representing dice rolls, as well as
#   the number of 1s rolled.
################################################################
def calcSuccesses(rawDice, targetNumber):
    successes = 0
    ruleOfOnes = 0
    for roll in rawDice:
        if(roll >= targetNumber):
            successes += 1
        elif(roll == 1):
            ruleOfOnes += 1
    return successes, ruleOfOnes

################################################################
# Performs a standard Shadowrun 3e Success Test
################################################################
def doSuccessTest(numDice, targetNumber, numComp = 0):
    if(targetNumber > 36):
        rawDice = makeRoll(numDice, targetNumber)
    else:
        rawDice = makeRoll(numDice)
    successes, ruleOfOnes = calcSuccesses(rawDice, targetNumber)
    glitchStatus = ''
    compDice = []
    if(successes == 0):
        if(ruleOfOnes == numDice):
            glitchStatus = 'Critical Glitch!'
        elif(ruleOfOnes > math.floor(numDice/2)):
            glitchStatus = 'Glitch!'
    elif(numComp > 0):
        compDice = makeRoll(numComp)
        compSuccesses = calcSuccesses(compDice, targetNumber)[0]
        successes += math.floor(compSuccesses/2)
    return (rawDice, compDice, glitchStatus, successes)

################################################################
# Performs a standard Shadowrun 3e Open Test
################################################################
def doOpenTest(numDice, rollCap = 120):
    rawDice = makeRoll(numDice, rollCap)
    result = max(rawDice)
    return rawDice, result
