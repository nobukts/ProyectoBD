from cProfile import run
from mailbox import NoSuchMailboxError
import mysql.connector

#Clases a usar
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

    #Finalizar la conexion a la BD
    def terminarConexion(self):
        print("\nFinalizando conexion!")
        self.cursor.close()
        self.connection.close()
        print("Se finalizo correctamente la conexion")

    #Agregar una carrera a la BD
    def agregarCarrera(self, nombreCarrera):
        comando="INSERT INTO Carrera (nombreCarrera) VALUES (%s)"
        try:
            self.cursor.execute(comando, (nombreCarrera,))
            self.connection.commit()
            print("Se agrego correctamente la carrera ",nombreCarrera, "\n")
        except Exception as e:
            print(e)

    #Agregar un alumno a la BD
    def agregarAlumno(self, nombre, apellido, runA, añoIngreso, nombreCarrera):
        comando="INSERT INTO Alumno (nombreA, apellidoA, runA, correoA, añoIngreso, Carrera_nombreCarrera) VALUES (%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(comando, (nombre, apellido, runA, ((nombre+"."+apellido+"@mail.andes.cl").lower()), añoIngreso, nombreCarrera))
            self.connection.commit()
            print("Se agrego correctamente al alumno ", nombre, " ", apellido)
        except Exception as e:
            print(e)

# ===============================================================
#Codigo principal

db = DataBase()

while(True):
    print("1) Agregar una carrera")
    print("2) Agregar un alumno")
    print("0) Salir del programa")
    opcion = int(input("Ingrese una de las opciones: "))
    
    if opcion == 1:
        db.agregarCarrera(input("Ingrese el nombre de la carrera: "))
    elif opcion == 2:
        nombre = input("Ingrese el nombre del alumno:")
        apellido = input("Ingrese el apellido del alumno:")
        runA = int(input("Ingrese el RUN del alumno:"))
        añoIngreso = int(input("Ingrese el año de ingreso a la carrera del alumno:"))
        nombreCarrera = input("Ingrese la carrera elegida por el alumno:")
        db.agregarAlumno(nombre, apellido, runA, añoIngreso, nombreCarrera)
    elif opcion == 0:
        break
    else:
        print("No existe tal opcion\n")

    
db.terminarConexion()