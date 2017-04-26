import random

import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Sheets_access.json', scope)
client = gspread.authorize(creds)

shFLFL = client.open('Falafel_Sheet')

wsChat = shFLFL.worksheet("Chat")

wsPlayers = shFLFL.worksheet("Players_&_Stats")



def NewPlayer(Player_Name, Level, AfinityList, Other):

# Used to create a new player
   

    # This code isnt necisary at the moment, I need to learn about global variable... (and classes...)
                 
    # Afinity should be in order of most afinity to least afinity
    
    print("Hello, " + Player_Name)
    
    BaseStrength = random.randint(1 + Level, 6 * Level)
    BaseAgility = random.randint(1 + Level, 6 * Level)
    BasePerception = random.randint(1 + Level, 6 * Level)
    BaseChakra = random.randint(15 * Level, 30 * Level)
    BaseHp = random.randint(15 * Level, 30 * Level)

    print("Strength: {} \nAgility: {} \nPerception: {} \nChakra: {} \nHp: {}".format(BaseStrength, BaseAgility, BasePerception, BaseChakra, BaseHp))

    print("To change any of these stats, you may access the dictionary storing this info by using these keywords:")
    print('"Name", "Strength", "Agility", "Perception", "Chakra", "Hp", "Afinity", or "Other"')
          
    playerVar = {"Name": Player_Name, "Strength": BaseStrength, "Agility": BaseAgility, "Perception": BasePerception, "Chakra": BaseChakra, "Hp": BaseHp, "Afinity": AfinityList, "Other": Other}
    
    # When you learn about classes, this can be replaced with a global variable




'''def AutoPlayer(NP):
      NewP_Num = 0
    x = 1
    while x == 1:
        try:
            exec('var21 = NewPlr_{}["Strength"]'.format(NewP_Num))
            NewP_Num = NewP_Num + 1
            
        except NameError:
            x = 0'''

# use this instead of updating that other code, just create a new subrutine

def UploadPlayer(playerVar):
   sh.get_worksheet(0)
   i = 1
   While True:
      wsPlayers.update_acell(1 , 2 + i, Player_Name)
      wsPlayers.update_acell(2 , 2 + i, BaseStrength)
      wsPlayers.update_acell(3 , 2 + i, BaseAgility)
      wsPlayers.update_acell(4 , 2 + i, BasePerception)    
      wsPlayers.update_acell(5 , 2 + i, BaseChakra)
      wsPlayers.update_acell(6 , 2 + i, BaseHp)
      wsPlayers.range.update_acell('H2:L2', AffinityList)
      Password = input("What would you like to set as your password?")
      wsPlayers.update_acell
      i += 1
   
