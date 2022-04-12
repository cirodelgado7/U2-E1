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
    E1 = Email()
    E1.crearObjetoEmail('informatica.fcefn@gmail.com')
    E2 = Email()
    E2.crearObjetoEmail('wicc2019@unsj-cuim.edu')
    E3 = Email()
    E3.crearObjetoEmail('juanLiendro1957@yahoo.com')
    archivo = open('Correos.csv')
    reader = csv.reader(archivo, delimiter=';')
    d = input('\n Ingrese el Nombre de la Cuenta: ')
    L = []
    for fila in reader:
        correo = fila[0] + fila[1] + fila[2] + "." + fila[3]
        E4 = Email()
        E4.crearObjetoEmail(correo)
        L.append(E4)
    c = 0
    for i in range(len(L)):
        if L[i].retornaEmail() == d:
            c = c + 1
    if (c > 1):
        print('\n La cuenta ingresada está repetida')
    else:
        print('\n La cuenta ingresada no está repetida')
    archivo.close()
