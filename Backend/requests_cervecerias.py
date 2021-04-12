'''
EXAMEN TECNICO INCREASE
Pablo Brun 2021

BACKEND
Pasos:
1. Obtener una lista de cervecerías que contengan el texto "lagunitas" en su
nombre. Para ello, se debe ejecutar el siguiente servicio, indicando el texto a
buscar en el queryParam "query". GET -
https://api.openbrewerydb.org/breweries/autocomplete

2. De la lista de resultados del punto 1, tomar aquellos que contengan en la key
"name", el valor "Lagunitas Brewing Co".

3. A través del siguiente servicio, obtener el detalle de cada cervecería de la lista
del punto 2 y tomar solo el que contenga "state" = "California".
GET - https://api.openbrewerydb.org/breweries/{id}

'''

import requests


class requests_cervecerias:
    # variables a utilizar
    query_name = 'lagunitas'
    query_name_2 = 'Lagunitas Brewing Co'
    state = 'California'

    # Paso 1
    # Query GET
    my_query_1 = requests.get('https://api.openbrewerydb.org/breweries/autocomplete', params={'query': query_name})

    # Paso 2
    # convierto el resultado a json
    my_query_2 = my_query_1.json()

    # busco los resultados por nombre y los agrego a la nueva lista
    res_paso2 = []
    for i in my_query_2:
        if query_name_2 in i['name']:
            res_paso2.append(i)

    # Paso3
    # para cada resultado de la lista del paso 2 hago un nuevo query con su ID y verifico el state y lo agrego a la nueva lista
    res_paso3 = []
    for i in res_paso2:
        my_query_paso3 = requests.get('https://api.openbrewerydb.org/breweries/' + i['id'])
        my_query_paso3 = my_query_paso3.json()
        if state in my_query_paso3['state']:
            res_paso3.append(my_query_paso3)

