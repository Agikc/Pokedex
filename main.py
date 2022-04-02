import requests

print('Pokedex')
print('='*50)

pokemon = input('Digite o Nome do Pokemon: ').lower()

print('='*50)

apipoke = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

if apipoke.status_code == 200:
    
    poke = apipoke.json()
    
    def getid():
        id = poke['id']
        print(f'No. {id}')

    def getname():
        nome = poke['name']
        print(f'Nome: {nome}')
    
    def gettype():
        types = poke['types']
        
        if len(types) == 2:
            type1 = types[0]['type']['name']
            type2 = types[1]['type']['name']
            print(f'Tipos: {type1} | {type2}')
        
        else:
            type1 = types[0]['type']['name']
            print(f'Tipo: {type1}')
            

    def getstatus():
        status = poke["stats"]
        hp = status[0]['base_stat']
        attack = status[1]['base_stat']
        defense = status[2]['base_stat']
        spdef = status[4]['base_stat']
        speed = status[5]['base_stat']
        spatk = status[3]['base_stat'] 
        print(f'HP: {hp}\nATK: {attack}\nSp.Atk: {spatk}\nDef: {defense}\nSp.Def: {spdef}\nSpeed: {speed}')

else:
    print('API FORA DO AR')

# Execução
getid()
getname()
gettype()
getstatus()
print('='*50)
