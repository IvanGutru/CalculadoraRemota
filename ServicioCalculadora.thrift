struct Resultado {1: double resultado, 2: string mensajeError,}


service Calculadodra{
    Resultado Suma( 1: double primerNumero, 2: double segundoNumero)
    Resultado Resta( 1: double primerNumero, 2: double segundoNumero)
    Resultado Division( 1: double primerNumero, 2: double segundoNumero)
    Resultado Multiplicacion(  1: double primerNumero, 2: double segundoNumero)
    
}