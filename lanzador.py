#!/usr/local/bin/python3.4
__author__ = 'Victor Valotto'
__version__ = '9.1.0'

import adquisidor
import procesador
import visualizador
import persistidor
import utilidades
import modelo
from datetime import datetime
from configurador.configurador import *


class Lanzador():
    """
    Programa Lanzador
    """
    def __init__(self):
        pass

    @staticmethod
    def tecla():
        """
        Funcion que solicita un tecla para continuar
        """
        while True:
            if input('C para continuar> ') == "C":
                break
        return

    @staticmethod
    def informar_versiones():
        os.system("clear")
        titulo = "Versiones de los componentes"
        print(titulo)
        print('*' * len(titulo))
        print("adquisidor: " + adquisidor.__version__)
        print("procesador: " + procesador.__version__)
        print("visualizador: " + visualizador.__version__)
        print("persistidor: " + persistidor.__version__)
        print("modelo: " + modelo.__version__)
        print("utiles: " + utilidades.__version__)
        print()

    @staticmethod
    def ejecutar():
        """
        Se instancian las clases que participan del procesamiento
        """
        try:
            Lanzador.informar_versiones()
            Lanzador.tecla()
            Configurador.inicializar()

            a = Configurador.obtener_tipo("adquisidor")
            p = Configurador.obtener_tipo("procesador")
            v = Configurador.obtener_tipo("visualizador")
            rep_adq = Configurador.obtener_tipo("repositorio_adquisicion")
            rep_pro = Configurador.obtener_tipo("repositorio_procesamiento")

            print(a)
            print(p)
            print(v)
            print(rep_adq)
            print(rep_pro)

            'Obtencion de la señal y guardado'
            print('>')
            print("Incio - Paso 1 - Adquisicion de la señal")
            '''Paso 1 - Se obtiene la señal'''
            a.leer_senial()
            sa = a.obtener_senial_adquirida()
            sa.fecha_adquisicion = datetime.datetime.now().date()
            sa.comentario = input('Descripcion de la señal:')
            sa.id = int(input('Identificacion (nro entero):'))
            print('Fecha de lectura: {0}'.format(sa.fecha_adquisicion))
            print('Cantidad de valores obtenidos {0}'.format(sa.cantidad))
            Lanzador.tecla()
            print('Se persiste la señal adquirida')
            rep_adq.guardar(sa)
            print('Señal Guardada')

            '''Paso 2 - Se procesa la señal adquirida'''
            print('>')
            print("Incio - Paso 2 - Procesamiento")
            para_procesar = rep_adq.obtener(sa.id)
            p.procesar(para_procesar)
            sp = p.obtener_senial_procesada()
            Lanzador.tecla()
            print('Se persiste la señal procesada')
            sp.comentario = input('Descripcion de la señal procesada:')
            sp.id = int(input('Identificacion (nro entero)'))
            rep_pro.guardar(sp)
            print('Señal Guardada')

            '''Paso 3 - Se muestran las seniales '''
            print("Incio - Paso 3 - Mostrar Senial")
            adquirida = rep_adq.obtener(sa.id)
            procesada = rep_pro.obtener(sp.id)
            v.mostrar_datos(adquirida)
            print('----->')
            v.mostrar_datos(procesada)
            print('----->')

        except Exception as ex:
            print(ex.args)
            print("El programa termino con errores")
        finally:
            print("Fin Programa - DIP")


if __name__ == "__main__":
    Lanzador().ejecutar()