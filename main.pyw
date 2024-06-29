import customtkinter as s
import PIL.Image as pl
from funcao import Pokedex, create_path
from pathlib import Path

dir = Path(__file__).parent.resolve() # Pega o caminho da Pasta Atual
Poke = Pokedex()

wifi = create_path(dir,'wifi.png')
icon_online = create_path(dir,'verde.png')
icon_offline = create_path(dir,'vermelho.png')
icon_pokedex = create_path(dir,'ico_pokedex.ico')

api_status = Poke.valid_api()

button_off = s.CTkImage(pl.open(icon_offline),size=(12,12))
button_on = s.CTkImage(pl.open(icon_online),size=(12,12))
wifi_img = s.CTkImage(pl.open(wifi),size=(90,90))

# Presets do menu principal
window = s.CTk()
window.title("Pokedex")
window.geometry("300x90")
s.set_appearance_mode("Dark")
window.iconbitmap(icon_pokedex)
window.resizable(False, False)

# Entrada
if api_status:
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
    top.title(Poke.get_name(main))
    top.iconbitmap(icon_pokedex)
    top.resizable(False, False)
    Label_image = s.CTkLabel(top, image=Poke.get_img(Poke.get_id(main)), text="").pack(padx=15,pady=5)
    label_name = s.CTkLabel(top,text=f'Nome: {Poke.get_name(main)}',font=("Cambria",20),height=10).pack(padx=15,pady=1)
    label_id = s.CTkLabel(top,text=f'ID: {Poke.get_id(main)}',font=("Cambria",20),height=10).pack(padx=15,pady=1)
    label_type = s.CTkLabel(top,text=Poke.get_type(main),font=("Cambria",20),height=10).pack(padx=15,pady=1)
    label_ability = s.CTkLabel(top,text=Poke.get_ability(main),font=("Cambria",20),height=10).pack(padx=15,pady=1)
    label_status = s.CTkLabel(top,text=Poke.get_status(main),font=("Cambria",20)).pack(padx=15,pady=5)
  except:
    pass
    

# Janela menu principal
if api_status:
  label_online = s.CTkLabel(window,text="Online").place(y=60,x=25)
  label_apistate = s.CTkLabel(window,image=button_on,text="").place(y=60,x=10)
  hello = s.CTkLabel(window,text="Digite o Nome ou ID do Pokémon").place(y=1,x=10)
  button = s.CTkButton(window,text="Pesquisar",command=setup,width=50).place(y=30,x=220)
else:
  label_wifi = s.CTkLabel(window,image=wifi_img,text='').pack(padx=10,pady=10)
  label_online = s.CTkLabel(window,text="Offline").place(y=60,x=25)
  label_apistate = s.CTkLabel(window,image=button_off,text="").place(y=60,x=10)

window.mainloop() 