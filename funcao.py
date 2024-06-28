import requests
import PIL.Image as pl
from urllib.request import urlopen
import customtkinter as s

eevee_triste = r"C:\Users\Miguel\Downloads\eevee.png"
icon_pokedex = r"C:\Users\Miguel\Codigos_python\Pokedex\ico_pokedex.ico"

class Pokedex():

  def valid_api(self):
    try:
      self.api = requests.get(f'https://pokeapi.co/api/v2/pokemon/')
      return True
    
    except:
      return False

  def api_poke(self,pokemon):
    self.pokemon = pokemon
    self.apipoke = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.pokemon.lower()}')
    self.poke = self.apipoke.json()
    return self.poke

  def getid(self,poke):
    self.id = self.poke['id']
    return self.id

  def getimg(self,id):
    link = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'
    img = pl.open(urlopen(link))
    img2 = s.CTkImage(img,size=(150,150))
    return img2

  def getname(self,poke):
    self.nome = self.poke['name']
    self.nome = self.nome.capitalize()
    return self.nome

  def gettype(self,poke):
      self.types = self.poke['types']
      match len(self.types):
        case 1:
          self.type1 = self.types[0]['type']['name']
          return f'Tipo: {self.type1.capitalize()}'
        
        case 2:
          self.type1 = self.types[0]['type']['name']
          self.type2 = self.types[1]['type']['name']
          return f'Tipos: {self.type1.capitalize()} | {self.type2.capitalize()}'
          
  def getability(self,poke):
    self.abilities = self.poke['abilities']
    match len(self.abilities):
      case 3: 
        self.ability1 = self.abilities[0]["ability"]["name"]
        self.ability2 = self.abilities[1]["ability"]["name"]
        self.ability3 = self.abilities[2]["ability"]["name"]
        return f" Habilidades: {self.ability1.capitalize()} | {self.ability2.capitalize()} | {self.ability3.capitalize()}  "
      case 2:
        self.ability1 = self.abilities[0]["ability"]["name"]
        self.ability2 = self.abilities[1]["ability"]["name"]
        return f'  Habilidades: {self.ability1.capitalize()} | {self.ability2.capitalize()}  '
      case 1:
        self.ability1 = self.abilities[0]["ability"]["name"]
        return  f'  Habilidades: {self.ability1.capitalize()}  '

  def getstatus(self,poke):
      self.status = self.poke["stats"]
      self.hp = self.status[0]['base_stat']
      self.attack = self.status[1]['base_stat']
      self.defense = self.status[2]['base_stat']
      self.spdef = self.status[4]['base_stat']
      self.speed = self.status[5]['base_stat']
      self.spatk = self.status[3]['base_stat'] 
      return f'Hp: {self.hp}\nAtk: {self.attack}\nSp.Atk: {self.spatk}\nDef: {self.defense}\nSp.Def: {self.spdef}\nSpeed: {self.speed}'
      
  def pop_error(self,main_variable,Poke,window): # Callback
    try:
      main = Poke.api_poke(main_variable.get())
      # Só cria uma janela se tiver um pokemon valido e algo escrito no input
      if main_variable.get() and main: # Nota: se main estiver vazia, ela passa, não tirar main_variable.get()
        top = s.CTkToplevel(window)
      return top,main
    except:
      error = s.CTkToplevel(window,relief='flat')
      error.iconbitmap(icon_pokedex)
      error.title("Pokedex")
      error.geometry("250x150")
      error.resizable(False, False)
      eevee = s.CTkImage(pl.open(eevee_triste),size=(100,100))
      label_eevee = s.CTkLabel(error,image=eevee,text="").pack()
      label_aviso = s.CTkLabel(error,text="Error de Digitação",font=("Cambria",20)).pack()