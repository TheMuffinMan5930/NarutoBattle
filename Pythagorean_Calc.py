import gspread

import math

import random

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Sheets_access.json', scope)
client = gspread.authorize(creds)

shFLFL = client.open('Falafel_Sheet')

shJS = client.open('Jitsus')

flChat = shFLFL.worksheet("Chat")

flPlayers = shFLFL.worksheet("Players_&_Stats")

jsFormat = shJS.worksheet("Format")



def calc_diag_dist(rowSq1, colSq1, rowSq2, colSq2):

    # Sq1 is the starting position
    # Sq2 is the ending position

    deltaRow = rowSq1 - rowSq2
    deltaCol = colSq1 - colSq2
    Pythag = abs(deltaRow) ** 2 + abs(deltaCol) ** 2
    return math.sqrt(Pythag)



def auto_calc_dist(begin_point, end_point):
    cell1 = jsFormat.find(begin_point)
    cell2 = jsFormat.find(end_point)
    return calc_diag_dist(cell1.row, cell1.col, cell2.row, cell2.col)



def CircleRand(radius):

    ListCord = []
    radiusSquare = radius ** 2
    x = 0
    
    while x < 25 * radius:

        cellsUp = random.uniform(0.0, radius)
        cellsOver = random.uniform(0.0, radius)
        
        if round(cellsUp ** 2 + cellsOver ** 2, 0) == radiusSquare:
            ListCord.append([cellsUp, cellsOver])
            x = x + 1
              
    return ListCord



def CircleEvery(radius):

    ListCord = []
    radiusSquare = radius ** 2
    cellsUp = 0.0
    cellsOver = 0.0
    
    while cellsOver < radius:

        if round(cellsUp ** 2 + cellsOver ** 2, 0) == radiusSquare:
            ListCord.append([cellsUp, cellsOver])
                
        if cellsUp >= radius:
            cellsUp = 0
            cellsOver = cellsOver + 0.1

        else:
            cellsUp = cellsUp + 0.1
        
    return ListCord


def Avg_Circle(lst):

    for i in lst:
        
        i[0] = int(round(i[0], 0))
        i[1] = int(round(i[1], 0))

    return lst



def Draw_Points(plst, pointupover):

    for i in plst:
        jsFormat.update_cell(i[0] + 1 + pointupover[0], i[1] + 1 + pointupover[1], "*")


def DrawCirE(rad, pdown, pover):
    Draw_Points(Avg_Circle(CircleEvery(rad)), [pdown, pover])



def DrawCirR(rad, pdown, pover):
    Draw_Points(Avg_Circle(CircleRand(rad)), [pdown, pover])


def MakeCirFull(lst):

    lst2 = []

    for o in lst:
        lst2.append([o[0], o[1]])
    
    for i in lst:
        lst2.append([i[0] * -1, i[1]])

    for a in lst:
        lst2.append([a[0], a[1] * -1])

    for b in lst:
        lst2.append([b[0] * -1, b[1] * -1])

    return lst2



def DrawCirFull(rad, pdown, pover):
    Draw_Points(MakeCirFull(Avg_Circle(CircleEvery(rad))), [pdown, pover])
            
           
