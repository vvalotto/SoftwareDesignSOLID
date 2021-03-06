"""
Configura la clase que se usara
"""
from xml.dom import minidom
from modelo.factory_senial import *
from procesador.factory_procesador import *
from adquisidor.factory_adquisidor import *
from visualizador.visualizador import *
from persistidor.repositorio import *
from persistidor.factory_context import *


def obtener_dir_datos():
    try:
        conf = minidom.parse("./datos/configuracion.xml")
        dir_datos = conf.getElementsByTagName("dir_recurso_datos")[0]
        return dir_datos.firstChild.data
    except IOError as ex:
        raise ex


def obtener_senial_config(senial_config):
    try:
        # Parsea el xml de configuracion
        conf_procesador = minidom.parse("./datos/configuracion.xml")
        # Busca el nodo de la senial para adquirir
        item_senial_adquirida = conf_procesador.getElementsByTagName(senial_config)[0]
        # Obtiene el nombre del tipo de senial
        senial = item_senial_adquirida.firstChild.data.strip()
        # Busca los nodos de los parametros
        item_tamanio = item_senial_adquirida.getElementsByTagName("tamanio")[0]
        # Llena la lista con los parametros asociados a la senial
        tamanio = item_tamanio.firstChild.data.strip()
        return senial, tamanio
    except Exception as ex:
        raise ex


def obtener_filtros_config(filtro_config):
    """
    Recupera desde la configuración el tipo de procesador y los
    parametros asociado
    Luego llama la factory para que devuelva el tipo de procesador creado
    """
    try:
        # Parsea el xml de configuracion
        conf_filtro = minidom.parse("./datos/configuracion.xml")
        # Busca el nodo del procesador
        item_filtro = conf_filtro.getElementsByTagName(filtro_config)[0]
        # Obtiene el nombre del tipo de procesador definido
        filtro = item_filtro.firstChild.data.strip()
        # Busca los nodos de los parametros
        item_params = item_filtro.getElementsByTagName("param")
        # Llena la lista con los parametros asociados al procesador
        params = []
        for param in item_params:
            params.append(param.firstChild.data)
        return filtro, params
    except Exception as ex:
        raise ex


def definir_senial_adquirir():
    try:
        senial, tamanio = obtener_senial_config("senial_adq")
        return FactorySenial.obtener_senial(senial, tamanio)
    except Exception as ex:
        raise ex


def definir_senial_procesar():
    try:
        senial, tamanio = obtener_senial_config("senial_pro")
        return FactorySenial.obtener_senial(senial, tamanio)
    except Exception as ex:
        raise ex


def definir_procesador():
    """
    Recupera desde la configuración el tipo de procesador y los
    parametros asociado
    Luego llama la factory para que devuelva el tipo de procesador creado
    """
    try:
        procesador, params = obtener_filtros_config("procesador")
        # Crea el procesador
        return FactoryProcesador.obtener_procesador(procesador,
                                                    definir_senial_procesar(),
                                                    params)
    except Exception as ex:
        raise ex


def definir_adquisidor():
    """
    Recupera desde la configuración el tipo de adquisidor y los
    parametros asociado
    Luego llama la factory para que devuelva el tipo de adquisidor creado
    """
    try:
        adquisidor, params = obtener_filtros_config("adquisidor")
        # Crea el procesador
        return FactoryAdquisidor.obtener_adquisidor(adquisidor,
                                                    definir_senial_adquirir(),
                                                    params)
    except Exception as ex:
        raise ex


def definir_visualizador():
    return Visualizador()


def definir_contexto(recurso):
    """
    Recupera desde la configuración el tipo de adquisidor y los
    parametros asociado
    Luego llama la factory para que devuelva el tipo de adquisidor creado
    """
    try:
        # Parsea el xml de configuracion
        conf_adquisidor = minidom.parse("./datos/configuracion.xml")
        # Busca el nodo del contexto
        item_contexto = conf_adquisidor.getElementsByTagName("contexto")[0]
        contexto = item_contexto.firstChild.data.strip()
        # Crea el contexto
        return FactoryContexto.obtener_contexto(contexto, recurso)
    except Exception as ex:
        raise ex


def definir_repositorio(contexto, tipo_senial):
    return RepositorioSenial(contexto, tipo_senial)


class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    componentes = {}

    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    titulo = "Configuración de los objetos que participan"
    print(titulo)
    print('*' * len(titulo))
    print()

    @staticmethod
    def inicializar():
        Configurador.agregar("adquisidor", definir_adquisidor())
        Configurador.agregar("procesador", definir_procesador())
        Configurador.agregar("visualizador", definir_visualizador())
        Configurador.agregar("contexto_datos_adquiridos", definir_contexto(obtener_dir_datos() + '/adq'))
        Configurador.agregar("contexto_datos_procesados", definir_contexto(obtener_dir_datos() + '/pro'))
        Configurador.agregar("repositorio_adquisicion",
                             definir_repositorio(Configurador.obtener_tipo("contexto_datos_adquiridos"),
                                                 definir_senial_adquirir()
                                                )
                             )
        Configurador.agregar("repositorio_procesamiento",
                             definir_repositorio(Configurador.obtener_tipo("contexto_datos_procesados"),
                                                 definir_senial_procesar()
                                                )
                             )
        return

    @staticmethod
    def agregar(tipo, clase):
        Configurador.componentes[tipo] = clase

    @staticmethod
    def obtener_tipo(tipo):
        return Configurador.componentes[tipo]
