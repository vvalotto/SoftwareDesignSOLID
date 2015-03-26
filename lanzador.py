"""
Programa lanzador del ejemplo
"""

from senial_SOLID.lector_senial import *


class Lanzador():
    """
    Programa Principal
    """
    def __init__(self):
        pass

    @staticmethod
    def ejecutar():
        """
        Ejecucion del programa lanzador
        :return
        """
        senial = LectorSenial(10)

        print("Iniciando")
        print("Paso 1")
        senial.leer_senial()
        
        print("Paso 2")
        senial.procesar_senial()
        
        print("Paso 3")
        senial.mostrar_senial()
        
        return

if __name__ == "__main__":
    Lanzador().ejecutar()
