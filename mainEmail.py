import csv
from claseEmail import Email

if __name__ == '__main__':
    nombre = input('\n Nombre: ')  # Ingreso de datos por teclado
    idCuenta = input(' Nombre de Cuenta: ')
    dominio = input(' Dominio: ')
    tipoDominio = input(' Tipo de Dominio: ')
    password = input(' Contraseña: ')
    unEmail = Email(idCuenta, dominio, tipoDominio, password)
    print('\n Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, unEmail.retornaEmail()))
    print('\n Cambio de Contraseña')
    unEmail.cambiaContraseña()  # (Mensaje)
    print('\n Creación de Objetos de la clase Email')
    Email.crearObjetoEmail('informatica.fcefn@gmail.com')
    Email.crearObjetoEmail('wicc2019@unsj-cuim.edu')
    Email.crearObjetoEmail('juanLiendro1957@yahoo.com')
    archivo = open('Correos.csv')
    reader = csv.reader(archivo,delimiter=';')
    d = input('\n Ingrese el dominio: ')
    c=0
    for fila in reader:
        if fila[2]==d:
            c+=1
    print('Cantidad de dominios iguales: {}'.format(c))
    archivo.close()
