rounds = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
    }
]

def imprimir(rounds):
    # funcion para imprimir ordenado y con tabla 
    print('-------------------------------------------------------')
    print('Jugador    Kills    Assists    Deaths    MVPs    Puntos') 
    print('-------------------------------------------------------')
    ordenado = dict(sorted(contador.items(), key=lambda x: x[1]['Puntos'], reverse = True))
    for jugador in ordenado:
        space = 11 - int(len(jugador))
        print(jugador, end='')
        print(space*' ', end= '')
        ultimo = 'kills'
        for metrica in ordenado[jugador]:
            print(ordenado[jugador][metrica], end='')
            space = int(len(metrica)) + 4 - len(str(ordenado[jugador][metrica])) 
            print((space)*' ', end= '')
        print()

# Crear diccionario contador 

contador = {}
for i in rounds[0]: #i es el jugador
    contador[i] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'Puntos': 0}

for n_round in range(len(rounds)):

    # inicializamos los puntos y el mvp de cada ronda
    max_p = 0
    j_mvp = ''
    
    for jugador in rounds[n_round]:
        
        # variable jug es para ahorrar caracteres
        jug = rounds[n_round][jugador]
        
        # linea que suma los puntos de cada jugador por ronda 
        puntos = jug['kills'] * 3 + jug['assists'] - jug['deaths'] 
        contador[jugador]['Puntos'] = contador[jugador]['Puntos'] + puntos
        
        # sumanos kills, assists y deaths
        contador[jugador]['kills'] = contador[jugador]['kills'] + jug['kills']
        contador[jugador]['assists'] = contador[jugador]['assists'] + jug['assists']
        if jug['kills'] == True:
            contador[jugador]['deaths'] += 1
            
        # obtenemos el MVP
        if puntos > max_p:
            j_mvp = jugador
            max_p = puntos
    
    # sumamos el MVP
    contador[j_mvp]['mvps'] += 1

    print()
    print(f'Ronda nro {n_round + 1}:')
    imprimir(rounds)

print()
print('Partida terminada: resultado final')
imprimir(rounds)

# El programa esta hecho para que si la cantidad de kills/asistencias/muertes es mas de las que se piden, la impresion se de de forma ordenada