# gremlin-bot
A simple Discord bot to allow users to make basic Shadowrun 3rd Edition-style dice tests

Here is a list of commands and their syntax:
1. ```$st [Number of Dice] [Target Number] [(optional) Number of Complementary Skill Dice]```  
      This command rolls a normal Shadowrun success test (that is, anything where you roll against a target number). If you don't have any complementary skill dice, just skip it and it will be ignored accordingly.

2. ```$ot [Number of Dice] [(optional) Highest necessary number]```  
      This command rolls a normal Shadowrun open test. Note that the second parameter (which is optional) only needs to be specified if you need to have maximum rolls that surpass the number 120, so should probably almost never be needed.
