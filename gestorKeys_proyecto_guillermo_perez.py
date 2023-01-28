'''


                        jillexdxd
                    Gestor de contraseñas
                        version final

'''
import random as rd
import csv
import pyperclip as pc

#Limpiar pantalla
def clear():
    for x in range(20):
        print("\n")

#Menu con numeros
def menu():
    menu=True
    print("Gestor de contraseñas\n")
    while menu:
        print("1. Generador de contraseña")
        print("2. Solicitar contraseña")
        print("3. Introducir contraseña ya creada")
        print("4. Regenerar contraseña")
        print("5. Borrar contraseña")
        print("6. Listado de contraseñas almacenadas")
        print("0. Salir")
        opcion=int(input("Introduce una opcion: "))
        if opcion==1:
            linea=generarKey()
        guardaCSV(linea)
        elif opcion==2:
            pedirKey()
        elif opcion==3:
            introducirKey()
        elif opcion==4:
            regenerarKey()
        elif opcion==5:
            borrarKey()
        elif opcion==6:
            listadoKeys()
        elif opcion==0:
            menu=False
        else:
            print("\nERROR: Introduce una opcion valida\n")

#Generar Contraseña (apila en una lista los datos para escribirlo en el csv en la funcion guardaCSV
def generarKey(): #Añadir seleccion de caracteres y asegurar que haya 1 numero al menos en lo generado    clear()
    lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    generado=""
    linea=[]
    
    plataforma=input("\nIntroduce plataforma: ")
    usuario=input("Introduce el usuario: ")
    n=int(input("Introduce la cantidad de caracteres deseados: "))
    controlNum=rd.randint(0,n)

    #Este bucle introduce en la variable "generado" los caracteres aleatoriamente hasta el numero deseado
    #Para controlar que haya obligatoriamente un numero en la contraseña declaro en la variable "controlNum"
    #un numero de 0 a n, asegurando que cuando x tome el valor de "controNum" introduca al menos un numero
    for x in range(n):
        if controlNum==x:
            random=rd.randint(52,61)
        else:
            random=rd.randint(0,61)
        generado=generado+lista[random]

    print("\nPlataforma:", plataforma)
    print("Usuario:",usuario)
    #print("Contraseña:",generado) #Mostraba en la anterior version la contraseña generada
    print("Contraseña:",len(generado)*"*")
    print("\nContraseña copiada en el portapapeles\n\n")
    pc.copy(generado)
    
    #Apila en orden los datos introducidos y generados para posteriormente guardarlos en el CSV con la funcion "guardaCSV()"
    linea.append(plataforma)
    linea.append(usuario)
    linea.append(generado)
    return linea

#Guarda la contraseña generada en un archivo csv
def guardaCSV(linea):
    f=open('almacenamiento.csv', '+a', newline='\n')    #Asignamos a f la funcion de abrir el fichero csv
    writer=csv.writer(f, delimiter=";")                 #Asignamos a writer el metodo writer para escribir con los parametros dados
    writer.writerow(linea)                              #Escribe en el documento una nueva linea con los datos pasados por parametro
    f.close()                                           #Cierra el archivo .csv guardando los cambios

#Solicitar la contraseña (busca en el archivo de csv devuelve la lista y cojo la posicion 3 que es la contraseña)
def pedirKey():
    clear()
    print("Solicita una contraseña almacenada:\n")
    plataforma=input("Introduce la plataforma: ")                           #Se introduce los dos primeros datos para buscar
    usuario=input("Introduce el usuario: ")
    fichero=csv.reader(open('almacenamiento.csv', "r"), delimiter=";")      #Asigna a fichero la funcion para el modo reader de la libreria csv
    control=False
    
    for linea in fichero:                                                   #Bucle for para comprobar la posicion de los datos
        if plataforma==linea[0] and usuario==linea[1]:
            control=True
            pc.copy(linea[2])                                               #De la libreria pyperclip metodo copy para copiar automaticamente la contraseña al portapapeles

    if control==True:
        print("\n<✓>Contraseña copiada al portapapeles<✓>\n")
    else:
        print("\n<!>No hay contraseña almacenada para esos valores<!>\n")
            
#Permitir guardar una contraseña ya dada (no tiene complicacion, lo mismo que el generado pero con informacion dada para la pass)
def introducirKey():
    clear()
    linea=[]
    plataforma=input("\nIntroduce plataforma: ")
    usuario=input("Introduce el usuario: ")
    key=input("Introduce la contraseña: ")
    linea.append(plataforma)
    linea.append(usuario)
    linea.append(key)
    guardaCSV(linea)
    print("Contraseña guardada\n")

#Modificar datos
def regenerarKey():
    clear()
    print("Modificar contraseña\n")
    reGen=generarKey()
    control=False
    L=[]                                                #Variable que uso para reapilar el contenido de el documento y reescribirlo en orden
    
    archivo=open('almacenamiento.csv', 'r')
    reader=csv.reader(archivo, delimiter=';')
    
    for linea in reader:                                    #Apila los datos en "L" cambiando el valor para la posicion de la contraseña en el fichero
        if reGen[0]==linea[0] and reGen[1]==linea[1]:
            control=True
            linea[2]=reGen[2]
        L.append(linea)
    archivo.close()

    if control==False:
        print("Plataforma y usuario no encontrado")
    else:    
        archivo=open('almacenamiento.csv', 'w+', newline='\n')                  #Se reescribe el fichero con los nuevos datos en la variable "L"
        writer=csv.writer(archivo, delimiter=';')
        writer.writerows(L)
        archivo.seek(0)
        reader=csv.reader(archivo)
        print("Contraseña regenerada con exito")
    archivo.close()
    
#Borra la linea entera y reajusta el documento
def borrarKey():
    clear()
    print("Borrar contraseña")
    plataforma=input("Introduce una plataforma: ")
    usuario=input("Introduce un usuario: ")
    L=[]
    control=False
    
    archivo=open('almacenamiento.csv', 'r')
    reader=csv.reader(archivo, delimiter=';')

    for linea in reader:                                    #Reescribe el archivo en la lista "L" sin la linea que vamos a borrar
        if plataforma==linea[0] and usuario==linea[1]:
            control=True
        else:
            L.append(linea)
    archivo.close()

    
    if control==True:                                       #Reescribe el archivo a partir de "L"
        archivo=open('almacenamiento.csv', 'w+', newline='\n')
        writer=csv.writer(archivo, delimiter=';')
        writer.writerows(L)
        archivo.seek(0)
        reader=csv.reader(archivo)
        print("\n<!>Contraseña borrada<!>")
    else:
        print("No se ha podido encontrar contraseña para los datos dados")

#Consulta datos almacenados (abre el archivo y da un listado de contraseñas almacenadas)
def listadoKeys():
    clear()
    print("Contraseñas almacenadas:\n")
    fichero=csv.reader(open('almacenamiento.csv', "r"), delimiter=";")
    for linea in fichero:
        print("Plataforma:",linea[0],"Usuario:",linea[1])
    print("")


#Main
menu()
