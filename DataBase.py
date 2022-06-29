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
    
    #Agregar malla curricular a la BD
    def agregarMallaCurricular(self, año, cantCreditos, nombreCarrera):
        comando="INSERT INTO MallaCurricular (añoM, cantCreditosM, Carrera_nombreCarrera) VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(comando, (año, cantCreditos, nombreCarrera))
            self.connection.commit()
            print("Se ingreso correctamente la malla para la carrera ", nombreCarrera, " para el año", año)
        except Exception as e:
            print(e)

    #Seleccionar un idM de la BD
    def seleccionarMallaCurricular(self, año, nombreCarrera):
        comando="SELECT idM FROM MallaCurricular WHERE añoM=%s AND Carrera_nombreCarrera=%s"
        try:            
            self.cursor.execute(comando, (año, nombreCarrera))
            info = self.cursor.fetchone()
            return info[0]
        except Exception as e:
            print(e)
            return 0
    
    #Agregar una asignatura a la BD
    def agregarAsignatura(self, nombre, codigo, cantCred, semestre, prerequisito, notaAprob, idM, runP):
        comando="INSERT INTO Asignatura (nombreR,codigoR,cantCreditosR,semestre,prerequisito, notaAprobacion, MallaCurricular_idM,Profesor_run) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(comando, (nombre, codigo, cantCred,semestre,prerequisito,notaAprob,idM,runP))
            self.connection.commit()
            print("La asignatura ",nombre, " se ha creado con exito")
        except Exception as e:
            print(e)

    #Agregar un profesor a la BD
    def agregarProfesor(self, nombre, apellido, runP):
        comando="INSERT INTO Profesor (nombreP, apellidoP, runP, correoP) VALUES (%s,%s,%s,%s)"
        try:
            self.cursor.execute(comando, (nombre, apellido, runP, ((nombre+"."+apellido+"@mail.andes.cl").lower())))
            self.connection.commit()
            print("Se agrego correctamente al profesor ", nombre, " ", apellido)
        except Exception as e:
            print(e)
    
    #Actualizar cantidad de alumnos
    def actualizarAlumnos(self, nombreCarrera):
        comando="""UPDATE Carrera 
                    SET cantAlumnos = (SELECT COUNT(DISTINCT nombreA) 
                                        FROM Alumno
                                        WHERE Carrera_nombreCarrera='%s') 
                    WHERE nombreCarrera=%s"""
        try:
            self.cursor.execute(comando, (nombreCarrera, nombreCarrera))
            self.connection.commit()
        except Exception as e:
            print(e)        
    
    #Actualizar cantidad de creditos del alumno
    def actualizarCreditos(self, runA):
        comando="""UPDATE `Alumno` al
                    SET cantCreditosA=(SELECT SUM(a.cantCreditosR)
                                        FROM `Alumno_has_Ramo` alR JOIN `Ramo` r join `Asignatura` a
                                        WHERE alR.estadoRamo='2' and alR.Alumno_runA='%s' and a.codigoR=r.Asignatura_codigo and r.nroRamo=alR.Ramo_nroRamo)
                    WHERE al.runA='%s'"""
        try:
            self.cursor.execute(comando, (runA, runA))
            self.connection.commit()
        except Exception as e:
            print(e)

    #Seleccionar las asignaturas de una malla y semestre
    def seleccionarAsignaturas(self, idM, semestre):
        comando="SELECT codigoR FROM Asignatura WHERE MallaCurricular_idM=%s AND semestre=%s"
        try:
            self.cursor.execute(comando,(idM,semestre))
            codAs=self.cursor.fetchall()
            return codAs
        except Exception as e:
            print(e)
            return 0

    #Agregar ramos a la BD
    def agregarRamo(self, codA, año, semestre):
        comando="INSERT INTO Ramo (semestre, año, Asignatura_codigo) VALUES(%s,%s,%s)"
        try:
            self.cursor.execute(comando, (semestre, año, codA))
            self.connection.commit()
            print("Se agrego correctamente a la tabla de ramos")
        except Exception as e:
            print(e)

    def agregarRamoAlumno(self, codA, runA):
        comando="SELECT nroRamo FROM Ramo r WHERE r.nroRamo NOT IN (SELECT Ramo_nroRamo FROM Alumno_has_Ramo WHERE Ramo_nroRamo IS NOT NULL)"
        try:
            self.cursor.execute(comando)
            listaRamos=self.cursor.fetchall()
            for ramo in listaRamos:
                if ramo == codA: break
            
            estadoRamo = int(input("Ingrese el estado del ramo: "))
            comando="INSERT INTO Alumno_has_Ramo (ALumno_runA, Ramo_nroRamo, estadoRamo) VALUES (%s,%s,%s)"
            try:
                self.cursor.execute(comando,(runA, ramo[0], estadoRamo))
                self.connection.commit()
                print("Se hizo la union entre ramo y alumno correctamente")
            except Exception as e2:
                print(e2)
        except Exception as e1:
            print(e1)