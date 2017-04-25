import gspread
Current_PLayer = get_current_player() # def this in main.py
Opponent = get_opponent() # def this as well
Jitsu_Player = sh.worksheet(Player_Name + "- Jitsus")
try:
  Jit1 = worksheet.acell(A2) # Go back and replace the coordinates with the correct coordinates.
  Jit2 = worksheet.acell(B2)
  Jit3 = worksheet.acell(C2)
  Jit4 = worksheet.acell(D2)
  Jit5 = worksheet.acell(E2)
  Jit6 = worksheet.acell(F2)
  Jit7 = worksheet.acell(G2)
except: # is there a tab here? 
  print("Error, Jitsu number does not match the number of Jitsus in program.")

confirmation_of_jitsus = input("Is it correct that you have #@, #@, #@, #@, #@, #@, #@ as your ttjitsus? Y/N").format(Jit1, Jit2, Jit3, Jit4, Jit5, Jit6, Jit7)
try:
  if confirmation_of_jitsus == Y
    BattleReady()
  elif confirmation_of_jitsus == N
    QuitGame() # Def this aswell 
except:
    print("Error")
