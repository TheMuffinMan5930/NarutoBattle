#This code is a modual that makes the task of rolling virtual die much easier

import random

def Roll(randlow, randhigh):
    #A simpler way to do random.randint
    return random.randint(randlow, randhigh)

def AdvantageRoll(AdvantageNumber, randlow, randhigh):
    
    #This modual is a die roller that rolls with advantage/ disadvantage
    #Positive AdvantageNumber means advantage, while Negative AdvantageNumber means disadvantage
    #The Abs AdvantageNumber is one more or less than (or the same) the number of dies rolled

    if AdvantageNumber > 0:
        
        RandRollADV1 = random.randint(randlow, randhigh)
        RandRollADV2 = random.randint(randlow, randhigh)
        
        while AdvantageNumber != 0:
            
            if RandRollADV1 == max(RandRollADV2, RandRollADV1):
                RandRollADV2 = random.randint(randlow, randhigh)
                
            else:
                RandRollADV1 = random.randint(randlow, randhigh)
                
            AdvantageNumber = AdvantageNumber - 1
            
        return max(RandRollADV2, RandRollADV1)
      
    elif AdvantageNumber < 0:
        
        RandRollADV1 = random.randint(randlow, randhigh)
        RandRollADV2 = random.randint(randlow, randhigh)
        
        while AdvantageNumber != 0:
            
            if RandRollADV1 == min(RandRollADV2, RandRollADV1):
                RandRollADV1 = random.randint(randlow, randhigh)
                
            else:
                RandRollADV2 = random.randint(randlow, randhigh)
                
            AdvantageNumber = AdvantageNumber + 1
            
        return min(RandRollADV1, RandRollADV2)

    else:

    #This else occurs only if the original AdvantageNumber is 0
        
        return DRoll(randlow, randhigh)

def AdvantageRoll20(ADVNum):
    #This is a simpler advantage roller using only a D20
    return AdvantageRoll(ADVNum, 1, 20)

def Roll20():
    #A simpler random generator for only D20s
    return DRoll(1, 20)
