from lista_lista import Lista
from random import randint

# Se cuenta con una lista de entrenadores Pokémon.De cada uno de estos se conoce:
# nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver las siguientes actividades utilizando lista de lista implementando las funciones necesarias:


class Trainer:

    def __init__(self, name, c_tourneys_won, c_battles_lost, c_battles_won):

        self.name = name
        self.c_tourneys_won = c_tourneys_won
        self.c_battles_lost = c_battles_lost
        self.c_battles_won = c_battles_won

    def __str__(self):
        return f'{self.name}: TG: {self.c_tourneys_won} - BP: {self.c_battles_lost} - BG: {self.c_battles_won}'


class Pokemon:

    def __init__(self, name, level, type, subtype):

        self.name = name
        self.level = level
        self.type = type
        self.subtype = subtype

    def __str__(self):
        return f'{self.name} - nivel {self.level} - {self.type} - {self.subtype}'


trainers_by_pokemon = [
    Trainer("Lorenzo", 8, 10, 18),
    Trainer("Juan", 3, 4, 16),
    Trainer("Pablo", 5, 1, 17)
]

trainers_list = Lista()

# Insertar entrenadores a la lista
for trainer in trainers_by_pokemon:
    trainers_list.insert(trainer, "name")

pokemons = [
    Pokemon("Pikachu", 25, "Eléctrico", None),
    Pokemon("Charizard", 50, "Fuego", "Volador"),
    Pokemon("Bulbasaur", 18, "Planta", "Veneno"),
    Pokemon("Squirtle", 22, "Agua", None),
    Pokemon("Jigglypuff", 30, "Normal", "Hada"),
    Pokemon("Gengar", 45, "Fantasma", "Veneno"),
    Pokemon("Machop", 20, "Lucha", None),
    Pokemon("Geodude", 15, "Roca", "Tierra"),
    Pokemon("Eevee", 35, "Normal", None),
    Pokemon("Mewtwo", 70, "Psíquico", None),
    Pokemon("Gyarados", 48, "Agua", "Volador"),
    Pokemon("Machamp", 40, "Lucha", None),
    Pokemon("Vaporeon", 42, "Agua", None),
    Pokemon("Alakazam", 55, "Psíquico", None),
    Pokemon("Charmander", 14, "Fuego", None),
    Pokemon("Bellsprout", 22, "Planta", "Veneno"),
    Pokemon("Pikachu", 13, "Eléctrico", None)
]

pokemons_list = Lista()

# Insertar pokemons a la sublista de trainers_list
for pokemon in pokemons:
    trainer_number = randint(0, trainers_list.size()-1)
    trainers_list.get_element_by_index(trainer_number)[
        1].insert(pokemon, 'name')

trainers_list.barrido_entrenadores()

# a. obtener la cantidad de Pokémons de un determinado entrenador


def c_pokemons_by_trainer(trainers_list, selected_trainer):
    trainer = trainers_list.search(selected_trainer, 'name')

    if trainer != None:
        value = trainers_list.get_element_by_index(trainer)
        name_trainer, pokemons = value[0], value[1]
        print(
            f'El entrenador {name_trainer.name} tiene {pokemons.size()} pokemons')

        return pokemons.size()

    else:
        print('El entrenador no se encontró')


# b. listar los entrenadores que hayan ganado más de tres torneos

def trainers_mas_tres(trainers_list):
    lista_aux = Lista()

    for i in range(trainers_list.size()):
        trainer = trainers_list.get_element_by_index(i)

        if trainer[0].c_tourneys_won > 3:
            lista_aux.insert(trainer[0], 'name')

    print("Los entrenadores que han ganado mas de tres torneos son:")
    lista_aux.barrido()


# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados

def mas_nivel_mas_torneos(trainers_list):
    mas_torneos = trainers_list.get_element_by_index(0)[0].c_tourneys_won
    pos_mas_torneos = 0

    for i in range(1, trainers_list.size()):
        comparado = trainers_list.get_element_by_index(i)[0]

        if mas_torneos < comparado.c_tourneys_won:
            mas_torneos = comparado.c_tourneys_won
            pos_mas_torneos = i

    value = trainers_list.get_element_by_index(pos_mas_torneos)

    entrenador, sublista = value[0], value[1]

    if sublista.size() > 0:
        pokemon_mayor = sublista.get_element_by_index(0)

        for i in range(1, sublista.size()):
            pokemon = sublista.get_element_by_index(i)

            if pokemon_mayor.level < pokemon.level:
                pokemon_mayor = pokemon

        print(
            f"El pokemon de mayor nivel del entrenador con mas torneos ganados ({entrenador.name} con {entrenador.c_tourneys_won}) es {pokemon_mayor.name} de nivel {pokemon_mayor.level}")

        return pokemon_mayor

    else:
        print("El entrenador no tiene pokemons en este momento")


# d. mostrar todos los datos de un entrenador y sus Pokémons

def data_trainer_pokemon(trainers_list, selected_trainer):
    index_trainer = trainers_list.search(
        selected_trainer, 'name')

    if index_trainer != None:
        value = trainers_list.get_element_by_index(
            index_trainer)

        entrenador, pokemons = value[0], value[1]
        print(f'Entrenador {entrenador}')
        print("Pokemons:")
        if pokemons.size() > 0:
            pokemons.barrido()
        else:
            print("- VACIO.")

    else:
        print("No se encontró el entrenador")


# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79%

def trainer_porc_seventy_nine(trainers_list):
    no_hay = 0

    for i in range(trainers_list.size()):
        entrenador = trainers_list.get_element_by_index(i)[0]

        if porc_seventy_nine(entrenador.c_battles_won, entrenador.c_battles_lost):
            print(f'{entrenador.name} ganó mas del 79% de las batallas con {entrenador.c_battles_won} victorias y perdió {entrenador.c_battles_lost}')
        else:
            no_hay += 1

        if no_hay == trainers_list.size():
            print("Ningun entrenador ganó mas del 79% de las batallas")


def porc_seventy_nine(won_battles, lost_battles):
    percentage = won_battles / (won_battles + lost_battles) * 100

    if percentage > 79:
        return True
    else:
        return False


# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)

def trainers_fuegoplanta_o_aguavolador(trainers_list):

    # Compara si tiene fuego o planta

    for trainer in range(trainers_list.size()):
        value = trainers_list.get_element_by_index(trainer)

        entrenador, pokemons = value[0], value[1]

        fuego = False
        planta = False

        for pokemon in range(pokemons.size()):

            tipo = pokemons.get_element_by_index(pokemon).type
            subtipo = pokemons.get_element_by_index(pokemon).subtype

            # print(f'{entrenador.name} tiene {tipo} y {subtipo}')

            if tipo == 'Fuego' or subtipo == 'Fuego':
                fuego = True

            if tipo == 'Planta' or subtipo == 'Planta':
                planta = True

            if fuego and planta:
                print(f"{entrenador.name} tiene fuego y planta")
                break

    # Compara si tiene agua y volador

    for trainer in range(trainers_list.size()):
        value = trainers_list.get_element_by_index(trainer)

        entrenador, pokemons = value[0], value[1]

        agua = False
        volador = False

        for pokemon in range(pokemons.size()):

            tipo = pokemons.get_element_by_index(pokemon).type
            subtipo = pokemons.get_element_by_index(pokemon).subtype

            # print(f'{entrenador.name} tiene {tipo} y {subtipo}')

            if tipo == 'Agua' or subtipo == 'Agua':
                agua = True

            if tipo == 'Volador' or subtipo == 'Volador':
                volador = True

            if agua and volador:
                print(f"{entrenador.name} tiene agua y volador")
                break


# g. el promedio de nivel de los Pokémons de un determinado entrenador

def promedio_trainer(trainers_list, selected_trainer):
    index_trainer = trainers_list.search(selected_trainer, 'name')
    suma_level = 0

    if index_trainer != None:
        value = trainers_list.get_element_by_index(index_trainer)

        trainer, pokemons = value[0], value[1]

        for pokemon in range(pokemons.size()):
            suma_level += pokemons.get_element_by_index(pokemon).level

        prom_pokemon = round(suma_level/pokemons.size(), 1)

        print(
            f'El entrenador {trainer.name} tiene un promedio de nivel de pokemons de {prom_pokemon}')

        return prom_pokemon

    else:
        print("No se encontró el entrenador")


# h. determinar cuántos entrenadores no_tienen a un determinado Pokémon

def c_specific_pokemon(trainers_list, selected_pokemon):

    c_trainer_has_pokemon = 0

    for i in range(trainers_list.size()):

        value = trainers_list.get_element_by_index(i)
        trainer, pokemons = value[0], value[1]

        c_pokemon = 0

        for pokemon in range(pokemons.size()):
            name_pokemon = pokemons.get_element_by_index(pokemon).name

            if name_pokemon == selected_pokemon:
                c_pokemon += 1

        if c_pokemon > 0:
            print(
                f'El entrenador {trainer.name} tiene {c_pokemon} {selected_pokemon}')
            c_trainer_has_pokemon += 1

    print(f'{c_trainer_has_pokemon} entrenadores no_tienen a {selected_pokemon}')

    return c_trainer_has_pokemon


# i. mostrar los entrenadores que no_tienen Pokémons repetidos

def trainer_repeated_pokemons(trainers_list):

    trainers_by_pokemon = {}

    for i in range(trainers_list.size()):
        entrenador = trainers_list.get_element_by_index(i)

        for pokemon in range(entrenador[1].size()):
            name_pokemon = entrenador[1].get_element_by_index(pokemon).name

            if name_pokemon in trainers_by_pokemon:
                trainers_by_pokemon[name_pokemon].append(
                    entrenador[0].name)

            else:
                trainers_by_pokemon[name_pokemon] = [
                    entrenador[0].name]

    for name_pokemon, trainer_list in trainers_by_pokemon.items():

        if len(trainer_list) > 1:
            if len(trainer_list) != len(set(trainer_list)):
                print(f'{trainer_list[0]} tiene mas de un {name_pokemon}')


# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull

def trainer_tyrantrum_terrakion_wingull(trainers_list):
    no_tienen = True
    
    for i in range(trainers_list.size()):
        
        value = trainers_list.get_element_by_index(i)

        trainer, pokemons = value[0], value[1]

        for j in range(pokemons.size()):
            pokemon = pokemons.get_element_by_index(j)

            if pokemon.name in "Tyrantrum":
                print(f'{trainer.name} tiene a {pokemon.name}')
                no_tienen = False

            if pokemon.name in "Terrakion":
                print(f'{trainer.name} tiene a {pokemon.name}')
                no_tienen = False

            if pokemon.name in "Wingull":
                print(f'{trainer.name} tiene a {pokemon.name}')
                no_tienen = False
                
    if no_tienen :
        print("Ningun entrenador tiene estos pokemons(Tyrantrum, Terrakion o Wingull)")


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos

def trainer_has_pokemon(trainers_list, trainer_name, pokemon_name):
    index_trainer = trainers_list.search(trainer_name, 'name')

    if index_trainer != None:
        value = trainers_list.get_element_by_index(index_trainer)
        trainer, pokemons = value[0], value[1]

        cont = 0

        for j in range(0, pokemons.size()):
            pokemon = pokemons.get_element_by_index(j)

            if pokemon.name in pokemon_name:
                cont += 1
                print(f'Datos del entrenador: {trainer}')
                print(f'Datos del pokemon: {pokemon}')
        if cont == 0:
            print(f'no se encontró al pokemon {pokemon_name}')


# a
c_pokemons_by_trainer(trainers_list, "Lorenzo")
print()

# b
trainers_mas_tres(trainers_list)
print()

# c
mas_nivel_mas_torneos(trainers_list)
print()

# d
data_trainer_pokemon(trainers_list, "Juan")
print()

# e
trainer_porc_seventy_nine(trainers_list)
print()

# f
trainers_fuegoplanta_o_aguavolador(trainers_list)
print()

# g
promedio_trainer(trainers_list, "Pablo")
print()

# h
c_specific_pokemon(trainers_list, 'Pikachu')
print()

# i
trainer_repeated_pokemons(trainers_list)
print()

# j
trainer_tyrantrum_terrakion_wingull(trainers_list)
print()

# k
trainer_has_pokemon(trainers_list, "Lorenzo", "Charmander")
