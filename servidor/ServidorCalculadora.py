import sys
sys.path.append('gen-py')

from thrift.transport import TSocket
from thrift.server import TServer
from Calculadora import Calculadora
from Calculadora.ttypes import Resultado
class CalculadoraHandler(Calculadora.Iface):
    def Sumar(self,numeroUno,numeroDos):
        resultado = Resultado()
        resultado.resultado = numeroUno + numeroDos
        return resultado
    
    def Restar(self,numeroUno,numeroDos):
        resultado = Resultado()
        resultado.resultado = numeroUno - numeroDos
        return resultado 

    def Multiplicar(self,numeroUno,numeroDos):
        resultado = Resultado()
        resultado.resultado = numeroUno * numeroDos
        return resultado 


    def Dividir(self,numeroUno,numeroDos):
        resultado = Resultado()
        if numeroDos == 0:
            resultado.resultado = 0
            resultado.mensajeError = "No se puede dividir entre 0"
        else:
            resultado.resultado = numeroUno/numeroDos
        return resultado 

if __name__ == "__main__": 
    transporte_servidor = TSocket.TServerSocket(port=8080)
    procesador = Calculadora.Processor(CalculadoraHandler())
    servidor = TServer.TSimpleServer(procesador, transporte_servidor)
    print("Servicio de calculadora iniciado")
    servidor.serve()
    
