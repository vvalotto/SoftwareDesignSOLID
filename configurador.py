"""
Configura la clase que se usara
"""
from procesador.procesador import *
from adquisidor.adquisidor import *
from visualizador.visualizador import *
from persistidor.repositorio import *
from persistidor.contexto import *
from modelo.senial import *


def definir_senial_adquirir():
    return SenialPila()


def definir_senial_procesar():
    return SenialPila()


def definir_procesador():
    return Procesador( definir_senial_procesar())


def definir_adquisidor():
    return AdquisidorArchivo('/Users/voval/tmp/adquisidor/datos.txt', definir_senial_adquirir())


def definir_visualizador():
    return Visualizador()


def definir_contexto(recurso):
    return ContextoPickle(recurso)


def definir_repositorio(contexto):
    return RepositorioSenial(contexto)


class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    ctx_datos_adquisicion = definir_contexto('/Users/voval/tmp/adquisidor')
    ctx_datos_procesamiento = definir_contexto('/Users/voval/tmp/datos/pro')

    rep_adquisicion = definir_repositorio(ctx_datos_adquisicion)
    rep_procesamiento = definir_repositorio(ctx_datos_procesamiento)

    adquisidor = definir_adquisidor()  # Se configura el tipo de adquisidor
    procesador = definir_procesador()  # Se configura el tipo de procesador
    visualizador = definir_visualizador()  # Se configura el visualizador

    def __init__(self):
        pass
