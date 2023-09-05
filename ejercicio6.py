from lista import Lista

# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece(Marvel o DC) y biografía, implementar la funciones necesarias
# para poder realizar las siguientes actividades:


class Superhero:
    def __init__(self, name, year, comic_house, info):
        self.name = name
        self.year = year
        self.comic_house = comic_house
        self.info = info

    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}, Comic House: {self.comic_house}, Info: {self.info}"


def cargar_superheroes(lista):

    datos_superheroes = [
        Superhero("Spider-Man", 1962, "Marvel",
                  "Peter Parker es un estudiante de secundaria..."),
        Superhero("Batman", 1939, "DC",
                  "Bruce Wayne es un multimillonario empresario y filántropo..."),
        Superhero("Iron Man", 1963, "Marvel",
                  "Tony Stark es un genio inventor y empresario. Después de sufrir una lesión en el pecho, construye una armadura tecnológica que le otorga habilidades sobrehumanas y se convierte en el superhéroe conocido como Iron Man."),
        Superhero("Superman", 1938, "DC",
                  "Clark Kent es un extraterrestre del planeta Krypton..."),
        Superhero("Wonder Woman", 1941, "DC",
                  "Diana Prince es una princesa amazona de la isla de Themyscira..."),
        Superhero("Green Lantern", 1940, "DC",
                  "Hal Jordan es un piloto de pruebas que recibe un anillo de poder que le otorga superpoderesy lo convierte en Linterna Verde. Protege el universo como miembro de la Corporación de Linternas Verdes."),
        Superhero("Wolverine", 1974, "Marvel",
                  "Logan, también conocido como Wolverine, es un mutante con garras retráctiles y poderes regenerativos. Ha vivido durante siglos y es conocido por su naturaleza feroz y su participación en los X-Men."),
        Superhero("Doctor Strange", 1963, "DC",  # estaba en marvel
                  "El Dr. Stephen Strange era un cirujano talentoso que, después de un accidente automovilístico, busca la ayuda del Anciano y se convierte en el Hechicero Supremo, protegiendo el mundo de amenazas místicas."),
        Superhero("Captain Marvel", 1968, "Marvel",
                  "Carol Danvers, también conocida como la Capitana Marvel, es una exoficial de la Fuerza Aérea de los Estados Unidos. Después de un accidente, adquiere poderes cósmicos y se convierte en una heroína intergaláctica."),
        Superhero("Flash", 1956, "DC",
                  "Barry Allen es un científico forense que obtiene la velocidad sobrehumana después de ser alcanzado por un rayo. Se convierte en el superhéroe conocido como Flash, protector de Central City."),
        Superhero("Star Lord", 1976, "Marvel",
                  "Peter Quill, también conocido como Star Lord, es un aventurero espacial y líder de los Guardianes de la Galaxia. Posee habilidades tácticas y tecnológicas excepcionales.")
    ]

    for superheroe in datos_superheroes:
        lista.insert(superheroe, 'name')


# a. eliminar el nodo que contiene la información de Linterna Verde

def eliminar_lin_verde(lista):

    aparece = lista.search('Green Lantern', 'name')
    if aparece is None:
        print("No está en la lista")

    else:
        lista.delete('Green Lantern', 'name')
        print("Green Lantern eliminado")


# b. mostrar el año de aparición de Wolverine

def ap_wolverine(lista):

    year = int

    aparece = lista.search('Wolverine', 'name')
    if aparece is None:
        print("No está en la lista")

    else:
        year = lista.get_element_by_index(aparece).year
        print(f"El año de aparicion de wolverine es {year}")

        return year


# c. cambiar la casa de Dr. Strange a Marvel

def cambiar_dr_strange(lista, ):
    new_house = "Marvel"
    aparece = lista.search('Doctor Strange', 'name')

    if aparece is None:
        print("No está en la lista")

    else:
        hero = lista.get_element_by_index(aparece)
        hero.comic_house = new_house
        print(f"La casa de {hero.name} es {hero.comic_house}")


# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”

def biografia_traje_armadura(lista):

    for i in range(lista.size()):
        hero = lista.get_element_by_index(i)
        if 'armadura' in hero.info:
            print(f'{hero.name} tiene un su biografia la palabra "armadura"')

        elif 'traje' in hero.info:
            print(f'{hero.name} tiene un su biografia la palabra "traje"')


# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963

def name_house_before_year(lista):
    no_hay = True

    print("Superheroes cuya aparicion es anterior a 1963:")
    for i in range(lista.size()):
        hero = lista.get_element_by_index(i)

        if hero.year < 1963:
            print(
                f'Nombre: {hero.name} - Casa: {hero.comic_house} - año: {hero.year}')
            no_hay = False

    if no_hay:
        print("- VACIO.")


# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla

def casa_cap_marvel_wonder_woman(lista):
    for i in range(lista.size()):
        hero = lista.get_element_by_index(i)

        if hero.name == "Captain Marvel" or hero.name == "Wonder Woman":
            print(f'{hero.name} pertenece a {hero.comic_house}')


# g. mostrar toda la información de Flash y Star-Lord

def info_flash_star_lord(lista):
    for i in range(lista.size()):
        hero = lista.get_element_by_index(i)

        if hero.name == "Flash" or hero.name == "Star Lord":
            print(hero)
            print()


# h. listar los superhéroes que comienzan con la letra B, M y S

def starts_with_BMS(lista):

    lista_aux = Lista()

    no_hay: True

    print("superhéroes que comienzan con la letra B, M y S:")
    for i in range(lista.size()):
        hero = lista.get_element_by_index(i)

        if hero.name.startswith(('B', 'M', 'S')):
            lista_aux.insert(hero, 'name')
            no_hay = False

    if no_hay:
        print("- VACIO.")

    else:
        lista_aux.barrido()

    return lista_aux


# i. determinar cuántos superhéroes hay de cada casa de comic.

def hero_by_comic_house(lista, comic_house):
    c_comic_house = 0
    
    for i in range(lista.size()):
        hero = lista.get_element_by_index(i)
        
        if hero.comic_house == comic_house:
            c_comic_house += 1
            
    print(f"De {comic_house} hay {c_comic_house} superheroes")
            
    return c_comic_house


lista = Lista()
cargar_superheroes(lista)

# a
eliminar_lin_verde(lista)
print()
lista.barrido()
print()

# b
ap_wolverine(lista)
print()

# c
cambiar_dr_strange(lista)
print()

# d
biografia_traje_armadura(lista)
print()

# e
name_house_before_year(lista)
print()

# f
casa_cap_marvel_wonder_woman(lista)
print()

# g
info_flash_star_lord(lista)

# h
starts_with_BMS(lista)
print()

# i
hero_by_comic_house(lista, "Marvel")
print()

hero_by_comic_house(lista, "DC")
print()
