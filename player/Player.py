from piemc.player.Player import Player
class Player:
  Player.gamemode = gamemode
  Player.isOP = isOP
  Player.Health = 10
  Player.Hunger = 20
  
  def damaged():
    Player(Health = Player(Health) - 0.5)
