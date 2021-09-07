## random  

Este módulo implementa generadores de números pseudoaleatorios para varias distribuciones.


## Números aleatorios 

random.**seed**(*a=None*, *version=2*)

Inicializa el generador de números aleatorios.  

Si *a* es omitido o None, se utilizará la hora actual del sistema. Si las fuentes de aleatoriedad vienen del sistema operativo, éstas se usarán en vez de la hora del sistema.  

Si *a* es un entero, se usará directamente.  
Con la versión 2 (la versión por defecto), un objeto str, bytes, o bytearray se convierte en int y se usarán todos sus bits.


