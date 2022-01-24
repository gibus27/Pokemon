from pokemon import Pokemon

class PokTerrestre(Pokemon):
  def __init__(self,nom, poids, taille):
    super().__init__(nom, poids)
    self.taille = taille

