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
2.2- Si no lo cumple, se le agrega una letra, al inicio de la palabra ingresada (HOLA), el valor del largo sería 4, y se le suma 2, entonces sigue sin cumplir que el resto de la división sea igual a 0, por lo cual se le ha de ir agregando una letra al inicio de la palabra

2- Se verifica si el modulo de 55 corresponde a 0 para poder dividirla luego en 55 tener un y tener un numero entero. En caso de que no sea el caso se agregan dos caracteres al inicio y al final de la palabra para poder llegar a efectuar dicha operación. El carácter a elegir se obtiene a partir de la posición de la primera letra más el contador del ciclo. Por ultimo se verifica si el número del carácter está dentro del diccionario, si no es así se ubica la primera posición y se calcula otra vez. El string resultante es palabra

3- Se toma la palabra generada, se hace las divisones correspondientes, y se ocupa el valor del día actual, para hacer un corrimiento dentro de esta

4- También se genera un nuevo arreglo, el cual contiene los pesos y se suma con la variable del día actual anteriormente mencionada.

5- Y por último se generan variables que han de usarse para guardar los valores de los pesos, y posterior generación de la palabra

6- Por último, para obtener la generación del hash, se suma cada _contadordivision_ obteniendo un valor y posteriormente dicho valor es transformado para que se logre ubicar dentro del diccionario. Dicha transformación tiene que volver a la posición inicial del diccionario cada vez que llegue al final de diccionario. Una vez que se tiene la posición para los valores establecidos, se va guardando dentro de la variable salida, y después repetimos el ciclo para ir generando el hash

7- Para obtener la entropía del _hash_ básicamente se hace uso de la operación matemática para obtenerlo.

8- Se resalta que se aplica funciones de los hashes _MD5_, _SHA1_, _SHA256_ para comprobar el tema de los tiempos.
