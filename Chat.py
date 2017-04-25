import random

import gspread

from oauth2client.service_account import ServiceAccountCredentials

def ChatOverGSLow(name, Pasword):

    whlp_var = 1

    #put codein here that checks credentaisl

    while whlp_var == 1:
    
        ChatData = input(name + ": ")

        if ChatData.lower == "exit":
            whlp_var = 0

        else:
            wsChat.update_cell(1, 1, name + ": " + ChatData) 



def ChatOverGSHigh():

    ChatGetVal2 = wsChat.cell(1, 1).value

    while 1:

        ChatGetVal1 = wsChat.cell(1, 1).value

        if ChatGetVal1 != ChatGetVal2:
            print(ChatGetVal1)
            
        ChatGetVal2 = ChatGetVal1

        
