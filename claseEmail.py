import csv
import re


class Email:  # (Definición de la Clase)

    __idcuenta = ''  # (Atributo)
    __dominio = ''  # (Atributo)
    __tipodominio = ''  # (Atributo)
    __password = ''  # (Atributo)

    def __init__(self, idcuenta="", dominio="", tipodominio="", password=""):  # (Constructor)
        self.__idcuenta = idcuenta  # (Inicialización)
        self.__dominio = dominio  # (Inicialización)
        self.__tipodominio = tipodominio  # (Inicialización)
        self.__password = password  # (Inicialización)

    def retornaEmail(self):  # (Método)
        nombre = input('\n Nombre: ')  # Ingreso de datos por teclado
        self.__idcuenta = input(' Nombre de Cuenta: ')  # Ingreso de datos por teclado
        self.__dominio = input(' Dominio: ')  # Ingreso de datos por teclado
        self.__tipodominio = input(' Tipo de Dominio: ')  # Ingreso de datos por teclado
        self.__password = input(' Contraseña: ')  # Ingreso de datos por teclado
        correo = self.__idcuenta + '@' + self.__dominio + '.' + self.__tipodominio
        print('\n Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, correo))

    def getDominio(self):  # (Método)
        return self.__dominio

    def getIdCuenta(self):  # (Método)
        return self.__idcuenta

    def cambiaPassword(self):  # (Método)
        print('\n Cambio de Contraseña')
        c = input('\n Contraseña actual: ')
        if c == self.__password:
            n = input('\n Contraseña nueva: ')
            self.__password = n
            print('\n Contraseña cambiada con éxito')
            print(' La nueva contraseña es: {} '.format(self.__password))
        else:
            print('\n Contraeña incorrecta')

    def crearObjetoEmail(self, correo):  # (Método)
        print('\n Creación de Objetos de la clase Email')
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.lower()):
            print('\n ****Correo correcto****')
            li = correo.split("@")
            a = li[1].split(".")
            self.__idcuenta = li[0]
            self.__dominio = a[0]
            self.__tipodominio = a[1]
            self.__password = '123'
            self.mostrarObjetoCreado()
        else:
            print('\n *****Correo incorrecto*****')

    def mostrarObjetoCreado(self):  # (Método)
        print('Nombre de Cuenta: {}'.format(self.__idcuenta))
        print('Dominio: {}'.format(self.__dominio))
        print('Tipo de Dominio: {}'.format(self.__tipodominio))
        print('Contraseña: {}'.format(self.__password))

    def testEmail(self):  # (Método)
        E1 = Email()  # (Instanciación del Objeto)
        E1.crearObjetoEmail('informatica.fcefn@gmail.com')  # (Mensaje o Llamada al método)
        E2 = Email()  # (Instanciación del Objeto)
        E2.crearObjetoEmail('wicc2019@unsj-cuim.edu')  # (Mensaje o Llamada al método)
        E3 = Email()  # (Instanciación del Objeto)
        E3.crearObjetoEmail('juanLiendro1957@yahoo.com')  # (Mensaje o Llamada al método)

    def abrirArchivo(self):
        archivo = open('Correos.csv')
        reader = csv.reader(archivo, delimiter=';')
        L = []
        for fila in reader:
            correo = fila[0]
            E4 = Email()
            E4.crearObjetoEmail(correo)
            L.append(E4)
        archivo.close()
        return L

    def verificarEmail(self, L):
        d = input('\n Ingrese el Nombre de la Cuenta: ')
        c = 0
        for i in range(len(L)):
            if L[i].getIdCuenta() == d:
                c = c + 1
        if c == 1:
            print('\n El Nombre de la Cuenta si está repetido')
        else:
            print('\n El Nombre de la cuenta no está repetido')
