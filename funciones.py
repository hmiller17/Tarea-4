def punto_1():
    #diccionario = {"perro":1,"gato":2,"pez":3,"raton":4}
    diccionario = {"perro":2,"gato":4,"pez":1,"raton":1}
    list(diccionario)
    sorted(diccionario)
    for i in diccionario:
        print(i)

def punto_2():
    diccionario_1 = {"perro":1,"gato":2,"pez":3,"raton":4,"Culebra":5}
    diccionario_2 = {"perro":1,"gato":2,"pez":3,"raton":4}
    #diccionario_1 = {"perro":1,"gato":2,"pez":3,"raton":4}
    #diccionario_2 = {"perro":1,"gato":2,"pez":3,"raton":4}
    for i,j in diccionario_1.items():
        if i not in diccionario_2:
            return print("Hay claves y valores que no estan en el otro diccionario")
        if diccionario_2[i] != j:
            return True
    print("Todos los claves y valores se encuentran en el otro diccionario")

def punto_3():
    diccionario_1 = {"perro":1,"gato":2,"pez":3,"Camilo":4}
    diccionario_2 = {"Camilo":20,"Julian":30,"Pedro":4}
    diccionario_final = {}
    for i,j in diccionario_1.items():
        diccionario_final[i] = j

    for i,j in diccionario_2.items():
        if i not in diccionario_final:
            diccionario_final[i] = j
    print(diccionario_final)

    

def punto_4():
    edad_minima = 30
    edad_maxima = 50
    lista_personas = [
    {"nombres": "María Fernanda", "apellidos": "Gómez López", "edad": 42},
    {"nombres": "Luis Fernando", "apellidos": "Martínez Rivas", "edad": 29},
    {"nombres": "Javier Alejandro", "apellidos": "Córdoba Sánchez", "edad": 37},
    {"nombres": "Isabel Cristina", "apellidos": "Vásquez Ortega", "edad": 31},
    {"nombres": "Santiago", "apellidos": "Suárez Rodríguez", "edad": 25},
    {"nombres": "Catalina", "apellidos": "Jiménez Moreno", "edad": 45},
    {"nombres": "Andrés Felipe", "apellidos": "Arévalo Silva", "edad": 39},
    {"nombres": "Valentina", "apellidos": "Mendoza Torres", "edad": 28},
    {"nombres": "Fernando", "apellidos": "Serrano Salazar", "edad": 55}
    ]
    for i in lista_personas:
        edad = i.get("edad")
        if edad_minima <= edad <= edad_maxima:
            nombres = i.get("nombres")
            apellidos = i.get("apellidos")
            print(f"Nombres: {nombres}, Apellidos: {apellidos}")


def main():

    punto_1()
    punto_2()
    punto_3()
    punto_4()


if(__name__ == "__main__"):
    main()