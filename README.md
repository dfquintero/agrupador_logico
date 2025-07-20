# Agrupador lógico
## Requerimientos
## Instalación
## Interfaz 
<img width="669" height="516" alt="Interfaz" src="https://github.com/user-attachments/assets/e3efd209-fcaf-42e6-bb33-39ebf4f08b80" />

- _**1. Cuadro de entrada:**_ En este espacio se ve reflejada la expresión lógica ingresada por el usuario que debe esta conformado por proposiciones (representadas por letras) y operadores lógicos que son ingresados desde el panel de botones [2].
- _**2. Panel de botones:**_ En este panel encontrarás cinco botones asignados a distintos operadores lógico y dos botones para el paréntesis de apertura y cierre respectivamente, con estos botones se podrán ingresar de forma simple las expresiones lógicas. Adicionalmente, esta el botón **Procesar** con el que se puede hacer funcionar el programa .
- _**3. Cuadro de salida:**_ En este espacio se podrá ver el resultado y los pasos de lo que fue ingresado en el cuadro de entrada [1] al momento de presionar el botón procesar en el panel de botones [2].
- _**4. Salida del código LaTex:**_ En este espacio se genera una traducción del resultado final del cuadro de salida [3] al lenguaje LaTex y al lado un botón que permite copiarlo.
## Funcionamiento

La principal función de este proyecto es (como su nombre lo indica) agrupar secciones de una expresión lógica ingresada por el usuario mediante el uso de paréntesis y llevarla a su forma bien formulada, lo que facilita la resolución y comprensión de la misma, para eso es necesario tener en cuenta elementos como la prioridad y el orden de los operadores lógicos.

<img width="647" height="359" alt="Orden operadores" src="https://github.com/user-attachments/assets/f1d44066-cc1a-464f-87e9-a0a2ae96534f" />

En la siguiente imagen se puede observar cómo en el caso de que haya varios operadores iguales o de la misma prioridad, el programa los agrupa en un orden de izquierda a derecha:

<img width="482" height="448" alt="Orden operadores 2" src="https://github.com/user-attachments/assets/d62a583b-61de-4a5b-9e2f-3ff948487f69" />


Al ingresar la expresión lógica hay que ser cuidadosos con la ubicación de los operadores lógicos, los paréntesis y las proposiciones, puesto que cuando el programa detecta cierto error en la ubicación de estos elementos no mostrara los pasos ni los resultados en el cuadro de salida si no que mostrara un mensaje de error como se muestra a continuación:  

<img width="487" height="454" alt="Error" src="https://github.com/user-attachments/assets/914e7f0b-30fd-4ff0-806c-b0fe59c9a887" />

Otra de las funciones del proyecto es traducir el resultado final a lenguaje LaTex, por lo que es necesario cambiar los operadores lógicos por su equivalente a este lenguaje.

<img width="643" height="361" alt="LaTex" src="https://github.com/user-attachments/assets/6260f703-0402-48a7-9223-2ad5bb977625" />

Cuando el cuadro de salida [2] muestra los pasos, el resultado y ningún error, puedes dirigirte a la parte inferior y presionar el botón de **copiar** para obtener la expresión del resultado en LaTex.

<img width="491" height="446" alt="LaTex 2" src="https://github.com/user-attachments/assets/031cd9a4-4070-4116-a0cf-a0a6c795ea31" />

Esto permite pegar la expresión facilmente, mostrándose de la siguiente forma:

<img width="300" height="42" alt="LaTex 3" src="https://github.com/user-attachments/assets/84964992-cb2c-40d3-ac3b-a40f57b2e410" />

## Video
