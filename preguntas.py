"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data= [int(row[1]) for row in data]
    resultado=sum(data)
    resultado
    return resultado


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv","r") as file:
        data=file.readlines()
    data= [row[0] for row in data]
    data_1=list(set(data))
    resultados=dict(zip(data_1,[0,0,0,0,0]))
    for elemento in data:
        if resultados.get(elemento)!= None:
            val=resultados.get(elemento)+1
            resultados.update({elemento:val})
    tuplas=[(key,valor) for key, valor in resultados.items()]
    from operator import itemgetter
    f=sorted(tuplas, key=itemgetter(0))
    return f


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1= [row[0] for row in data]
    data_1=list(set(data_1))
    resultados=dict(zip(data_1,[0,0,0,0,0]))
    for elemento in data:
        if resultados.get(elemento[0])!= None:
            val=resultados.get(elemento[0])+int(elemento[1])
            resultados.update({elemento[0]:val})
    tuplas=[(key,valor) for key, valor in resultados.items()]
    from operator import itemgetter
    f=sorted(tuplas, key=itemgetter(0))
    return f


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    fechas=[]
    for elemento in data:
        fechas.append(elemento[2])
    fechas=[row.split('-') for row in fechas]
    meses=[]
    for elemento in data:
        meses.append(elemento[2][5:7])
    meses=list(set(meses))
    resultados=dict(zip(meses,[0] * len(meses)))
    for elemento in data:
        val=resultados.get(elemento[2][5:7])+1
        resultados.update({elemento[2][5:7]:val})
    tuplas=[(key,valor) for key, valor in resultados.items()]
    from operator import itemgetter
    f=sorted(tuplas, key=itemgetter(0))
    return f


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1=[row[:2] for row in data]
    result={}
    for letra, valor in data_1:
        valor=int(valor)
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra]=[valor]
    result=[(key,max(valor),min(valor)) for key, valor in result.items()]
    result=sorted(result, key=itemgetter(0),reverse=False)
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1=[elemento[-1].replace('\n','') for elemento in data]
    data_1=[row.split(',') for row in data_1]
    result={}
    for elemento in data_1:
        for elem in elemento:
            key,valor=elem.split(':')
            valor=int(valor)
            if key in result.keys():
                result[key].append(valor)
            else:
                result[key]=[valor]
    result=[(key,min(valor),max(valor)) for key, valor in result.items()]
    result=sorted(result, key=itemgetter(0),reverse=False)
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1=[row[:2] for row in data]
    result={}
    for letra, valor in data_1:
        valor=int(valor)
        if valor in result.keys():
            result[valor].append(letra)
        else:
            result[valor]=[letra]
    result=[(key,valor) for key, valor in result.items()]
    result=sorted(result, key=itemgetter(0),reverse=False)
    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    from operator import itemgetter
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1=[row[:2] for row in data]
    result={}
    for letra, valor in data_1:
        valor=int(valor)
        if valor in result.keys():
            #print()
            result[valor].append(letra)
        else:
            result[valor]=[letra]
    llaves=list(result.keys())
    for key in llaves:
        val=result[key]
        val=list(set(val))
        val=sorted(val)
        result[key]=val
    resultl=[(key,valor) for key, valor in result.items()]
    resultl=sorted(resultl, key=itemgetter(0),reverse=False)
    return resultl


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1=[elemento[-1].replace('\n','') for elemento in data]
    data_1=[row.split(',') for row in data_1]
    result={}
    for elemento in data_1:
        for elem in elemento:
            key,valor=elem.split(':')
            valor=int(valor)
            if key in result.keys():
                result[key].append(valor)
            else:
                result[key]=[valor]
    result=[(key,len(valor)) for key, valor in result.items()]
    #result=sorted(result, key=itemgetter(0),reverse=False)
    result=dict(result)
    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1=[(row[0],len(row[3].split(',')),len(row[4].split(',')))for row in data]
    return data_1


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1=[[row[1],row[3].split(',')] for row in data]
    result={}
    for elemento in data_1:
        for elem in elemento[1]:
            valor=elemento[0]
            valor=int(valor)
            if elem in result.keys():
                result[elem].append(valor)
            else:
                result[elem]=[valor]
    result=[(key,sum(valor)) for key, valor in result.items()]
    result=dict(result)
    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    from operator import itemgetter
    with open("data.csv","r") as file:
        data=file.readlines()
    data=[row.split('\t') for row in data]
    data_1=[[elemento[0],elemento[-1].replace('\n','').split(',')] for elemento in data]
    result={}
    for elemento in data_1:
        for elem in elemento[1]:
            val=elem.split(':')
            val=int(val[1])
            if elemento[0] in result.keys():
                result[elemento[0]].append(val)
            else:
                result[elemento[0]]=[val]
    result=[(key,sum(valor)) for key, valor in result.items()]
    result=sorted(result, key=itemgetter(0),reverse=False)
    result=dict(result)
    return result
