# AI has randomly generated stats with a total of 20 Skill points. each jitsu (it gets 4) is ranked from highest to lowest, with a class asigned to it.
# if statements determine what jitsu TYPE should be used, and the stats of jitsus are balanced from highest to lowest. AI randomly chooses 1
# each jitsu has a number attached to it, use 1, 2 and so on. Randomly selected in
# this section is turn 1, prints turn one stats, weapon used, and other things into log batch file or txt file for observation
# the ninjas take turns, each turn being logged, and the subsequent NOT global variables for their max health ect. 
# each turn is logged into file and winner is saved into file, with all stats. 
# while statement procedurely adds to number of ninjas with a while ... +1 to the number of ninjas. Each ninja has a higher number, 01, 02, 03 and so on.
i = 2
while i > 1:
    Ninja_(i) = AI_Ninjas(object)
class AI_Ninjas(object):
    def __init__(self):
            self.BaseStrength = random.randint(1 + Level, 6 * Level)
            self.BaseAgility = random.randint(1 + Level, 6 * Level)
            self.BasePerception = random.randint(1 + Level, 6 * Level)
            self.BaseChakra = random.randint(15 * Level, 30 * Level)
            self.BaseHp = random.randint(15 * Level, 30 * Level)
            self.jitsus = jitsus_for_(i)
    def __str__(self):s
    print(self.name)
    i += 1
    

