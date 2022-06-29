from DataBase import *

db = DataBase()

while(True):
    print('\033[34m')
    print("PROYECTO BD")
    print("============\n")
    print("1) Agregar una carrera")
    print("2) Agregar un alumno")
    print("3) Agregar malla curricular")
    print("4) Agregar asignaturas a una malla")
    print("5) Agregar un profesor")
    print("6) Agregar ramos a un alumno")
    print("0) Salir del programa")
    print('\033[0m')
    opcion = int(input("Ingrese una de las opciones: "))
    
    if opcion == 1:
        db.agregarCarrera(input("Ingrese el nombre de la carrera: "))
    elif opcion == 2:
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        runA = int(input("Ingrese el RUN del alumno: "))
        añoIngreso = int(input("Ingrese el año de ingreso a la carrera del alumno: "))
        nombreCarrera = input("Ingrese la carrera elegida por el alumno: ")
        db.agregarAlumno(nombre, apellido, runA, añoIngreso, nombreCarrera)
        db.actualizarCantAlumnos(nombreCarrera)
    elif opcion == 3:
        nombreCarrera=input("Ingrese el nombre de la carrera: ")
        año=int(input("Ingrese el año: "))
        cantCreditos=int(input("Ingrese la cantidad de creditos: "))
        db.agregarMallaCurricular(año,cantCreditos,nombreCarrera)
    elif opcion == 4:
        nombreCarrera=input("Ingrese el nombre de la carrera: ")
        año=int(input("Ingrese el año: "))
        idM = int(db.seleccionarMallaCurricular(año, nombreCarrera))

        if idM != 0:
            print("Se encontro la malla curricular ", idM)
            cantAsig=int(input("¿Cuantas asignaturas desea agregar?"))
            for i in range(cantAsig):
                nombreAsig=input("Ingrese el nombre de la asignatura: ")
                codigoAsig=input("Ingrese el codigo de la asignatura: ")
                cantCreditos=int(input("Ingrese la cantidad de creditos de la asignatura: "))
                semestre=int(input("Ingrese el semestre de la carrera en el que se imparte: "))
                prerequisito=input("Ingrese el codigo del ramo que es necesario para poder cursar la asignatura: ")
                notaAprobacion=float(input("Ingrese la nota de aprobacion minima para la asignatura: "))
                runP=int(input("Ingrese el RUN del profesor a cargo de la asignatura: "))
                db.agregarAsignatura(nombreAsig,codigoAsig,cantCreditos,semestre,prerequisito,notaAprobacion, idM,runP)
        else:
            print('\033[31m' + "No se encontro la malla curricular\nNo se puede continuar con la transaccion" + '\033[0m')
    elif opcion == 5:
        nombreP=input("Ingrese el nombre del profesor: ")
        apellidoP=input("Ingrese el apellido del profesor: ")
        runP=int(input("Ingrese el RUN del profesor: "))
        db.agregarProfesor(nombreP, apellidoP, runP)
    elif opcion == 6:
        nombreCarrera=input("Ingrese el nombre de la carrera: ")
        año=int(input("Ingrese el año: "))
        run=int(input("Ingrese el RUN del alumno: "))
        idM = int(db.seleccionarMallaCurricular(año, nombreCarrera))

        if idM != 0:
            print("Se encontro la malla curricular ", idM)
            semestreA=int(input("Eliga el semestre de las asignaturas a agregar: "))
            listaA=db.seleccionarAsignaturas(idM, semestreA)
            for asignatura in listaA:
                print("Asignatura = ", asignatura[0])
                semestre=int(input("Ingrese el semestre en que se cursa : "))
                año=int(input("Ingrese el año en el que se cursa: "))
                db.agregarRamo(asignatura[0],año,semestre)
                db.agregarRamoAlumno(asignatura[0], run)    
        else:
            print('\033[31m' + "No se encontro la malla curricular\nNo se puede continuar con la transaccion" + '\033[0m')
    elif opcion == 0:
        break
    else:
        print("No existe tal opcion\n")

    
db.terminarConexion()