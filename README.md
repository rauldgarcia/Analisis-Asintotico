**ANÁLISIS ASINTÓTICO**

Tarea 3.

Programar un algoritmo de su elección (no tan sencillo) y analizarlo de la siguiente forma:

1) Graficar tiempo de ejecución en función de N.
1) Graficar dos cotas superiores y 2 cotas inferiores sobre los mismos ejes.
1) Repetir el punto 1 y 2 ejecutando el programa en otra computadora de mayores o menores capacidades de distinto desempeño.
1) Analizar los resultados y discutirlos. Escribir de la manera mas completa las características de las dos computadoras:
   1. Sistema operativo.
   1. RAM (generación y velocidad).
   1. HDD/SDD.
   1. CPU (Ghz, nucleos, generación).
1) Obtener conclusiones que relacionan las graficas obtenidas.

El algoritmo escogido para la realización del análisis asintótico es una red neuronal artificial de tres capas, la primera capa cuenta con tres neuronas, la segunda capa cuenta con dos neuronas y la capa final cuenta con tres neuronas. Las neuronas de la segunda y tercer capa utilizan la función sigmoidal. La red se entrena con el algoritmo backpropagation para que las entradas X1=1.0, X2=0.25, X3=-0.5 obtengan las salidas O1=1.0, O2=0.5, O3=0. La implementación se realizo basado en el articulo “Artificial Neural Networks for Beginners”  de Carlos Gershenson.

![](Aspose.Words.62734dee-e27e-4deb-bb45-76342f30ca8e.001.png)

La grafica naranja corresponde al comportamiento de ejecución del programa Y=n. La grafica azul es la cota superior Y=n1.5.

La grafica rosa es la cota superior Y=2(n/3).

La grafica gris es la cota inferior Y=0.5n.

La grafica morada es la cota inferior Y=n/10.

Primero se ejecuto en una computadora con las siguientes características:

MSI GF63-Thin-9SCX

- Sistema operativo: Ubuntu 22.04, x86\_64
- RAM: 16 Gb DDR4-2666 MHz
- HDD: 200 Gb 300 Mb/s
- CPU: Intel Core i5-9300H @ 2.40 Ghz, 4 núcleos con 8 subprocesos, 14 nm.
- GPU: Nvidia GeForce GTX 1650 4 Gb GDDR5 1024 cuda cores 1.25 GHz

![](Aspose.Words.62734dee-e27e-4deb-bb45-76342f30ca8e.002.png)

Como se puede ver en la grafica el tiempo de ejecución del programa es de aproximadamente 0.37 para 25 iteraciones del algoritmo haciendo que sea un algoritmo lineal en función del numero de iteraciones que realiza.

Posteriormente se ejecuto en una computadora con las siguientes características:

MSI GF63-Thin-9SCX

- Sistema operativo: Windows 10, x86\_64
- RAM: 16 Gb DDR4-2666 MHz
- SDD: 238 Gb 2100 Mb/s
- CPU: Intel Core i5-9300H @ 2.40Ghz, 4 núcleos con 8 subprocesos, 14 nm.
- GPU: Nvidia GeForce GTX 1650 4 Gb GDDR5 1024 cuda cores 1.25 GHz

![](Aspose.Words.62734dee-e27e-4deb-bb45-76342f30ca8e.003.png)

A pesar de que el programa se corre en la misma computadora, cambiando solamente el sistema operativo y la unidad de almacenamiento (Ubuntu corre en un disco duro y Windows en un disco de estado solido), los resultados en el caso de Windows son de 0.77 segundos de ejecución, por lo cual se puede ver que aun corriendo en una unidad de almacenamiento de mayor velocidad (7 veces mas rápido), el tiempo de procesamiento es mayor,  lo que es el doble de tiempo comparado a que si corriera en Ubuntu. 

HP 14-CM0XX

- Sistema operativo: Windows 10, x86\_64
- RAM: 4 Gb DDR4-1866 MHz
- SDD: 1 Tb 150 Mb/s
- CPU: AMD A6-9225 @ 2.6 GHz, 2 nucleos con 2 subprocesos, 28nm.

![](Aspose.Words.62734dee-e27e-4deb-bb45-76342f30ca8e.004.png)

Como se puede observar en el grafico el tiempo de ejecución en esta computadora es de 1.15 segundos, que si se comparan con los 0.77 y 0.37, se puede notar que es el que tiene mayor tiempo de ejecución, ademas se puede notar como hay mayor espacio entre cierto puntos, esto debido a que el programa tardaba a procesar la información mas tiempo entre una iteración y la siguiente. Finalmente se puede llegar a la conclusión que mientras mas potente y rápida sea la computadora, mas rápido se ejecutara el código, tomando en cuenta el hecho de que ese tiempo de ejecución se vera afectado dependiendo el sistema operativo que lo corra.
