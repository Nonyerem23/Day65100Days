class character:
  name = None
  health = 100
  mp = 100

  def __init__(self, name):
    self.name = name
  def print(self):
    print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}")
  def setStats(self, health, mp):
    self.health = health
    self.mp = mp
class player(character):
  nickname = None
  lives = 3
  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname
  def print(self):
    print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")
  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} lives on!")
      return True
    else:
      print(f"{self.nickname} has expired!")
      return False

class enemy(character):
  type = None
  strength = None
  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength
  def print(self):
    print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")
class orc(enemy):
  speed = None
  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed
  def print(self):
    print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: {self.speed}")

class vampire(enemy):
  day = True
  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day
  def print(self):
    print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}")

print("🌟Generic RPG🌟")
print()
player1 = player("David")
player1.print()
print(player1.isAlive())
print()
vamp1 = vampire(False)
vamp1.print()
print()
vamp2 = vampire(True)
vamp2.print()
print()
orc1 = orc(200)
orc1.print()
print()
orc2 = orc(250)
orc2.print()
print()

orc3 = orc(300)
orc3.print()
print()
print("That's all folks!")
