import time
import string
import random
estudiantes = []
documentos = []
notas = []
docentes = []
documentosp = []
asignadas = []
asignaturas = []
posicio = 0
materias_per = []
materias_ganadas = []
mate_per2 = []
materias_hab = []
nota_per = []

cursos =["6A","7A","8A","9A","10A","11A"]
materias = ["matematicas", "español", "religion", "arte", "ingles", "sociales"]
A6=6
A7=6
A8=6
A9=6
A10=6
A11=6
asig = 0
print("BIENVENIDO AL COLEGIO ADSO.COM")
while True:
    while True:
        try:
            print("----------------- SELECCIONE SU ROL ----------------")
            print("1. Coordinador")
            print("2. Profesor")
            print("3. Estudiante")
            rol = int(input())
            if rol in [1,2,3]:
                break
            else:
                print("Solo ingresar los numeros asignados")
                print("---------------------------------------------------------------------------------------------------")
        except:
            print("No se aceptan estos caracteres")
            print("---------------------------------------------------------------------------------------------------")
    while True:
        if rol == 1:
            while True:
                try:
                    print("---------------------------------------------------------------------------------------------------")
                    print("-------------------------- LOGIN --------------------------")
                    print("1. Registrarse")
                    print("2. Iniciar Seccion")
                    log = int(input())
                    if log >= 1 and log < 4:
                        break
                    else:
                        print("Solo los numeros que estan asignados")
                except:
                    print("Solo numeros")
            if log == 1:
                print("--------------------------------------------------------------------------------------------------------------")
                print("------------------------------------------ Registrarse ------------------------------------------------")
                while True:
                    print("Ingrese su nombre")
                    nombre = input()
                    valido=nombre.split()
                    if len(valido)>=3:
                        break
                    else:
                        print("Minimo tres partes de su nombre")
                iniciales=valido[0][0]+valido[1][0]+valido[2]
                print("Su usuario es:", iniciales)
                longitud = 12
                minusculas = string.ascii_lowercase
                mayusculas = string.ascii_uppercase
                numeros = string.digits
                especiales = string.punctuation
                contraseña = [
                    random.choice(minusculas),
                    random.choice(mayusculas),
                    random.choice(numeros),
                    random.choice(especiales)
                ]
                todos = minusculas + mayusculas + numeros + especiales
                contraseña.append(random.choice(todos))
                random.shuffle(contraseña)
                contraseña_final = "".join(contraseña)
                print("Su contraseña es:", contraseña_final)
                print("----------------------------------------------------------------------------------------------------------------------------------")
                print("Ingrese una palabra clave para desbloquear su usuario por si se le bloquea por alguna razon")
                palabra = input()
                print("-------------------------------------- Iniciar Seccion -----------------------------------------")
                n = 3
                while True:
                    n -=1
                    usuario = input("Usuario: ")
                    if usuario == iniciales:
                        break
                    else:
                        print("Usuario Incorrecto")
                        print(f"Le quedan {n} intentos")
                        print("----------------------------------------------------------------------------------------------------------------------------------")
                        if n == 0:
                            print("Su usuario esta bloqueado")
                            print("Ingrese la palabra clave para desbloquearlo")
                            palab = input()
                            if palab == palabra:
                                print("Felicidades su usuario ha sido desbloquedo")
                                print("Su usuario es: ", iniciales)
                n = 3
                while True:
                    n -= 1
                    contra = input("contraseña: ")
                    if contra == contraseña_final:
                        break
                    else:
                        print("Contraseña Incorrecta")
                        print(f"Le quedan {n} intentos")
                        if n == 0:
                            print("Su usuario esta bloqueado")
                            print("Ingrese la palabra clave para desbloquearlo")
                            palab = input()
                            if palab == palabra:
                                print("Felicidades su usuario ha sido desbloquedo")
                                print("Su contraseña es: ", contraseña_final)
            if log == 2:
                print("-------------------------------------- Iniciar Seccion -----------------------------------------")
                n = 3
                while True:
                    n -=1
                    usuario = input("Usuario: ")
                    if usuario == iniciales:
                        break
                    else:
                        print("Usuario Incorrecto")
                        print(f"Le quedan {n} intentos")
                    if n == 0:
                        print("Su usuario esta bloqueado")
                n = 3
                while True:
                    n -= 1
                    contra = input("contraseña: ")
                    if contra == contraseña_final:
                        break
                    else:
                        print("Contraseña Incorrecta")
                        print(f"Le quedan {n} intentos")
                        if n == 0:
                            print("Su usuario esta bloqueado")
                            print("Ingrese la palabra clave para desbloquearlo")
                            palab = input()
                            if palab == palabra:
                                print("Felicidades su usuario ha sido desbloquedo")
                                print("su contraseña es: ", contraseña_final)
            while True:
                try:
                    print("---------------------------------------------------------------------------------------------------")
                    print("------------------ Sistema Escolar -------------------")
                    print("Opciones del Señor Coordinador")
                    print("1. Seleccionar Profesores")
                    print("2. Seleccionar Estudiantes")
                    print("3. Notificaciones")
                    print("4. Salir")
                    opi = input()
                    if opi in ["1","2","3"]:
                        break
                    else:
                        print("Error de opciones, solo(1-3)")
                        print("---------------------------------------------------------------------------------------------------")
                except:
                    print("Solo debe ingresar esas opciones")
                    print("---------------------------------------------------------------------------------------------------")
            if opi == "1":
                while True:         
                    while True:
                        try:
                            print("---------------------------------------------------------------------------------------------------")
                            print("-------------------------- Sistema academico de Profesores --------------------------")
                            print("1. Registrar Profesor")
                            print("2. Asignar Curso")
                            print("3. Eliminar Docente del curso")
                            print("4. Salir")
                            opinion = input()
                            if opinion in ["1","2","3","4"]:
                                break
                            else:
                                print("Solo ingresar los numeros asignados")
                                print("---------------------------------------------------------------------------------------------------")
                        except:
                            print("Solo debe ingresar esas opciones")
                            print("---------------------------------------------------------------------------------------------------")
                    if opinion == "1":
                        m = 1
                        print("---------------------------------------------------------------------------------------------------")
                        print("Ingrese el nombre del Profesor: ")
                        nombrep = input()
                        while True:
                            print(f"Ingrese el número de documento de {nombrep}:")
                            docp = input()
                            if docp.isdigit() and 7 <= len(docp) <= 10:
                                docp=int(docp)
                                break
                            elif docp.isdigit() and len(docp)<7:
                                docp=int(docp)
                                print("No puedes ingresar menos de 7 digitos")
                                print("---------------------------------------------------------------------------------------------------")
                            else:
                                print("No se pueden ingresar letras")
                            print("---------------------------------------------------------------------------------------------------")
                        if docp in documentosp:
                            print("Error, Este documento fue registrado")
                            print("Por motivos de seguridad será enviado al menú de opciones")
                            print("---------------------------------------------------------------------------------------------------")
                            break
                        else:
                            docentes.append(nombrep)
                            documentosp.append(docp)
                            print("Docente registrado con éxito")
                            print("---------------------------------------------------------------------------------------------------")
                    if opinion == "2":
                        if len(docentes)== 0:
                            print("No hay ningun docente registrado")
                            print("No hay a quien asignarle el curso")
                            print("--------------------------------------------------------------------------------------------------------------")
                            break
                        p = 1
                        while p <= 5:
                            try:
                                print("Ingrese el documento del Profesor:")
                                docps = int(input())
                                if docps in documentosp:
                                    break
                                else:
                                    print("Este documento no ha sido registrado")
                                    p += 1
                            except:
                                print("Error, no puede ingresar letras")
                            p += 1
                            if p > 5:
                                break
                        
                        if docps in documentosp:
                            pos = documentosp.index(docps)
                            print(f"Docente encontrado: {docentes[pos]}")
                            print("---------------------------------------------------------------------------------------------------")
                            print("¿A qué curso lo desea asignar?")
                            for i in cursos:
                                print(i)
                            while True:
                                try:
                                    print("Ingrese el curso al que lo va asignar:")
                                    curso = input()
                                    if curso in cursos:
                                        if curso == "6A" and A6>0:
                                            A6-=1
                                            print("Asignado con éxito a 6A")
                                        elif curso == "7A" and A7>0:
                                            A7-=1
                                            print("Asignado con éxito a 7A")
                                        elif curso == "8A" and A8>0:
                                            A8-=1
                                            print("Asignado con éxito a 8A")
                                        elif curso == "9A" and A9>0:
                                            A9-=1
                                            print("Asignado con éxito a 9A")
                                        elif curso == "10A" and A10>0:
                                            A10-=1
                                            print("Asignado con éxito a 10A")
                                        elif curso == "11A" and A11>0:
                                            A11-=1
                                            print("Asignado con éxito a 11A")
                                        else:
                                            print("No hay cupos disponibles o curso no existe")
                                        break
                                    else:
                                        print("Ese curso no a sido registrado")
                                except:
                                    print("Vuelva a intentarlo, tuvo un error")

                    if opinion == "3":
                        if len(documentosp) == 0:
                            print("No hay ningun profesor asignado")
                            print("--------------------------------------------------------------------------------------------------------------")
                            break   
                        f = 1
                        print("Asegurese de saber el número de documento")
                        while f <= 5:
                            try:
                                elimi = int(input("Digite el documento del docente al le que desea eliminar el curso:"))
                                if elimi in documentosp:
                                    posi = documentosp.index(elimi)
                                    print(f"Docente encontrado: ({docentes[posi]})")
                                    print("Ingrese el grado que lo va a eliminar:")
                                    grado = input()
                                    if grado in asignadas:
                                        posio = asignadas.index(grado)
                                        print(f"Ya se eliminó de ese curso {posio}")
                                    print("El docente ya fue eliminado de ese curso")
                                    break
                                else:
                                    print("Este docente no ha sido registrado")
                                f += 1
                            except:
                                print("No se aceptan letras")
                                f += 1
                            if f > 5:
                                break
                    if opinion == "4":
                        print("Saliendo del programa......")
                        break

            if opi == "2":
                while True:
                    while True:
                        while True:
                            try:
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("------------------------- Sistema academico de Estudiantes ----------------------")
                                print("Bienvenido Señor coordinador")
                                print("1. Registrar Estudiante")
                                print("2. Ver estudiantes")
                                print("3. Ver promedios y resultados")
                                print("4. Eliminar Estudiante del curso")
                                print("5. Salir")
                                opcion = input()
                                if opcion =="1" or opcion =="2" or opcion =="3" or opcion =="4" or opcion =="5" or opcion =="6" :
                                    break
                                else:
                                    print("Solo debe ingresar esas opciones (1-6)")
                                    print("--------------------------------------------------------------------------------------------------------------")
                            except:
                                print("Error, solo esas opciones")
                                print("--------------------------------------------------------------------------------------------------------------")
                            
                        if opcion == "1":
                            print("--------------------------------------------------------------------------------------------------------------")
                            print("Ingrese el nombre del estudiante: ")
                            nombre = input()
                            while True:
                                print(f"Ingrese el número de documento de {nombre}:")
                                cedula_est = input()
                                if cedula_est.isdigit() and len(cedula_est)<= 10 and len(cedula_est)>= 7:
                                    cedula_est=int(cedula_est)
                                    break
                                elif cedula_est.isdigit() and len(cedula_est)< 7:
                                    cedula_est=int(cedula_est)
                                    print("No puedes ingresar menos de 7 digitos")
                                else:
                                    print("No se pueden ingresar letras")
                                    print("--------------------------------------------------------------------------------------------------------------")
                            if cedula_est in documentos:
                                print("Este documento ya fue registrado, volverá al menú de estudiantes")
                                print("--------------------------------------------------------------------------------------------------------------")
                            else:
                                documentos.append(cedula_est)
                                estudiantes.append(nombre)
                                notas.append([0,0,0])
                                asignaturas.append("")
                                if len(asignadas)<= 0:
                                    asignadas.append(asig)
                                print("Estudiante registrado con éxito")
                            break
                        elif opcion == "2":
                            if len(estudiantes) == 0:
                                print("No hay estudiantes registrados")
                            for i in range(len(estudiantes)):
                                print(f"{i +1}. {estudiantes[i]} - Doc: {documentos[i]}")
                        elif opcion == "3":
                            if len(estudiantes) == 0:
                                print("No hay estudiantes registrados")

                            for m in range(len(estudiantes)):
                                notap = notas[m]
                                promedio = sum(notap) / 3
                                if promedio >= 7:
                                    estd = "GANA"
                                else:
                                    estd = "PIERDE"
                                print("")
                                print("--------------------- REPORTE DE ESTUDIANTES ------------------------")
                                print(f"Nombre:      {estudiantes[m]}")
                                print(f"Documento:   {documentos[m]}")
                                print(f"Asignatura:  {asignaturas[m]}")
                                print(f"Notas:       {notap}")
                                print(f"Promedio:    {promedio:.2f}")
                                print(f"Estado:      {estd}")
                                print("------------------ FIN DEL REPORTE ---------------------")
                                print("--------------------------------------------------------------------------------------------------------------")
                        elif opcion =="5":
                            z = 1
                            print("Asegurese de saber el número de documento")
                            while z <= 5:
                                try:
                                    eliminar = int(input("Digite el documento del estudiante que desea eliminar: -> "))
                                    if eliminar in documentos:
                                        posicion = documentos.index(eliminar)
                                        print(f"Estudiante encontrado: ({estudiantes[posicion]})")

                                        print("El estudiante ya fue eliminado")
                                        break
                                    else:
                                        print("Este estudiante no ha sido registrado")
                                        z += 1
                                except:
                                    print("No se acptan letras")
                                    z += 1
                                if z > 5:
                                    break
                        if opcion =="6":
                            print("Saliendo de esta parte del Sistema")
                            break
                    if opcion =="6":
                        print("--------------------------------------------------------------------------------------------------------------")
                        break
            if opi == "3":
                if len(notificacion) >0:
                    print(notificacion)
                    while True:
                        try:
                            print("Permite desbloquear al profesor?")
                            print("1. Si")
                            print("2. No")
                            op = int(input())
                            if op == 1 or op == 2:
                                break
                            else:
                                print("Solo los numeros asignados")
                        except:
                            print("Solo ingresar numeros")
                else:
                    print("No hay notificaciones hasta el momento")
                    print("Ingrese (x) para salir")
                    x = input()
                    if x == "x":
                        break      
            if opi == "4":
                print("Saliendo del progreama...")
                break
        elif rol == 2:
            while True:
                try:
                    print("---------------------------------------------------------------------------------------------------")
                    print("-------------------------- LOGIN --------------------------")
                    print("1. Registrarse")
                    print("2. Iniciar Secion")
                    log = int(input())
                    if log >= 1 and log < 4:
                        break
                    else:
                        print("Solo los numeros que estan asignados")
                except:
                    print("Solo numeros")
            if log == 1:
                print("--------------------------------------------------------------------------------------------------------------")
                print("------------------------------------------ Registrarse ------------------------------------------------")
                while True:
                    print("Ingrese su nombre")
                    nombre = input()
                    valido = nombre.split()
                    if len(valido)>=3:
                        break
                    else:
                        print("Minimo tres partes de su nombre")
            iniciales = valido[0][0]+valido[1][0]+valido[2]
            print("Su usuario es:", iniciales)
            longitud = 12
            minusculas = string.ascii_lowercase
            mayusculas = string.ascii_uppercase
            numeros = string.digits
            especiales = string.punctuation
            contraseña = [
                random.choice(minusculas),
                random.choice(mayusculas),
                random.choice(numeros),
                random.choice(especiales)
            ]
            todos = minusculas + mayusculas + numeros + especiales
            contraseña.append(random.choice(todos))
            random.shuffle(contraseña)
            contraseña_final = "".join(contraseña)
            print("Su contraseña es:", contraseña_final)
            print("--------------------------------------------------------------------------------------------------------")
            print("-------------------------------------- Iniciar Seccion -----------------------------------------")
            n = 3
            while True:
                n -=1
                usuario = input("Usuario: ")
                if usuario == iniciales:
                    break
                else:
                    print("Usuario Incorrecto")
                    print(f"Le quedan {n} intentos")
                    print("----------------------------------------------------------------------------------------------------------------------------------")
                    if n == 0:
                        print("Su usuario esta bloqueado")

                        notificacion = print("El usuario de un profesor ha sido bloqueado")
                n = 3
                while True:
                    n -= 1
                    contra = input("contraseña: ")
                    if contra == contraseña_final:
                        break
                    else:
                        print("Contraseña Incorrecta")
                        print(f"Le quedan {n} intentos")
                        if n == 0:
                            print("Su usuario esta bloqueado")
                            notificacion = print("El usuario de un profesor ha sido bloqueado")
            if log == 2:
                print("-------------------------------------- Iniciar Seccion -----------------------------------------")
                n = 3
                while True:
                    n -=1
                    usuario = input("Usuario: ")
                    if usuario == iniciales:
                        break
                    else:
                        print("Usuario Incorrecto")
                        print(f"Le quedan {n} intentos")
                    if n == 0:
                        print("Su usuario esta bloqueado")
                        notificacion = print("El usuario de un profesor ha sido bloqueado")
                n = 3
                while True:
                    n -= 1
                    contra = input("contraseña: ")
                    if contra == contraseña_final:
                        break
                    else:
                        print("Contraseña Incorrecta")
                        print(f"Le quedan {n} intentos")
                        if n == 0:
                            print("Su usuario esta bloqueado")
                            notificacion = print("El usuario de un profesor ha sido bloqueado")
            if len(docentes) == 0:
                print("No hay ningun docente registrado")
                while True:
                    try:
                        print("Ingrese (1) para volver al menu principal")
                        cero = int(input())
                        if cero == 1:
                            break
                        else:
                            print("Solo ingresar el numero uno")
                    except:
                        print("Solo ingresar numeros")
                if cero == 1:
                    break
            else:          
                print("----------------- MENU PROFESOR -----------------")
                print("1. Iniciar proceso completo de estudiantes")
                print("2. Salir")
                op_prof = int(input())
                if op_prof == 1:
                    print("Ejecutando el código completo del profesor...")
                    p=0
                    estudiantes_g = []
                    estudiantes_p = []
                    cedula = []
                    asign = []
                    materias_no_habilitadas = []
                    cursos = [ "6A",  "7A",  "8A",  "9A",  "10A",  "11A"]
                    asignaturas = ["matematicas", "español", "religion", "arte", "ingles", "sociales"]
                    rol = 0
                    cont = 0
                    while True:
                        try:
                            print("Ingrese el documento del docente")
                            document_doce = int(input())
                            if document_doce in documentosp:
                                print("Profesor encontrado")
                                print("--------------------------------------------------------------------------------------------------------------")
                                break
                            else:
                                print("Profesor no encontrado")
                                print("--------------------------------------------------------------------------------------------------------------")
                        except:
                            print("Solo numeros en la cedula")
                        print("--------------------------------------------------------------------------------------------------------------")

                    print(f"Nombre: {nombrep}")
                    print(f"Cedula: {docp}")
                    print(f"Curso en el que esta: {curso}")
                    print("--------------------------------------------------------------------------------------------------------------")
                    
                    while True:
                        try:
                            print("Ingrese la cantidad de estudiantes que hay en ese curso")
                            cant_curso = int(input())
                            if cant_curso == 0:
                                print("No a ingresado ningun estudiante")
                                exit()
                            break
                        except:
                            print("Solo ingresar numeros")
                            print("-------------------------------------------------------------------------------------------------------------------")

                    for i in range(1, cant_curso + 1):

                        suma1 = suma2 = suma3 = suma4 = suma5 = suma6 = 0.0
                        promedio1 = promedio2 = promedio3 = promedio4 = promedio5 = promedio6 = 0.0
                        suma_total = 0.0
                        z = 0 

                        print("--------------------------------------------------------------------------------------------------------------")
                        
                        while True:
                            print("Ingrese la cedula del estudiante")
                            cedula_input = input()
                            if cedula_input.isdigit():
                                if len(cedula_input) < 7:
                                    print("Cedula Invalida, debe tener entre 7 a 10 caracteres")
                                    print("--------------------------------------------------------------------------------------------------------------")
                                elif len(cedula_input) <= 10:
                                    cedula_est = int(cedula_input)
                                    if cedula_est in cedula:
                                        print("Esa cedula ya esta registrada")
                                        print("--------------------------------------------------------------------------------------------------------------")
                                    else:
                                        if cedula_est in documentos:
                                            pos = documentos.index(cedula_est)
                                            print(f"Estudiante encontrado: {estudiantes[pos]}")
                                            cedula.append(cedula_est)
                                            break
                                        else:
                                            print("Estudiante no encontrado")
                            else:
                                print("solo ingresar numeros en la cedula")

                        print("--------------------------------------------------------------------------------------------------------------")
                        b=0
                        for i in asignaturas:
                            b +=1
                            while True:
                                try:
                                    print(f"Ingrese la asignatura #{b} la cual quiere el promedio / ej: (1, 2, 3...)")
                                    print("PONER LOS NUMEROS EN ORDEN")
                                    cont2=0
                                    for i in asignaturas:
                                        cont2 += 1
                                        print(cont2, "", i)
                                    asignatura = int(input("asignatura: "))
                                    if asignatura == 1 or asignatura == 2 or asignatura == 3 or asignatura == 4 or  asignatura ==  5 or asignatura == 6:
                                        if asignatura in asign:
                                            print("Esta asignatura ya esta registrada")
                                            print("--------------------------------------------------------------------------------------------------------------")
                                        else:
                                            asign.append(asignatura)
                                            break                               
                                    else:
                                        print("solo las asignaturas que estan asignadas")
                                        print("--------------------------------------------------------------------------------------------------------------")
                                except:
                                        print("solo las asignaturas que estan asignadas")
                                        print("--------------------------------------------------------------------------------------------------------------")
                            if asignatura == 1:
                                asignatura = "Matematicás"
                            elif asignatura == 2:
                                asignatura = "Español"
                            elif asignatura == 3:
                                asignatura = "Religión"
                            elif asignatura == 4:
                                asignatura = "Arte"
                            elif asignatura == 5:
                                asignatura = "Ingles"
                            elif asignatura == 6:
                                asignatura = "Sociales"
                            if b == 1:
                                notas1 =[]
                                a = 0
                                for _ in range(1, 4):
                                    a +=1
                                    while True:
                                        try:
                                            print(f"Ingrese la nota #{a} de {asignatura}")
                                            nota = float(input())
                                            if 0<=nota<= 10:
                                                break
                                            else:
                                                print("Solo notas de 0 a 10")
                                        except:
                                            print("Solo numeros")
                                            print("--------------------------------------------------------------------------------------------------------------")
                                    suma1 += nota
                                    promedio1 = suma1 / 3
                                    notas1.append(nota)
                                if promedio1 >= 7:
                                    print(f"El estudiante {nombre} ganó la asignatura con un promedio de {promedio1}")
                                    materias_ganadas.append(asignatura)
                                else:
                                    z += 1
                                    print(f"El estudiante {nombre} perdió la asignatura con un promedio de {promedio1}")
                                    nota_per.append(promedio1)
                                    materias_per.append(asignatura)
                                    mate_per2.append(asignatura)
                                print("--------------------------------------------------------------------------------------------------------------")

                            if b == 2:
                                notas2 =[]
                                a = 0
                                for _ in range(1, 4):
                                    a +=1
                                    while True:
                                        try:
                                            print(f"Ingrese la nota #{a} de {asignatura}")
                                            nota = float(input())
                                            if 0<=nota<= 10:
                                                break
                                            else:
                                                print("Solo notas de 0 a 10")
                                        except:
                                            print("Solo numeros")
                                            print("--------------------------------------------------------------------------------------------------------------")
                                    suma2 += nota
                                    promedio2 = suma2 / 3
                                    notas2.append(nota)
                                if promedio2 >= 7:
                                    print(f"El estudiante {nombre} ganó la asignatura con un promedio de {promedio2}")
                                    materias_ganadas.append(asignatura)
                                else:
                                    z += 1
                                    print(f"El estudiante {nombre} perdió la asignatura con un promedio de {promedio2}")
                                    nota_per.append(promedio2)
                                    materias_per.append(asignatura)
                                    mate_per2.append(asignatura)
                                print("--------------------------------------------------------------------------------------------------------------")

                            if b == 3:
                                notas3 =[]
                                a = 0
                                for _ in range(1, 4):
                                    a +=1
                                    while True:
                                        try:
                                            print(f"Ingrese la nota #{a} de {asignatura}")
                                            nota = float(input())
                                            if 0<=nota<= 10:
                                                break
                                            else:
                                                print("Solo notas de 0 a 10")
                                        except:
                                            print("Solo numeros")
                                            print("--------------------------------------------------------------------------------------------------------------")
                                    suma3 += nota
                                    promedio3 = suma3 / 3
                                    notas3.append(nota)
                                if promedio3 >= 7:
                                    print(f"El estudiante {nombre} ganó la asignatura con un promedio de {promedio3}")
                                    materias_ganadas.append(asignatura)
                                else:
                                    z += 1
                                    print(f"El estudiante {nombre} perdió la asignatura con un promedio de {promedio3}")
                                    nota_per.append(promedio3)
                                    materias_per.append(asignatura)
                                    mate_per2.append(asignatura)
                                print("--------------------------------------------------------------------------------------------------------------")

                            if b == 4:
                                notas4 =[]
                                a = 0
                                for _ in range(1, 4):
                                    a +=1
                                    while True:
                                        try:
                                            print(f"Ingrese la nota #{a} de {asignatura}")
                                            nota = float(input())
                                            if 0<=nota<= 10:
                                                break
                                            else:
                                                print("Solo notas de 0 a 10")
                                        except:
                                            print("Solo numeros")
                                            print("--------------------------------------------------------------------------------------------------------------")
                                    suma4 += nota
                                    promedio4 = suma4 / 3
                                    notas4.append(nota)
                                if promedio4 >= 7:
                                    print(f"El estudiante {nombre} ganó la asignatura con un promedio de {promedio4}")
                                    materias_ganadas.append(asignatura)
                                else:
                                    z += 1
                                    print(f"El estudiante {nombre} perdió la asignatura con un promedio de {promedio4}")
                                    nota_per.append(promedio4)
                                    materias_per.append(asignatura)
                                    mate_per2.append(asignatura)
                                print("--------------------------------------------------------------------------------------------------------------")

                            if b == 5:
                                notas5 =[]
                                a = 0
                                for _ in range(1, 4):
                                    a +=1
                                    while True:
                                        try:
                                            print(f"Ingrese la nota #{a} de {asignatura}")
                                            nota = float(input())
                                            if 1<=nota<= 10:
                                                break
                                            else:
                                                print("Solo notas de 0 a 10")
                                        except:
                                            print("Solo numeros")
                                            print("--------------------------------------------------------------------------------------------------------------")
                                    suma5 += nota
                                    promedio5 = suma5 / 3
                                    notas5.append(nota)
                                if promedio5 >= 7:
                                    print(f"El estudiante {nombre} ganó la asignatura con un promedio de {promedio5}")
                                    materias_ganadas.append(asignatura)
                                else:
                                    z += 1
                                    print(f"El estudiante {nombre} perdió la asignatura con un promedio de {promedio5}")
                                    nota_per.append(promedio5)
                                    materias_per.append(asignatura)
                                    mate_per2.append(asignatura)
                                print("--------------------------------------------------------------------------------------------------------------")

                            if b == 6:
                                notas6 =[]
                                a = 0
                                for _ in range(1, 4):
                                    a +=1
                                    while True:
                                        try:
                                            print(f"Ingrese la nota #{a} de {asignatura}")
                                            nota = float(input())
                                            if 0<=nota<= 10:
                                                break
                                            else:
                                                print("Solo notas de 0 a 10")
                                        except:
                                            print("Solo numeros")
                                            print("--------------------------------------------------------------------------------------------------------------")
                                    suma6 += nota
                                    promedio6 = suma6 / 3
                                    notas6.append(nota)
                                print(f"El promedio de {asignatura} del estudiante {nombre} es de {promedio6}")
                                if promedio6 >= 7:
                                    print(f"El estudiante {nombre} ganó la asignatura con un promedio de {promedio6}")
                                    materias_ganadas.append(asignatura)
                                else:
                                    z += 1
                                    print(f"El estudiante {nombre} perdió la asignatura con un promedio de {promedio6}")
                                    nota_per.append(promedio6)
                                    materias_per.append(asignatura)
                                    mate_per2.append(asignatura)
                                print("--------------------------------------------------------------------------------------------------------------")
                        suma_total = (suma1 + suma2 + suma3 + suma4 + suma5 + suma6) / 6
                        asig = list(materias_per)  
                        if z == 0:
                            print(f"El estudiante {nombre} ganó el año")
                        if z == 1:
                            print("El estudiante perdió una materia")
                            print(f"El estudiante {nombre} tiene una oportunidad de recuperar la materia que perdió")
                            print("--------------------------------------------------------------------------------------------------------------")
                            print(f"El estudiante perdio la asignatura")
                            for i in materias_per:
                                print(i)
                            print("--------------------------------------------------------------------------------------------------------------")
                        if z == 2:
                            print("El estudiante perdió dos materias")
                            print(f"El estudiante {nombre} tiene una oportunidad de recuperar la materia que perdió")
                            print("--------------------------------------------------------------------------------------------------------------")
                            print(f"El estudiante perdió la asignatura")
                            for i in materias_per:
                                print(i)
                            print("--------------------------------------------------------------------------------------------------------------")
                        if z == 3:
                            print("El estudiante perdió 3 materias")
                            print("Perdió el año")
                            print(f"El estudiante {nombre} tiene una oportunidad de recuperar el año")
                            print("--------------------------------------------------------------------------------------------------------------")
                            print(f"El estudiante perdió la asignatura")
                            for i in materias_per:
                                print(i)
                            print("--------------------------------------------------------------------------------------------------------------")
                        if z > 3:
                            print("El estudiante perdió mas de 3 materias")
                            print("Perdió el año")
                            print(f"El estudiante {nombre} tiene una oportunidad de recuperar el año")
                            print("--------------------------------------------------------------------------------------------------------------")
                            print(f"El estudiante perdió la asignatura")
                            for i in materias_per:
                                print(i)
                        if len(materias_per) >=1:
                            while True:
                                try:
                                    print("--------------------------------------------------------------------------------------------------------------")
                                    print("El estudiante pudo hacer la recuperacion?")
                                    print("1. Si")
                                    print("2. No")
                                    op = int(input())
                                    if op == 1 or op == 2:
                                        break
                                    else:
                                        print("Solo numeros asignados")
                                except:
                                    print("Solo numeros")
                            if op == 1:
                                print("El estudiante ya hizo la recuperación")
                                p=0
                                for _ in range(z):
                                    p += 1
                                    while True:
                                        try:
                                            print(f"Ingrese la nota de la asignatura #{p} que habilito")
                                            nota_r = float(input())
                                            if 1<=nota_r<= 10:
                                                break
                                            else:
                                                print("Solo notas de 0 a 10")
                                        except:
                                            print("Solo numeros")
                                            print("--------------------------------------------------------------------------------------------------------------")
                                if mate_per2:
                                    if nota_r < 7:
                                        mate_per2.pop(0)
                                    else:
                                        recovered = mate_per2.pop(0)
                                        materias_hab.append(recovered)
                                        print("----------------------------------------------------------------------------------------------------------------------")
                                print("-----------------------------------------------------------------------------------------------------------------------")
                                print("------------------------- ADSO.COM ----------------------------")
                                print(curso)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Profesor: {nombrep}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Estudiante: {nombre}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Documento: {cedula_est}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas Ganadas:")
                                for i in materias_ganadas:
                                    print(i)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas Perdidas:")
                                for l in asig:
                                    print(l)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Asignaturas Habilitadas:")
                                for a in materias_hab:
                                    print(a)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Asignaturas No Habilitadas")
                                for i in mate_per2:
                                    print(i)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Promedio del estudiante: {suma_total}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                if len(materias_hab) >=0 and len(materias_hab) < 6:
                                    print("No logro habilitar todas las materias")
                                    print("Perdio el año")
                                    estudiantes_p.append(nombre)
                                print("--------------------------------------------------------------------------------------------------------------")
                                if len(materias_hab) == 3:
                                    print("Felicidades a ganado el año")
                                    estudiantes_g.append(nombre)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Estudiantes Que Ganaron el Año")
                                for q in estudiantes_g:
                                    print(q)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Estudiantes Que Perdieron el Año")
                                for u in estudiantes_p:
                                    print(u)
                            if op == 2:
                                print("-----------------------------------------------------------------------------------------------------------------------")
                                print("------------------------- ADSO.COM ----------------------------")
                                print(curso)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Profesor: {nombrep}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Estudiante: {nombre}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Documento: {cedula_est}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas Ganadas:")
                                for i in materias_ganadas:
                                    print(i)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas Perdidas:")
                                for l in asig:
                                    print(l)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas Habilitadas:")
                                for a in materias_hab:
                                    print(a)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(" Asignaturas No Habilitadas")
                                for i in mate_per2:
                                    print(i)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Promedio del estudiante: {suma_total}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                if len(materias_hab) >=0 and len(materias_hab) < 6:
                                    print("No logro habilitar todas las materias")
                                    print("Perdio el año")
                                    estudiantes_p.append(nombre)
                                print("--------------------------------------------------------------------------------------------------------------")
                                if len(materias_hab) == 3:
                                    print("Felicidades a ganado el año")
                                    estudiantes_g.append(nombre)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Estudiantes Que Ganaron el Año")
                                for q in estudiantes_g:
                                    print(q)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Estudiantes Que Perdieron el Año")
                                for u in estudiantes_p:
                                    print(u)
                                
                        else:
                                print("-----------------------------------------------------------------------------------------------------------------------")
                                print("------------------------- ADSO.COM ----------------------------")
                                print(curso)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Profesor: {nombrep}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Estudiante: {nombre}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Documento: {cedula_est}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas Ganadas:")
                                for i in materias_ganadas:
                                    print(i)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas Perdidas:")
                                for l in asig:
                                    print(l)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas Habilitadas:")
                                for a in materias_hab:
                                    print(a)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Asignaturas No Habilitadas")
                                for i in mate_per2:
                                    print(i)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print(f"Promedio del estudiante: {suma_total}")
                                print("--------------------------------------------------------------------------------------------------------------")
                                if len(materias_hab) >=0 and len(materias_hab) < 6:
                                    print("No logro habilitar todas las materias")
                                    print("Perdio el año")
                                    estudiantes_p.append(nombre)
                                print("--------------------------------------------------------------------------------------------------------------")
                                if len(materias_hab) == 3:
                                    print("Felicidades a ganado el año")
                                    estudiantes_g.append(nombre)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Estudiantes Que Ganaron el Año")
                                for q in estudiantes_g:
                                    print(q)
                                print("--------------------------------------------------------------------------------------------------------------")
                                print("Estudiantes Que Perdieron el Año")
                                for u in estudiantes_p:
                                    print(u)
                break
                if op_prof == 2:
                    print("Saliendo del programa...")
                    exit()

        elif rol == 3:
                while True:
                    try:
                        print("---------------------------------------------------------------------------------------------------")
                        print("-------------------------- LOGIN --------------------------")
                        print("1. Registrarse")
                        print("2. Iniciar Secion")
                        log = int(input())
                        if log >= 1 and log < 3:
                            break
                        else:
                            print("Solo los numeros que estan asignados")
                    except:
                        print("Solo numeros")
                if log == 1:
                    print("--------------------------------------------------------------------------------------------------------------")
                    print("------------------------------------------ Registrarse ------------------------------------------------")
                    while True:
                        print("Ingrese su nombre")
                        nombre = input()
                        valido=nombre.split()
                        if len(valido)>=3:
                            break
                        else:
                            print("Minimo tres partes de su nombre")
                    iniciales=valido[0][0]+valido[1][0]+valido[2]
                    print("Su usuario es:", iniciales)
                    print("------------------------------------------------------------------------------------------------")
                    longitud = 12
                    minusculas = string.ascii_lowercase
                    mayusculas = string.ascii_uppercase
                    numeros = string.digits
                    especiales = string.punctuation
                    contraseña = [
                        random.choice(minusculas),
                        random.choice(mayusculas),
                        random.choice(numeros),
                        random.choice(especiales)
                    ]
                    todos = minusculas + mayusculas + numeros + especiales
                    contraseña.append(random.choice(todos))
                    random.shuffle(contraseña)
                    contraseña_final = "".join(contraseña)
                    print("Su contraseña es:", contraseña_final)
                    print("------------------------------------------------------------------------------------------------")
                    print("-------------------------------------- Iniciar Seccion -----------------------------------------")
                    n = 3
                    while True:
                        n -=1
                        usuario = input("Usuario: ")
                        if usuario == iniciales:
                            break
                        else:
                            print("Usuario Incorrecto")
                            print(f"Le quedan {n} intentos")
                            print("----------------------------------------------------------------------------------------------------------------------------------")
                            if n == 0:
                                print("Su usuario esta bloqueado")
                                notificacion = print("El usuario de un estudiante ha sido bloqueado")
                    n = 3
                    while True:
                        n -= 1
                        contra = input("contraseña: ")
                        if contra == contraseña_final:
                            break
                        else:
                            print("Contraseña Incorrecta")
                            print(f"Le quedan {n} intentos")
                            if n == 0:
                                print("Su usuario esta bloqueado")
                                notificacion = print("El usuario de un estudiante ha sido bloqueado")
                if log == 2:
                    print("-------------------------------------- Iniciar Seccion -----------------------------------------")
                    n = 3
                    while True:
                        n -=1
                        usuario = input("Usuario: ")
                        if usuario == iniciales:
                            break
                        else:
                            print("Usuario Incorrecto")
                            print(f"Le quedan {n} intentos")
                        if n == 0:
                            print("Su usuario esta bloqueado")
                    n = 3
                    while True:
                        n -= 1
                        contra = input("contraseña: ")
                        if contra == contraseña_final:
                            break
                        else:
                            print("Contraseña Incorrecta")
                            print(f"Le quedan {n} intentos")
                            if n == 0:
                                print("Su usuario esta bloqueado")
                                print("Ingrese la palabra clave para desbloquearlo")
                                palab = input()
                                if palab == palabra:
                                    print("Felicidades su usuario ha sido desbloquedo")
                                    print("Tiene 3 nuevos intentos")
                if len(estudiantes) == 0:
                    print("No hay ningun estudiante registrado")
                    while True:
                        try:
                            print("Ingrese (1) para volver al menu principal")
                            cero = int(input())
                            if cero == 1:
                                break
                            else:
                                print("Solo ingresar el numero uno")
                        except:
                            print("Solo ingresar numeros")
                    if cero == 1:
                        break
                else:
                    print("------------------------ BIENVENIDOS A ADSO.COM ---------------------------")
                    print(f"{curso}")
                    print(f"Nombre Profesor: {nombrep}")
                    print(f"Nombre Estudiante: {nombre}")
                    print(f"Documento: {docp}")

                    print("--------------------------------------------------------------------------------------------------------------")
                    while True:
                        try:
                            print("Elija una opcion")
                            print("1. Asignaturas ganadas y perdidas con sus respectivas notas.")
                            print("2. Asignaturas habilitadas")
                            print("3. Promedio del estudiante")
                            opcion = int(input())
                            if opcion > 1 and opcion < 5:
                                break
                            else:
                                print("Ingresar solo los numeros asignados")
                        except:
                            print("Solo numeros")
                    if opcion == 1:
                        print("Asignaturas Perdidas:")
                        for l in asig:
                            print(l)
                        print("--------------------------------------------------------------------------------------------------------------")
                        print("Notas")
                        for i in notas_per:
                            print(i)
                        print("--------------------------------------------------------------------------------------------------------------")
                        print("Asignaturas Ganadas")
                        for v in materias_ganadas:
                            print(v)
                        print("--------------------------------------------------------------------------------------------------------------")
                    if opcion == 2:
                        print(f"Asignaturas Habilitadas:")
                        for a in materias_hab:
                            print(a)
                        print("--------------------------------------------------------------------------------------------------------------")
                    if opcion == 3:
                        print(f"Promedio del estudiante: {suma_total}")
                        print("--------------------------------------------------------------------------------------------------------------")

                    
                    
                    
                    

                

                
            
            
