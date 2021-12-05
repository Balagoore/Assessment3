import requests

result = requests.get("https://pokemon/ditto").json()

pokemon["id"], pokemon["name"], pokemon["height"], pokemon["weight"]

class BasePokemon:

    def __init__(self, name: str):
        self.name = name


class Pokemon(BasePokemon):

    def __init__(self, name: str, id: float, height: float, weight: float):

        BasePokemon.__init__(self, name)

        self.__name = name
        self.__id = id
        self.__height = height
        self.__weight = weight
    @property
    def Id(self):
        return self.__id
    @Id.setter
    def Id(self, id):
        self.__id = id
    def Height(self):
        return self.__height

    @Height.setter
    def Height(self, height):
        self.__height = height

    def Weight(self):
        return self.__weight

    @Weight.setter
    def Weight(self, weight):
        self.__weight = weight
  #  Id = property(__getID, __setID)
  #  Height = property(__getHeight, __setHeight)
  #  Weight = property(__getWeight, __setWeight)
    def __str__(self):
        return f'Pokemon name is {self.name}, {self.id}, {self.height}, {self.weight}'

    PokemonStats()


class PokemonStats:

   def __init__(self, hp: float, attack: str, defense: str, sp_attack: str, sp_defense: str, speed: float):
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__sp_attack = sp_attack
        self.__sp_defense = sp_defense
        self.__speed = speed

   @property
   def HP(self):
       return self.__hp

   @HP.setter
   def HP(self, hp):
       self.__hp = hp

   def Attack(self):
       return self.__attack

   @Attack.setter
   def Attack(self, attack):
       self.__attack = attack

   def Defense(self):
       return self.__defense

   @Defense.setter
   def Defense(self, defense):
       self.__defense = defense

   def Spatt(self):
       return self.__sp_attack
   @Spatt.setter
   def Spatt(self, sp_attack):
       self.__sp_attack = sp_attack

   def Spdef(self):
       return self.__sp_defense

   @Spdef.setter
   def Spdef(self, sp_defense):
       self.__sp_defense = sp_defense

   def Speed(self):
       return self.__speed
   @Speed.setter

   def Speed(self, speed):
       self.__speed = speed

   def __str__(self):
       return f'Pokemon description is {self.hp}, {self.attack}, {self.defense}, {self.sp_attack}, {self.sp_defense}'

class PokeAPI(Pokemon):
    def __init__(self, get_full, Pt):
        Pokemon.__init__(self, name, id, height, weight)
        self.get_full = get_full
        self.Pt = Pt
        Pt = False

    def get_pokemon(self, name):
        return pokemon

    def get_all(self, get_full):

        return basepokemon if get_full == Pt else print()

    def get_pokemon(self, get_full) -> Iterator:

        while get_full != Pt:
            yield pok .PokemonStats



pok = Pokemon(name, id, height, weight)
pok.str()
basepok = BasePokemon(name)
Ditto = Pokemon()

print(Ditto.get_full)
