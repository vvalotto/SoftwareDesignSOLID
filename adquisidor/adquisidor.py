"""
Se modifica la clase base y se extiende con la clase abstracta trazador
"""
from abc import ABCMeta, abstractmethod
from modelo.senial import *
from utiles.trazador import *


class BaseAdquisidor(BaseTrazador, metaclass=ABCMeta):
    """
    Clase Abstracta Adquisidor
    """
    def __init__(self, senial):
        """
        Inicializa el adquisidor con una lista vacia de valores de la senial
        :valor: Tamanio de la coleccion de valores de la senial
        """
        self._senial = senial

    def obtener_senial_adquirida(self):
        """
        Devuelve la lista de valores de la senial adquirida
        :return: senial
        """
        return self._senial

    @abstractmethod
    def leer_senial(self):
        """
        Metodo abstracto. Cada adquisidor tiene su propia implementacion
        de la lectura de la senial
        """
        pass

    @abstractmethod
    def _leer_dato_entrada(self):
        pass

    def trazar(self, entidad, accion, mensaje):
        """
        Registra un evento asociado a la proceso de adquisicion
        entidad: clase que genera el evento
        accion: metodo o funcion en la que se genera el evento
        mensaje: Comentario
        """
        nombre = 'adquisidor_logger.log'
        try:
            with open(nombre, 'a') as logger:
                logger.writelines('------->\n')
                logger.writelines('Accion: ' + str(accion) + '\n')
                logger.writelines(str(entidad) + '\n')
                logger.writelines(str(datetime.datetime.now()) + '\n')
                logger.writelines(str(mensaje) + '\n')
        except IOError as eIO:
            raise eIO


class AdquisidorSimple(BaseAdquisidor):
    """
    Adquisidor de datos desde el teclado
    """
    def _leer_dato_entrada(self):
        """
        Lee un dato por teclaso
        :return: dato leido
        """
        dato = 0
        while True:
            try:
                dato = float(input('Valor:'))
                break
            except ValueError:
                print('Dato mal ingresado, <enter>')
            finally:
                return dato

    def leer_senial(self):
        """
        llena la coleccion de valores de la senial desde el teclado
        :return:
        """
        print("Lectura de la senial")
        for i in range(0, self._senial.tamanio):
            print("Dato nro:" + str(i))
            self._senial.poner_valor(self._leer_dato_entrada())
        return


class AdquisidorArchivo(BaseAdquisidor):
    """
    Adquisidor de datos desde Archivo
    """
    def __init__(self, ubicacion, senial):
        """
        Inicializa la instancia con la ubicacion del archivo a leer
        :param ubicacion:
        """
        BaseAdquisidor.__init__(self, senial)
        if isinstance(ubicacion, str):
            self._ubicacion = ubicacion
        else:
            super().trazar(AdquisidorArchivo,
                           'Inicializacion',
                           'El dato no es de una ubicacion valida, (No es un nombre de archivo')
            raise Exception('El dato no es de una ubicacion valida, (No es un nombre de archivo')
        return

    @property
    def ubicacion(self):
        return self._ubicacion

    def _leer_dato_entrada(self):
        pass

    def leer_senial(self):
        print('Lectura de la senial')
        print(self._ubicacion)
        try:
            with open(self._ubicacion, 'r') as a:
                for linea in a:
                    dato = float(linea)
                    self._senial.poner_valor(dato)
                    print(dato)
        except IOError as ex:
            super().trazar(AdquisidorArchivo,
                           'leer_senial',
                           'I/O Error: ' + str(ex))
            raise 'I/O Error'
        except ValueError as ex:
            super().trazar(AdquisidorArchivo,
                           'leer_senial',
                           'Dato de senial no detectado: ' + str(ex))
            print('Dato de senial no detectado')
            raise ex
        except Exception as ex:
            super().trazar(AdquisidorArchivo,
                            'leer_senial',
                           'Error en la carga de datos: ' + str(ex))
            print('Error en la carga de datos')
            raise ex
