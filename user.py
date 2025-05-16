#IMPORTAMOS LIBRERIA DE SQLITE3 QUE VIENE EN PYTHON OTRAS BD TENEMOS QUE REALIZAR LA DESCARGA 
import sqlite3 as sql

#CREAMOS Y CONECTAMOS A UNA BASE DE DATOS REAL (CMDB.db) COMO EN cop.py (crud only python)
#SOLO QUE AHORA LOS QUERRY SI VAN EN LENGUAJE SQL 

def conectar():
    return sql.connect('CMDB.db')

#CRUD + SQLITE3 + PYTHON for USER
#CREATE
def create_item (programa, nombre, homoclave, galaxy, specta):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO VIDEOTECA_MC (Programa, Nombre, Homoclave, Galaxy, Spectra) VALUES (?, ?, ?, ?, ?)', (programa, nombre, homoclave, galaxy, specta))
    conn.commit()
    conn.close()
    print("item creado")
#READ
def read_iteam():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM VIDEOTECA_MC')
    resultados = cursor.fetchall()
    conn.close()
    for fila in resultados:
        print(fila)


#MENU DE OPCIONES PARA CRUD SEGUN admin
def menu():
    while True:
        print("\n1. CREATE ITEM \n2. READ ITEM \n3. EXIT")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            programa = input("Programa: ")
            nombre = input("Nombre del programa: ")
            homoclave = input("Homoclave: ")
            galaxy = input("Resguardo en Galaxy: ")
            spectra = input("Resguardo en Spectra: ")
            create_item (programa, nombre, homoclave, galaxy, spectra)
        elif opcion == '2':
            read_iteam()
        elif opcion == '3':
            break
        else:
            print("STUPID ASSHOLE!!! \nOpción no válida .")


        
#MENU PRINCIPALFOR USER

if __name__ == "__main__":
    menu()