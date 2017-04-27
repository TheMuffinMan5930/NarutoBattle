def take_hp():
  """ Can only be used by DM """
  player_lose_hp = input("Which player would you like to take HP from?")
  try:
    exec(player_lose_hp + "HP -= 1")
  except:
    print("Not a player.")
    take_hp()

"""
if Player_Name = DM or DungeonMaster
  def TakeHP = raw_input("Which player would you like to take HP from?")
  if player = Player1
    Player1HP -= 1 #is this how you do it? NOAH!
  elif player = Player2
    Player2HP -= 1 # And so on and so on...
  else:
    print("Not a player")

  def SpawnEnemy(HP, Atk, Per, Ag, Def, Cha, Location) // double check this is the name of all of the stats
    print("An enemy has been spawned at $@, with #@ Health, #@ Attack, #@ Perception, #@ Agility, #@ Defense, and #@ Chakra!") (Location, HP, Atk, Per, Ag, Def, Cha)
  def Effect_Give //effect or affect?
    Effect_Given = raw_input("What effect would you like to give?")
      if Effect_Given = //Effect1 goes here
        Player1Status = Effect_Given
      elif Effect_Given = # //effect2 goes here
      
      # so on and so forth
"""    
    
  

  
