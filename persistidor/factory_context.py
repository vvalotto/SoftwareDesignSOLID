from persistidor.contexto import *


class FactoryContextoDatos(object):
    """
    Responsable de crear la clase de contexto de datos
    """
    def __int__(self):
        pass

    @staticmethod
    def obtener_contexto(tipo_contexto, param):

        contexto = None
        if tipo_contexto == 'archivo':
            contexto = ContextoArchivo(param)

        elif tipo_contexto == 'pickle':
            contexto = ContextoPickle(param)

        return contexto