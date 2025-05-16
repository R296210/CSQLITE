#IMPORTAMOS LIBRERIA DE SQLITE3 QUE VIENE EN PYTHON OTRAS BD TENEMOS QUE REALIZAR LA DESCARGA 
import sqlite3 as sql

#CREAMOS Y CONECTAMOS A UNA BASE DE DATOS REAL (CMDB.db) COMO EN cop.py (crud only python)
#SOLO QUE AHORA LOS QUERRY SI VAN EN LENGUAJE SQL 

def conectar():
    return sql.connect('CMDB.db')

#MANDAMOS NUESTRA PRIMERA INSTRUCCION DESPUES DE CONECTARNOS A LA BASE DE DATOS
#CREAMOS LA TABLA DEL CONTENIDO A GUARDAR ID, PROGRAMA, NOMBRE, HOMOCLAVE
def create_table():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS VIDEOTECA_MC (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Programa TEXT NOT NULL,
            Nombre TEXT NOT NULL,
            Homoclave TEXT NOT NULL,
            Galaxy TEXT NOT NULL,
            Spectra TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#CRUD + SQLITE3 + PYTHON for ADMIN
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

#UPDATE
def update_item(id_elemento, nuevo_programa, nuevo_nombre, nueva_homoclave, nuevo_galaxy, nuevo_spectra):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE VIDEOTECA_MC SET Programa = ?, Nombre = ?, Homoclave = ?, Galaxy = ?, Spectra = ? WHERE id = ?', (nuevo_programa, nuevo_nombre, nueva_homoclave, nuevo_galaxy, nuevo_spectra, id_elemento))
    conn.commit()
    conn.close()
    print("Item actualizado.")

#DELETE
def delete_item(id_elemento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM VIDEOTECA_MC WHERE id = ?', (id_elemento,))
    conn.commit()
    conn.close()
    print("Item eliminado.")

#MENU DE OPCIONES PARA CRUD SEGUN admin
def menu():
    while True:
        print("\n1. CREATE ITEM \n2. READ ITEM \n3. UPDATE ITEM \n4. DELETE ITEM \n5. EXIT")
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
            id_elemento = int(input("ID del item a actualizar: "))
            nuevo_programa  = input("Nuevo Programa: ")
            nuevo_nombre  = input("Nuevo Nombre: ")
            nueva_homoclave  = input("Nueva Homoclave: ")
            nuevo_galaxy  = input("Guardado en Galaxy: ")
            nuevo_spectra  = input("Guardado en Spectra: ")
            update_item(id_elemento, nuevo_programa, nuevo_nombre, nueva_homoclave, nuevo_galaxy, nuevo_spectra)
        elif opcion == '4':
            id_elemento = int(input("ID del producto a eliminar: "))
            delete_item(id_elemento)
        elif opcion == '5':
            break
        else:
            print("STUPID ASSHOLE!!! \nOpción no válida .")
        
#MENU PRINCIPAL 

if __name__ == "__main__":

    #create_table()
    menu()