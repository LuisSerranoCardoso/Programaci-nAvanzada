import numpy as np

class MatrizFloat:

    """
    Clase que representa una matriz dinámica 1D/2D

    Atributos de clase:
        TIPO_DATO #Tipo de dato por defecto (np.float32)

    Atributos de isntancia (protegidos):
        matriz #Almacena la matriz (Utilice numpy)
        nfil   #Almacena número de filas de la matriz (int)
        ncol   #Almacena número de columnas de la matriz (int)
    """

    def __init__(...):
        """
        Inicializador. No recibe parámetros adicionales.
        Inicializa el atributo matriz con None y los atributos nfil y ncol a 0
        """

        pass

    def matriz_identidad(...):
        """
        Método de clase que crea y devuelve una nueva
        instancia de MatrizFloat configurada como matriz
        identidad de tamaño n x n

        Parámetros:
            El tamaño de n de la matriz devuelve:
                Nueva instancia con matriz identidad creada
                (MatrizFloat)
        """"

        #NOTA: Utilice "eye" de numpy para crear la matriz identidad

        pass

def mismas_dimensiones(...)
    """
    Método para comparar dimensiones.

    Parámetros:
        m1  #Primera matriz a comparar (MatrizFloat)
        m2  #Segunda matriz a comparar (MatrizFloat)

    Devuelve:
        bool: True si ambas matrices tienen el mismo número de
        filas y columnas, y False en caso contrario
        (o si alguna no está creada)
    """

    pass

def crear_matriz2D(...):
    """
    Método para crear una matriz unidimensional de ceros.
    Usa crear_matriz2D para asignar 1 fila y n columnas.
    Parámetros:
        nElementos: Número de elementos de la fila (int)
    """

    pass

def existe(...):
    """
    Método que verifica si matriz está creada y no está vacía
    Devuelve:
        True si existe, de los contrario False
    """

    pass

def introducir(...):
    """
    Método que solicita por consola el valor numérico decimal
    para cada posición (i, j) de la matriz.

    Da error si se intenta introducir datos sin haber creado
    matriz previamente,
    """

    pass

def mostrar(...):
    """
    Método apra mostrar las dimensiones y los elementos de la
    matriz. Si la matriz no existe (existe() == False), muestra
    un mensaje advirtiendolo
    """

#=============================================================
# OPERARIONES ALGEBRAICAS
#=============================================================

def sumar_matrices(...):
    """
    Método que suma la matriz actual con otra matriz.

    Parámetros:
        otra_matriz: objeto de MatrizFloat con la matriz a sumar

    Devuelve:
        Un nuevo objeto MatrizFloat con la matriz resultante de
        la suma.
    """

    #Nota: Las dimensiones de ambas matrices deben coincidir.

    pass

def restar_matrices(...):
    """
    Método que resta la matriz actual con otra matriz.

    Parámetros:
        otra_matriz: objeto de MatrizFloar con la matriz restar

    Devuelve:
        Un nuevo objero MatrizFloar con la matriz resultante de
        la resta
    """

    #Nota: Las dimensiones de ambas matrices deben coincidir

    pass
