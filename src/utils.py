def imprimir(contador):
    """funcion para imprimir ordenado y con tabla"""
    print('-------------------------------------------------------')
    print('Jugador    Kills    Assists    Deaths    MVPs    Puntos') 
    print('-------------------------------------------------------')

    ordenado = dict(sorted(contador.items(), key=lambda x: x[1]['Puntos'], reverse = True))

    for jugador in ordenado:

        space = 11 - int(len(jugador))
        print(jugador, end='')
        print(space*' ', end= '')
        
        for metrica in ordenado[jugador]:
            print(ordenado[jugador][metrica], end='')
            space = int(len(metrica)) + 4 - len(str(ordenado[jugador][metrica])) 
            print((space)*' ', end= '')
        
        print()
        
def calcular_puntos(jug):
    """linea que suma los puntos de cada jugador por ronda """
    return jug['kills'] * 3 + jug['assists'] - jug['deaths'] 

def procesar_ronda(round, contador):
    """nicializamos los puntos y el mvp de cada ronda"""
    max_p = 0
    j_mvp = ''
    
    for jugador in round:

        # asignamos el diccionario de cada jugador a una variable para hacerlo mas sencillo
        jug = round[jugador]

        # calculamos los puntos de la ronda del jugador y los sumamos
        puntos = calcular_puntos(jug)
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
