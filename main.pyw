import customtkinter as s
import PIL.Image as pl
from funcao import Pokedex

Poke = Pokedex()

icon_online = r"C:\Users\Miguel\Codigos_python\Pokedex\verde.png"
icon_offline = r"C:\Users\Miguel\Codigos_python\Pokedex\vermelho.png"
icon_pokedex = r"C:\Users\Miguel\Codigos_python\Pokedex\ico_pokedex.ico"

# Presets do menu principal
window = s.CTk()
window.title("Pokedex")
window.geometry("300x90")
s.set_appearance_mode("Dark")
window.iconbitmap(icon_pokedex)
window.resizable(False, False)

# Entrada
if Poke.valid_api() == True:
  main_variable = s.StringVar()
  input = s.CTkEntry(window, textvariable=main_variable, width=200).place(y=30,x=10)

# Botão criando janela de informações
def setup():
  try:
    top,main = Poke.pop_error(main_variable, Poke, window)
  except:
    pass
  
  # Segundo Try para evitar erros no Terminal
  try:
    top.title(Poke.getname(main))
    top.iconbitmap(icon_pokedex)
    top.resizable(False, False)
    Label_image = s.CTkLabel(top, image=Poke.getimg(Poke.getid(main)), text="").pack(padx=15,pady=5)
    label_name = s.CTkLabel(top,text=f'Nome: {Poke.getname(main)}',font=("Cambria",20),height=10).pack(padx=15,pady=1)
    label_id = s.CTkLabel(top,text=f'ID: {Poke.getid(main)}',font=("Cambria",20),height=10).pack(padx=15,pady=1)
    label_type = s.CTkLabel(top,text=Poke.gettype(main),font=("Cambria",20),height=10).pack(padx=15,pady=1)
    label_ability = s.CTkLabel(top,text=Poke.getability(main),font=("Cambria",20),height=10).pack(padx=15,pady=1)
    label_status = s.CTkLabel(top,text=Poke.getstatus(main),font=("Cambria",20)).pack(padx=15,pady=5)
  except:
    pass
    

# Janela menu principal
if Poke.valid_api() == True:
  botao_on = s.CTkImage(pl.open(icon_online),size=(12,12))
  label_online = s.CTkLabel(window,text="Online").place(y=60,x=25)
  label_apistate = s.CTkLabel(window,image=botao_on,text="").place(y=60,x=10)
  hello = s.CTkLabel(window,text="Digite o Nome ou ID do Pokémon").place(y=1,x=10)
  button = s.CTkButton(window,text="Pesquisar",command=setup,width=50).place(y=30,x=220)

if Poke.valid_api() == False:
  botao_off = s.CTkImage(pl.open(icon_offline),size=(12,12))
  label_online = s.CTkLabel(window,text="Offline").place(y=60,x=25)
  label_apistate = s.CTkLabel(window,image=botao_off,text="").place(y=60,x=10)

window.mainloop() 