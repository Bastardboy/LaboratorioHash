from datetime import date
import math
import time
import hashlib

def hash(palabra):
 
    original = palabra
    #generamos 2 diccionarios con los caracteres de la base a utilizar 
    diccionario = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,'i':18,
    'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,'v':31,'w':32,'x':33,'y':34,'z':35, 'A':36,'B':37,'C':38,
    'D':39,'E':40,'F':41,'G':42,'H':43,'I':44,'J':45,'K':46,'L':47,'M':48,'N':49,'O':50,'P':51,'Q':52,'R':53,'S':54,'T':55,'U':56,'V':57,
    'W':58,'X':59,'Y':60,'Z':61,' ':62, ',':63, '.':64, ';':65, ':':66, '-':67, '_':68, '!':69, '?':70, '¡':71, '¿':72, '"':73, '\'':74,}

    diccionario2 = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',
    19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x',34:'y',35:'z',36:'A',37:'B',38:'C',
    39:'D',40:'E',41:'F',42:'G',43:'H',44:'I',45:'J',46:'K',47:'L',48:'M',49:'N',50:'O',51:'P',52:'Q',53:'R',54:'S',55:'T',56:'U',57:'V',
    58:'W',59:'X',60:'Y',61:'Z',62:' ', 63:',', 64:'.', 65:';', 66:':', 67:'-', 68:'_', 69:'!', 70:'?', 71:'¡', 72:'¿', 73:'"', 74:"'"}

    #tomamos el tamaño y el valor de la primera letra del string en el diccionario
    #verificamos si el caracter se encuentra en el diccionario
    size2 = int(len(palabra))
    
    if palabra[0] not in diccionario.keys():
        return -1
    primera = diccionario[palabra[0]]
    contador = 0
    #en el caso de que la palabra contenga menos de 55 caracteres, se completa con ceros
    
    flag = True
    while(flag):
        if(len(palabra)%55==0):
            flag = False
        else:
            if (len(palabra)+2)%55==0:
                contador = contador -1
                if (primera+contador) <= 74: 
                    palabra = palabra + str(diccionario2[primera+contador])
                    palabra =  str(diccionario2[primera+contador]) + palabra
                else:
                    primera = 0
            else:
                contador = contador + 1
                if (primera+contador) <= 74: 
                    palabra = palabra + str(diccionario2[primera+contador])
                else:
                    primera = 0


    #tomamos la nueva palabra, sus divisiones en 55 y el dia actual haciendo un corrimiento con este
    guardarLargo = int(len(palabra))
    division = int(guardarLargo/55)
    diaHoy = date.today()
    diaHoy = diaHoy.day + 5

    #En la siguiente secci´on se crea un arreglo con los pesos de cada carácter sumado con el contador y la variable diaHoy. 
    Arr_Pesos = []
    count = 1
    for i in palabra:
        Arr_Pesos.append(int(diccionario.get(i))+diaHoy+count)
        count = count + 1
    
    #Una vez que se generan los pesos del arreglo, se procede a convertilo en palabra
    contadordivision = 0
    salida = ""
    suma = 0

    #Los números se convierten en letras, de esta forma se ajusta al hash
    for i in range(guardarLargo):
        if(contadordivision == division-1):
            suma = suma + Arr_Pesos[i] 
            contadordivision = 0
            
            if(suma<=74):
                salida = salida + str(diccionario2.get(suma))
            else:
                flag = True
                num = suma
                while(flag):
                    if(num <= 74):
                        flag = False
                        salida = salida + str(diccionario2.get(num))
                        num = suma
                        
                    else:
                        num = num - 74

        else:
            suma = suma + Arr_Pesos[i]
            contadordivision = contadordivision + 1
    

    print("El hash de: ",original," es: ")
    print(salida)
    entropia(salida)


#la entropia se calcula como el largo de la palabra ingresada por el logaritmo en base 2 de la base utilizada:
def entropia(palabra):
    entropia =55*math.log(74,2)

    print("La entropia de ",palabra," es: ", entropia) 

def tiempo(palabra):
    inicio = time.time()
    hash(palabra)
    fin = time.time()
    print("El tiempo de ejecución HASH LABORATORIO es: ", fin-inicio, "\n")
    

def md5xd(palabra):
    inicio = time.time()
    md5 = hashlib.md5(palabra.encode())
    fin = time.time()
    entropia = 32*math.log(16,2)
    print("El hash MD5 de: ",palabra," es: ")
    print(md5.hexdigest())
    print("La entropia de MD5",palabra," es: ", entropia,"\n")

def tiempoMD5(palabra):
    inicio = time.time()
    md5xd(palabra)
    fin = time.time()
    print("El tiempo de ejecución MD5 LABORATORIO es: ", fin-inicio, "\n")

def sha1xd(palabra):
    inicio = time.time()
    sha1 = hashlib.sha1(palabra.encode())
    fin = time.time()
    entropia = 40*math.log(16,2)
    print("El hash SHA1 de: ",palabra," es: ")
    print(sha1.hexdigest())
    print("La entropia del SHA1",palabra," es: ", entropia,"\n")

def tiempoSHA1(palabra):
    inicio = time.time()
    sha1xd(palabra)
    fin = time.time()
    print("El tiempo de ejecución SHA1 LABORATORIO es: ", fin-inicio, "\n")

def sha256xd(palabra):
    inicio = time.time()
    sha256 = hashlib.sha256(palabra.encode())
    fin = time.time()
    entropia = 64*math.log(16,2)
    print("El hash SHA256 de: ",palabra," es: ")
    print(sha256.hexdigest())
    print("La entropia del SHA256",palabra," es: ", entropia,"\n")

def tiempoSHA256(palabra):
    inicio = time.time()
    sha256xd(palabra)
    fin = time.time()
    print("El tiempo de ejecución SHA256 LABORATORIO es: ", fin-inicio, "\n")

#al recibir el nombre lo convertimos como un string y lo pasamos al hash
def archivo2(palabra):
    inicio = time.time()
    f = open (palabra,'r')
    while(True):
        linea = f.readline()
        if not linea:
            break
        print(linea)
        hash(linea.rstrip())
    f.close()
    fin = time.time()
    print("Tiempo que demoro el hash laboratorio: ", fin-inicio,"\n")

def archivomd5(palabra):
    inicio = time.time()
    f = open (palabra,'r')
    while(True):
        linea = f.readline()
        if not linea:
            break
        md5xd(linea.rstrip())
    f.close()
    fin = time.time()
    print("Tiempo que demoro el hash MD5: ", fin-inicio,"\n")

def archivosha1(palabra):
    inicio = time.time()
    f = open (palabra,'r')
    while(True):
        linea = f.readline()
        if not linea:
            break
        sha1xd(linea.rstrip())
    f.close()
    fin = time.time()
    print("Tiempo que demoro el hash SHA1: ", fin-inicio,"\n")

def archivosha256(palabra):
    inicio = time.time()
    f = open (palabra,'r')
    while(True):
        linea = f.readline()
        if not linea:
            break
        sha256xd(linea.rstrip())
    f.close()
    fin = time.time()
    print("Tiempo que demoro el hash SHA256: ", fin-inicio)

print("La base utilizada es de 74 caracteres y son: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ más salto de linea (, . ; : - _ ! ? ¡ ¿ \" ' )")
print("1.- Ingresar palabra")
print("2.- Ingresar nombre de archivo para hash entrada por entrada de archivo")
decision1 = int(input("Ingrese una opcion: "))

if(decision1 == 1):
    palabra = input("Ingrese una palabra: ")
    tiempo(palabra)
    tiempoMD5(palabra)
    tiempoSHA1(palabra)
    tiempoSHA256(palabra)

elif decision1 == 2:
    nombre = input("Ingrese el path o direccion del archivo: ")
    archivo2(nombre)
    archivomd5(nombre)
    archivosha1(nombre)
    archivosha256(nombre)    

else:
    print("Numero no valido")
