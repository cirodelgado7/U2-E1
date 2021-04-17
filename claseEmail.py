import re

class Email:  # (Definición de la Clase)
    __idcuenta = ''  # (Atributo)
    __dominio = ''  # (Atributo)
    __tipodominio = ''  # (Atributo)
    __password = ''  # (Atributo)

    def __init__(self, idcuenta=__idcuenta, dominio=__dominio, tipodominio=__tipodominio, password=__password):  # (Constructor)
        self.__idcuenta = idcuenta  # (Inicialización)
        self.__dominio = dominio  # (Inicialización)
        self.__tipodominio = tipodominio  # (Inicialización)
        self.__password = password  # (Inicialización)

    def retornaEmail(self):  # (Método)
        return '' +self.__idcuenta + '@' + self.__dominio + '.' + self.__tipodominio

    def getDominio(self):  # (Método)
       return '' +self.__dominio

    def cambiaContraseña(self):  # (Método)
        c = input('\n Contraseña actual: ')
        if (c==self.__password):
            n = input('\n Contraseña nueva: ')
            self.__password = n
            print('\n Contraseña cambiada con éxito')
            print(' La nueva contraseña es: {} '.format(self.__password))
        else:
            print('\n Contraeña incorrecta')

    def crearObjetoEmail(correo):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.lower()):
            print('\n ****Correo correcto****')
            li = correo.split("@")
            a = li[1].split(".")
            idCuenta = li[0]
            dominio = a[0]
            tipoDominio = a[1]
            password = '123'
            otroEmail = Email(idCuenta, dominio, tipoDominio, password)
            otroEmail.mostrarObjetoCreado()
        else:
            print('\n *****Correo incorrecto*****')

    def mostrarObjetoCreado(self):
        print('Nombre de Cuenta: {}'.format(self.__idcuenta))
        print('Dominio: {}'.format(self.__dominio))
        print('Tipo de Dominio: {}'.format(self.__tipodominio))
        print('Contraseña: {}'.format(self.__password))