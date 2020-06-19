#!/bin/python3
import datetime
import discord
import os
import sr3Dice
from dotenv import load_dotenv
from discord.ext import commands

################################################################
# Initial bot configuration
################################################################

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')
client = discord.Client()

@bot.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


################################################################
# The 'st' command
################################################################
@bot.command(name='st', help='Rolls a standard Shadowrun 3e success test.')
async def rollSuccessTest(ctx, *args):
    #Basic input validation
    if(len(args) not in [2,3]):
        print(str(datetime.datetime.now())+'--> ERROR: Invalid number of arguments.')
        return
    try:
        numDice = int(args[0])
        targetNum = int(args[1])
        if(targetNum < 2):
            targetNum = 2
        numComp = 0
        if(len(args) == 3):
            numComp = int(args[2])
    except:
        print(str(datetime.datetime.now())+'--> ERROR: Invalid input values.')
        return
    rawDice, compDice, glitchStatus, successes = sr3Dice.doSuccessTest(numDice, targetNum, numComp)
    resultString = 'Rolling a Success Test with...\n'
    #Format the results for the base and (if applicable) complementary rolls in a code block
    resultString += 'Dice: '+str(numDice)
    resultString += '\n`'+', '.join(map(str, rawDice))+'`\n'
    if(numComp > 0 and successes > 0):
        resultString += 'Complementary Dice: '+str(numComp)+'\t'
        resultString += '\n`'+', '.join(map(str, compDice))+'`\n'
    #Print the target number on its own line after the rolls are displayed
    resultString += 'Target Number: '+str(targetNum)+'\n'
    #Follow with a line containing the number of successes, or - if the roll is a glitch - the glitchStatus
    if(glitchStatus == ''):
        resultString += 'Successes: '+str(successes)
    else:
        resultString += glitchStatus
    #Send result to the command line
    await ctx.send(resultString)

################################################################
# The 'ot' command
################################################################
@bot.command(name='ot', help='Rolls a standard Shadowrun 3e open test.')
async def rollOpenTest(ctx, *args):
    #Basic input validation
    if(len(args) not in [1,2]):
        print(str(datetime.datetime.now())+'--> ERROR: Invalid number of arguments.')
        return
    rollCap = 0
    try:
        numDice = int(args[0])
        if(len(args) == 2):
            rollCap = int(args[1])
    except:
        print(str(datetime.datetime.now())+'--> ERROR: Invalid input values.')
        return
    if(rollCap > 0):
        rawDice, highRoll = sr3Dice.doOpenTest(numDice, rollCap)
    else:
        rawDice, highRoll = sr3Dice.doOpenTest(numDice)
    resultString = 'Rolling an Open Test with...\n'
    #Format the results for the base in a code block
    resultString += 'Dice: '+str(numDice)
    resultString += '\n`'+', '.join(map(str, rawDice))+'`\n'
    resultString += 'Result: '+str(highRoll)
    await ctx.send(resultString)

################################################################
# Actually running the bot
################################################################
bot.run(TOKEN)
