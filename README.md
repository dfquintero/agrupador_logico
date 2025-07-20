# Agrupador lógico
## Nombres
-_**Quintero Gómez Diego Fernando**_

-_**Hernández Ortegón Joan Nicolás**_

-_**Castro Castillo Juan David**_
## Instalación
- _**Paso #1:**_ Ve a la sección `Releases`.

<img width="341" height="92" alt="Releases" src="https://github.com/user-attachments/assets/6aa733e8-6d07-4c5b-b79d-052e0eabb0f6" />
  
- _**Paso #2:**_ Descarga el archivo `agrupador_logico.exe`.
- _**Paso #3:**_ Ejecuta el archivo `agrupador_logico.exe`.

## Interfaz 
<img width="669" height="516" alt="Interfaz" src="https://github.com/user-attachments/assets/3caad84a-3e0d-40cb-9c06-c9a054a61bfe" />


- _**1. Cuadro de entrada:**_ En este espacio se ve reflejada la expresión lógica ingresada por el usuario que debe esta conformado por proposiciones (representadas por letras) y operadores lógicos que son ingresados desde el panel de botones [2].
- _**2. Panel de botones:**_ En este panel encontrarás cinco botones asignados a distintos operadores lógico y dos botones para el paréntesis de apertura y cierre respectivamente, con estos botones se podrán ingresar de forma simple las expresiones lógicas. Adicionalmente, esta el botón **Procesar** con el que se puede hacer funcionar el programa .
- _**3. Cuadro de salida:**_ En este espacio se podrá ver el resultado y los pasos de lo que fue ingresado en el cuadro de entrada [1] al momento de presionar el botón procesar en el panel de botones [2].
- _**4. Salida del código LaTex:**_ En este espacio se genera una traducción del resultado final del cuadro de salida [3] al lenguaje LaTex y al lado un botón que permite copiarlo.
## Funcionamiento

La principal función de este proyecto es (como su nombre lo indica) agrupar secciones de una expresión lógica ingresada por el usuario mediante el uso de paréntesis y llevarla a su forma bien formulada, lo que facilita la resolución y comprensión de la misma, para eso es necesario tener en cuenta elementos como la prioridad y el orden de los operadores lógicos.

<img width="647" height="359" alt="Orden operadores" src="https://github.com/user-attachments/assets/55a6a14a-78a1-4b2b-9b89-75c50f7ab550" />


En la siguiente imagen se puede observar cómo en el caso de que haya varios operadores iguales o de la misma prioridad, el programa los agrupa en un orden de izquierda a derecha:

<img width="482" height="448" alt="Orden operadores 2" src="https://github.com/user-attachments/assets/ce15923b-0fc5-4082-a112-d68e2d0664cf" />



Al ingresar la expresión lógica hay que ser cuidadosos con la ubicación de los operadores lógicos, los paréntesis y las proposiciones, puesto que cuando el programa detecta cierto error en la ubicación de estos elementos no mostrara los pasos ni los resultados en el cuadro de salida si no que mostrara un mensaje de error como se muestra a continuación:  

<img width="487" height="454" alt="Error" src="https://github.com/user-attachments/assets/b5e73424-d548-41a1-84a1-e754f6214af3" />


Otra de las funciones del proyecto es traducir el resultado final a lenguaje LaTex, por lo que es necesario cambiar los operadores lógicos por su equivalente a este lenguaje.

<img width="643" height="361" alt="LaTex" src="https://github.com/user-attachments/assets/1a15b31d-4f52-484b-a4d6-ff43f1e7e934" />


Cuando el cuadro de salida [2] muestra los pasos, el resultado y ningún error, puedes dirigirte a la parte inferior y presionar el botón de **copiar** para obtener la expresión del resultado en LaTex.

<img width="491" height="446" alt="LaTex 2" src="https://github.com/user-attachments/assets/4b2bde82-cae3-4437-a16c-dd72ac24737e" />


Esto permite pegar la expresión facilmente, mostrándose de la siguiente forma:

<img width="300" height="42" alt="LaTex 3" src="https://github.com/user-attachments/assets/916a3307-77d8-4152-9fd9-f9323b705eae" />


## Video

https://youtu.be/Lu3jEutbmoo
[![](https://markdown-videos.deta.dev/youtube/Lu3jEutbmoo)]
