from random import choices

class Perinola:
 def __init__(self):
  self.cara_visible = 1
 def __repr__(self):
  return f"Salio: {self.cara_visible}"
 def tirar(self):
  self.cara_visible = choices(1,self.caras)
  return self.cara_visible
  