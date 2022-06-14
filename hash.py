from datetime import date
from datetime import datetime
import math
import time

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
    #verificamos si el primer caracter se encuentra en el diccionario
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
                contador = contador + 2
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
    newlen = int(len(palabra))
    division = int(newlen/55)
    today = date.today()
    today = today.day + 5

    #generamos el arreglo que contiene los pesos y verificamos si el caracter actual se encuentra en el diccionario
    new_palabra = []
    count = 1
    for i in palabra:
        new_palabra.append(int(diccionario.get(i))+today+count)
        count = count + 1
    
    #YA GENERADOS LOS PESOS EN EL ARREGLO SE PROCEDE A CONVERTILOS A PALABRA
    contadordivision = 0
    salida = ""
    suma = 0

    #convertimos los numeros a letras ajustandolos al hash
    for i in range(newlen):
        if(contadordivision == division-1):
            suma = suma + new_palabra[i] 
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
            suma = suma + new_palabra[i]
            contadordivision = contadordivision + 1
    

    print("El hash de: ",original," es: ")
    print(salida)
    entropia(salida)


#la entropia se calcula como el largo de la palabra ingresada por el logaritmo en base 2 de la base utilizada:
def entropia(palabra):
    numeros = "0123456789"
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    especial = "  , . ; : - _ ! ? ¡ ¿ \" ' "

    size = len(palabra)

    flag = True
    contador = 0
    n = 0
    l = 0
    e = 0

    contador = 0
    while(flag):
        if(contador + 1) < size:
            contador = contador + 1
            if numeros.count(palabra[contador]) > 0 : n = 10 
            if letras.count(palabra[contador]) > 0 : l = 52 
            if especial.count(palabra[contador]) > 0 : e = 13

            if(n!=0 and l!=0 and e!=0):
                flag = False
        else:
            flag = False

    numerobase = n+l+e
    logaritmo = math.log(numerobase,2)
    entropia = logaritmo
    print("La entropia de ",palabra," es: ", entropia) 


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
    print(fin - inicio) 

print("La base utilizada es de 74 caracteres y son: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ más salto de linea (, . ; : - _ ! ? ¡ ¿ \" ' )")
print("1.- Ingresar palabra")
print("2.- Ingresar nombre de archivo para hash entrada por entrada de archivo")
decision1 = int(input("Ingrese una opcion: "))

if(decision1 == 1):
    palabra = input("Ingrese una palabra: ")
    hash(palabra)
 
        
elif decision1 == 2:
    nombre = input("Ingrese el path o direccion del archivo: ")
    archivo2(nombre)
    

else:
    print("Numero no valido")