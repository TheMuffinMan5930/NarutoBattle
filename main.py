import random

import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Sheets_access.json', scope)
client = gspread.authorize(creds)

shFLFL = client.open('Falafel_Sheet')

wsChat = shFLFL.worksheet("Chat")

wsPlayers = shFLFL.worksheet("Players_&_Stats")



def NewPlayer(Player_Name, Level, AffinityList, Password):
   

 
class Person(Object): # Move to person.py
   def __init__(self, Player_Name, Level, AffinityList, Password):
      self.BaseStrength = random.randint(1 + Level, 6 * Level)
      self.BaseAgility = random.randint(1 + Level, 6 * Level)
      self.BasePerception = random.randint(1 + Level, 6 * Level)
      self.BaseChakra = random.randint(15 * Level, 30 * Level)
      self.BaseHp = random.randint(15 * Level, 30 * Level)
      self.name = Player_Name
      self.Level = Level
      self.AffinityList = AffinityList
      self.Password = Password
   #def __str__(self): # This code won't work and you probably don't need it.
   #   return {"Name": Player_Name, "Strength": BaseStrength, "Agility": BaseAgility, "Perception": BasePerception, "Chakra": BaseChakra, "Hp": BaseHp, "Afinity": AfinityList, "Password": Password}
   
print("To change any of these stats, you may access the dictionary storing this info by using these keywords:")
    print('"Name", "Strength", "Agility", "Perception", "Chakra", "Hp", "Afinity", or "Other"')
          

def UploadPlayer(playerVar):
   
   NewRow = 1

   ColVal = wsPlayers.col_values(1)

   for NewRow, NewRowVal in enumerate(ColVal):
      
      if NewRowVal == "":
         
         break
      
   wsPlayers.update_cell(NewRow + 1, 1, playerVar["Name"])
   wsPlayers.update_cell(NewRow + 1, 2, playerVar["Strength"])
   wsPlayers.update_cell(NewRow + 1, 3, playerVar["Agility"])
   wsPlayers.update_cell(NewRow + 1, 4, playerVar["Perception"])
   wsPlayers.update_cell(NewRow + 1, 5, playerVar["Chakra"])
   wsPlayers.update_cell(NewRow + 1, 6, playerVar["Hp"])
   wsPlayers.update_cell(NewRow + 1, 8, playerVar["Afinity"][0])
   wsPlayers.update_cell(NewRow + 1, 9, playerVar["Afinity"][1])
   wsPlayers.update_cell(NewRow + 1, 10, playerVar["Afinity"][2])
   wsPlayers.update_cell(NewRow + 1, 11, playerVar["Afinity"][3])
   wsPlayers.update_cell(NewRow + 1, 12, playerVar["Afinity"][4])
   wsPlayers.update_cell(NewRow + 1, 14, playerVar["Password"])
