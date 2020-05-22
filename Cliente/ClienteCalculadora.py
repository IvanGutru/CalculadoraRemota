
import sys
sys.path.append('gen-py')
from ServicioCalculadora import Calculadodra
from ServicioCalculadora import ttypes
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

# def main():



transport = TSocket.TSocket('localhost',8080)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
cliente = Calculadodra.Client(protocol)


transport.open()
def resulta(resultado):
    if(resultado != None):
        print("El resultado es: ")
        print(resultado.resultado)
    else:
        print("El resultado es: ")
        print(resultado.mensajeError)

bandera = True
while bandera:
    print("\t MENU ")
    print("1.- Realizar suma ")
    print("2.- Realizar resta ")
    print("3.- Realizar division ")
    print("4.- Realizar multiplicacion ")
    print("5.- Salir")
    opcion = int(input("Selecciona una opcion: "))

    if opcion == 1:
        primerNumero = int(input("Ingresa el primer numero: "))
        segundoNumero = int(input("Ingresa el segundo numero: "))
        resulta(cliente.Suma(primerNumero, segundoNumero))
    elif(opcion == 2):
        primerNumero = int(input("Ingresa el primer numero: "))
        segundoNumero = int(input("Ingresa el segundo numero: "))
        resulta(cliente.Resta(primerNumero, segundoNumero))
    elif(opcion == 3):
        primerNumero = int(input("Ingresa el primer numero: "))
        segundoNumero = int(input("Ingresa el segundo numero: "))
        resulta(cliente.Division(primerNumero, segundoNumero))
    elif(opcion == 4):
        primerNumero = int(input("Ingresa el primer numero: "))
        segundoNumero = int(input("Ingresa el segundo numero: "))
        resulta(cliente.Multiplicacion(primerNumero, segundoNumero))
    elif(opcion == 5):
        break
    else:
        print("Elige una opción del 1 al 5")
transport.close()


    




