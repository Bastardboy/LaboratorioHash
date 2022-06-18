# Laboratorio N°3 Hash

## Caso de Usos

1- Se ha de ingresar una opción (1) Ingresar palabra o (2) Ingresar un archivo

2- Este mensaje/archivo ha de tener carácteres permitidos

3- Los carácteres permitidos están definidos previamente

4- Se efectuan las operaciones definidas en el script

5- Si se elige la opción (1) se entrega el Hash propio de esta con el tiempo y la entropia.

6- Si se elige la opción (2) se entrega el Hash propio y el tiempo que tardo en _Hashear_ el archivo.

El uso que se puede usar para este HASH es el de funcionar como un token, donde al enviar dicho token lo use para confirmar alguna confirmación en el sistema

## Procedimiento

1- Se toma el _String_ ingresado, y se toma los parámetros **Tamaño y Valor** y se verifica si está en el diccionario definido

2- Se bifucar en dos caminos, si cumple que posee 55 caracteres el mensaje, y si no posee los 55 caracteres.

2.1- En caso de no cumplir, primero se le suma +2 y se vuelve a comprobar.

  2.2- Si no lo cumple, se le agrega una letra, al inicio de la palabra ingresada **(mequieropegaruntiromeudeus)**, el valor del largo sería 26, y se le suma 2, entonces sigue sin cumplir que el resto de la división sea igual a 0, por lo cual se le ha de ir agregando una letra al inicio de la palabra.
  
  2.3- En caso de cumplirlo, la palabra, se le agrega una letra al final y se le suma el ciclo (contador) guardado.
  
  2.4- Ahora si la suma es menor o igual al largo del diccionario, el ciclo aumenta y vuelve a realizar este procesamiento de comprobar hasta que se obtenga el largo y   pueda pasar. En caso de que no, se vuelve a realizar el proceso anteriormente mencionado.

3- Ahora una vez que haya pasado la palabra se procede a recorrer el string caracter por caracter. Se convierte el caracter actual en un peso que se le dio en el diccionario, se le ha de sumar el día actual que es entregado de forma [1-31] +5, con la finalidad de hacer un cifrado ROT, el número de ciclos y se ingresa en el arreglo de pesos. Esto ocurre hasta que termina de recorrer todo el string **(mequieropegaruntiromeudeus)**. Cuando se llega al fin del recorrido, se tiene que la variable división pasa y se divide en 55, el contador de este proceso se inicializa en 0, la salida en vacio y se mantiene la suma y el iterador para el ciclo que recorre. Al tener todo esto se toma la primera posición del arreglo con los pesos asignado, y pasamos al instante final.

4- En primer caso ponemos donde se termina de efectuar, si el largo que se estipulo al hash (55) se cumple, aparece la salida representada por un string, además de aparecer en pantalla la entropía de la palabra que sería **341.5199351095923** y finaliza el programa.

  4.1- Si no cumple el largo estipulado se realizan los siguientes pasos, si el largo estipulado +1 es menor al largo del arreglo con pesos, se comprueba si el contador de la división previamente creado es menor en 1 a la división efectuadoa, a la variable suma se le suma el peso en la posición **i** y el contadordivisión es aumentado en 1. Si en vez de que pase esto, se cumple que que es menor en 1 a la división, a la variable suma se le suma el peso en la posición i y contador división pasa a ser 0. Posterior a esto, la suma es menor o igual a la base -1, a la salida se le agrega el caracter del diccionario en la posición suma y avanzamos un caracter, todo esto hasta terminarla. En caso que no ocurra así guardamos la variable suma para comprobar si ahbora es igual a la base, en caso que sí, a la salida se le agrega el caracter del diccionario en la posición de la variable suma, en caso que no la variable num pasa a ser num - 74 y de esta forma logra avanzar un caracter y vuelve al punto de partida para comprobar si el largo cumple y poder apreciar la salida del hash
