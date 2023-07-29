class Player:
  def __init__(self, name):
    self.name = name

  @property
  def name(self):
    return self.name

  @name.setter
  def name(self, name):
    self.name = name

class BasketballPlayer(Player):
  positions = ["Guard", "Forward", "Center"]

  def __init__(self, name, position):
    super().__init__(name)
    self.position = position

  @property
  def position(self):
    return self.position

  @position.setter
  def position(self, position):
    if position not in BasketballPlayer.positions:
      raise ValueError("Invalid position")
    self.position = position

