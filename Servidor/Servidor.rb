$:.push('gen-rb')
require 'thrift'
require 'Calculadodra'
require 'servicio_calculadora_types'

class CalculadoraHandler
    def Suma (primerNumero, segundoNumero)
        resultado = Resultado.new()
        resultado.resultado = primerNumero + segundoNumero
        puts("Se ha realizado una Suma")
        return resultado
    end
    
    def Resta(primerNumero, segundoNumero)
        resultado = Resultado.new()
        resultado.resultado = primerNumero - segundoNumero
        puts("Se ha realizado una Resta")
        return resultado
    end

    def Division(primerNumero, segundoNumero)
        resultado = Resultado.new()
        if primerNumero == 0
            resultado.mensajeError = 'ERROR: No se puede dividir entre 0'
            puts("No se puede dividir entre 0")
            return resultado
        else
            resultado.resultado = primerNumero/segundoNumero
        end
        puts("Se ha realizado una division")
        return resultado
    end

    def Multiplicacion(primerNumero, segundoNumero)
        resultado = Resultado.new()
        resultado.resultado = primerNumero*segundoNumero
        puts("Se ha realizado una Multiplicacion")
        return resultado
    end
end

handler = CalculadoraHandler.new()
procesador = Calculadodra::Processor.new(handler)
transporte = Thrift::ServerSocket.new(8080)
transportFactory = Thrift::BufferedTransportFactory.new()
servidor = Thrift::SimpleServer.new(procesador,transporte,transportFactory)

puts 'El servidor esta iniciando'
servidor.serve()
puts 'Iniciado'