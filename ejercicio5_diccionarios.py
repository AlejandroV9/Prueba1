'''
Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
'''
def ingresaUsuario():
    dic1={}
    for i in range(3):
        id=int(input("ingrese el id del usuario: "))
        name=input("ingrese el nombre asociado al id: ")
        dic1[id]=name
    return dic1

def mostrarDic1(dic1):
    for value in dic1:
        print(value, dic1[value])


def consultarDic1(dic1):
    numConsultar=int(input("Ingrese el numero a consultar"))
    if  numConsultar in dic1:
        print("el nombre asociado al numero es",dic1[numConsultar]) 
    else:
        print("no se encontro el numero")

dic1=ingresaUsuario()
mostrarDic1(dic1)
consultarDic1(dic1)

