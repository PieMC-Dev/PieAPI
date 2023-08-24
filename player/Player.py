# this Player class is Broken Do not use/rely on
from piemc.player.Player import Player
class Player:
  Player.gamemode = gamemode
  Player.isOP = isOP
  Player.Health = 10
  Player.Hunger = 20
  
  def damaged():
    Player(Health = Player(Health) - 0.5)

def fatigued():
  if Player(Health == 1):
    Player.Fatigued = True
  if Player(Health == 1 && Hunger == 3):
    Player.Fatigued = True
    if Player(Hunger == 3):
    Player.Fatigued = True
    else
    Player.Fatigued = False

def isOP():
  if Player(PieMC.server.ops(Player)) == True:
    Player.isOP = True
    else
    Player.isOP = False
