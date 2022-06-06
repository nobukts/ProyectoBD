from multiprocessing import connection
import mysql.connector

class DataBase:

    #Conectar a la BD
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='168.232.165.245',
            port=3306,
            user='ici0043',
            password='BD7343',
            db='ici0043'
        )
        self.cursor = self.connection.cursor()
        print("Conexion exitosa\n")

    #Seleccionar una carrera
    def seleccionarCarrera(self, nombre):
        comando = """SELECT * from Carrera Where nombreCarrera = %s"""
        try:
            self.cursor.execute(comando, (nombre,))
            carrera = self.cursor.fetchone()

            print("Nombre:", carrera[0])
            print("Cantidad de alumnos:", carrera[1])
        except Exception as e:
            print("Hubo un error al leer la informacion")

    #Seleccionar todas las carreras
    def seleccionarTodasLasCarreras(self):
        comando = 'SELECT * FROM Carrera'
        
        try:
            self.cursor.execute(comando)
            carreras = self.cursor.fetchall()

            for carrera in carreras:
                print("Nombre de la carrera:", carrera[0], " / Cantidad de alumnos: ", carrera[1])
                
        except Exception as e:
            print("Hubo un error al leer la informacion")

    def agregarCarrera(self, nombre):
        comando="""INSERT INTO Carrera (nombreCarrera, cantidadAlumnos) VALUES (%s, %s) """
        try:
            self.cursor.execute(comando, (nombre, 0))
            self.connection.commit()
            print("Se agrego correctamente la carrera ", nombre, "\n")
        except Exception as e:
            print("Hubo algun problema al agregar la carrera")

    #Finalizar la conexion a la BD
    def terminarConexion(self):
        self.cursor.close()
        self.connection.close()


database = DataBase()

while(True):
    print("1) Mostrar una carrera")
    print("2) Mostrar todas las carreras")
    print("3) Agregar carrera")
    print("0) Salir del programa\n")

    opcion = int(input())
    
    if opcion == 1:
        print("Ingresar el nombre de la carrera: ")
        database.seleccionarCarrera(input())
    elif opcion == 2:
        database.seleccionarTodasLasCarreras()
    elif opcion == 3:
        print("Ingresar el nombre de la carrera")

        database.agregarCarrera(input())
    elif opcion == 0:
        break
    else:
        print("Ha ingresado una opcion que no se encuentra en el menu")

print("Finalizando conexion!")
database.terminarConexion()
    