struct Resultado {
    1: double resultado;
    2: string mensajeError;
}


service Calculadora {
    Resultado Sumar( 1: double numeroUno, 2: double numeroDos)
    Resultado Restar( 1: double numeroUno, 2: double numeroDos)
    Resultado Multiplicar(  1: double numeroUno, 2: double numeroDos)
    Resultado Dividir( 1: double numeroUno, 2: double numeroDos)
}
