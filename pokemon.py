class Pokemon:
  # Constructor
  def __init__(self,nom, poids):
    self.nom = nom

  def toString(self):
    return ("Je m'appelle "+ self.nom)