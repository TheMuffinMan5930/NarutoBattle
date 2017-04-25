import gspread
Jitsu_Player = sh.worksheet(Player_Name + "- Jitsus")
i = 1
while True:
  exec("Jit" + i + " = worksheet.acell(" + i.string.ascii_uppercase.index(i - 1) + "2)")
  i += 1
confirmation_of_jitsus = input("Is it correct that you have #@, #@, #@, #@, #@, #@, #@ as your ttjitsus? Y/N").format(Jit1, Jit2, Jit3, Jit4, Jit5, Jit6, Jit7)
try:
  if confirmation_of_jitsus == Y
    BattleReady()
  elif confirmation_of_jitsus == N
    QuitGame() # Def this aswell 
except:
    print("Error")
