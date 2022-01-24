from pokTerrestre import PokTerrestre

class PokSport(PokTerrestre):
  def __init__(self,nom, poids, taille, freq):
    super().__init__(nom, poids, taille)
    self.freq = freq

