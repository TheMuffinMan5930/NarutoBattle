# The goal of this program is to begin automation of random rolls, and imput formulas
import random

import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Sheets_access.json', scope)
client = gspread.authorize(creds)

shFLFL = client.open('Falafel_Sheet')

wsChat = shFLFL.worksheet("Chat")

wsPlayers = shFLFL.worksheet("Players_&_Stats")

Player1_Name = ""
Player2_Name = ""
Player3_Name = ""
Player4_Name = ""
Player5_Name = ""
Player6_Name = ""

def NewPlayer1(Player1_Name, Level1, AfinityList1):
    
    print("Hello, " + Player_Name)
    
    BaseStrength = random.randint(1 + Level, 6 * Level)
    BaseAgility = random.randint(1 + Level, 6 * Level)
    BasePerception = random.randint(1 + Level, 6 * Level)
    BaseChakra = random.randint(15 * Level, 30 * Level)
    BaseHp = random.randint(15 * Level, 30 * Level)

    print("Strength: {} \nAgility: {} \nPerception: {} \nChakra: {} \nHp: {}".format(BaseStrength, BaseAgility, BasePerception, BaseChakra, BaseHp))

    BaseP1Char = {"Strength": 
    
    return 

def NewPlayer2(Player2_Name, Level2, AfinityList2):
    
    print("Hello, " + Player2_Name)
    
    BaseStrength2 = random.randint(1 + Level2, 6 * Level2)
    BaseAgility2 = random.randint(1 + Level2, 6 * Level2)
    BasePerception2 = random.randint(1 + Level2, 6 * Level2)
    BaseChakra2 = random.randint(15 * Level2, 30 * Level2)
    BaseHp2 = random.randint(15 * Level2, 30 * Level2)

    print("Strength: {} \nAgility: {} \nPerception: {} \nChakra: {} \nHp: {}".format(BaseStrength2, BaseAgility2, BasePerception2, BaseChakra2, BaseHp2))


def NewPlayer3(Player3_Name, Level3, AfinityList3):
    
    print("Hello, " + Player3_Name)
    
    BaseStrength3 = random.randint(1 + Level3, 6 * Level3)
    BaseAgility3 = random.randint(1 + Level3, 6 * Level3)
    BasePerception3 = random.randint(1 + Level3, 6 * Level3)
    BaseChakra3 = random.randint(15 * Level3, 30 * Level3)
    BaseHp3 = random.randint(15 * Level3, 30 * Level3)

    print("Strength: {} \nAgility: {} \nPerception: {} \nChakra: {} \nHp: {}".format(BaseStrength3, BaseAgility3, BasePerception3, BaseChakra3, BaseHp3))


def NewPlayer2(Player4_Name, Level4, AfinityList4):
    
    print("Hello, " + Player4_Name)
    
    BaseStrength4 = random.randint(1 + Level4, 6 * Level4)
    BaseAgility4 = random.randint(1 + Level4, 6 * Level4)
    BasePerception4 = random.randint(1 + Level4, 6 * Level4)
    BaseChakra4 = random.randint(15 * Level4, 30 * Level4)
    BaseHp4 = random.randint(15 * Level4, 30 * Level4)

    print("Strength: {} \nAgility: {} \nPerception: {} \nChakra: {} \nHp: {}".format(BaseStrength4, BaseAgility4, BasePerception4, BaseChakra4, BaseHp4))


def NewPlayer2(Player5_Name, Level5, AfinityList5):
    
    print("Hello, " + Player5_Name)
    
    BaseStrength5 = random.randint(1 + Level5, 6 * Level5)
    BaseAgility5 = random.randint(1 + Level5, 6 * Level5)
    BasePerception5 = random.randint(1 + Level5, 6 * Level5)
    BaseChakra5 = random.randint(15 * Level5, 30 * Level5)
    BaseHp5 = random.randint(15 * Level5, 30 * Level5)

    print("Strength: {} \nAgility: {} \nPerception: {} \nChakra: {} \nHp: {}".format(BaseStrength5, BaseAgility5, BasePerception5, BaseChakra5, BaseHp5))


def NewPlayer2(Player6_Name, Level6, AfinityList6):
    
    print("Hello, " + Player6_Name)
    
    BaseStrength6 = random.randint(1 + Level6, 6 * Level6)
    BaseAgility6 = random.randint(1 + Level6, 6 * Level6)
    BasePerception6 = random.randint(1 + Level6, 6 * Level6)
    BaseChakra6 = random.randint(15 * Level6, 30 * Level6)
    BaseHp6 = random.randint(15 * Level6, 30 * Level6)

    print("Strength: {} \nAgility: {} \nPerception: {} \nChakra: {} \nHp: {}".format(BaseStrength6, BaseAgility6, BasePerception6, BaseChakra6, BaseHp6))

def UploadPlayer1():

    print("Uploading...")
    wsPlayers.update_cell(2, 2, BaseStrength1)
    print("Finished STR")
    wsPlayers.update_cell(2, 3, BaseAgility1)
    print("Finished AGL")
    wsPlayers.update_cell(2, 4, BasePerception1)
    print("Finished PER")
    wsPlayers.update_cell(2, 5, BaseChakra1)
    print("Finished CHA")
    wsPlayers.update_cell(2, 6, BaseHp1)
    print("Finished HP")

    print("Upload Complete")

def UploadPlayer(PlayerName):
    
    if PlayerName == Player1_Name:
        UploadPlayer1()
    elif PlayerName == Player2_Name:
        print("B")
    elif PlayerName == Player3_Name:
        print("C")
    elif PlayerName == Player4_Name:
        print("D")
    elif PlayerName == Player5_Name:
        print("E")
    elif PlayerName == Player6_Name:
        print("F")
    else:
        print("Hmmm, That name doesnt corespond to any players.\nHeres a list of all player names: \n{}, {}, {}, {}, {}, {}.".format(Player1_Name, Player2_Name, Player3_Name, Player4_Name, Player5_Name, Player6_Name)) 
