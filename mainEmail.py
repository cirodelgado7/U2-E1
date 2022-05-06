from claseEmail import Email

if __name__ == '__main__':
    unEmail = Email()  # (Instanciación de un Objeto Email)
    unEmail.retornaEmail()  # (Mensaje o Llamada al método)
    unEmail.cambiaPassword()  # (Mensaje o Llamada al método)
    unEmail.testEmail()  # (Mensaje o Llamada al método)
    lista = unEmail.abrirArchivo()  # (Mensaje o Llamada al método)
    unEmail.verificarEmail(lista)  # (Mensaje o Llamada al método)
