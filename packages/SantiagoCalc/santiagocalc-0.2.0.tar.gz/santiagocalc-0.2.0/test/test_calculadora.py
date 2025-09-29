from SantiagoCalc.calculadora import Calculadora

def probar_suma():
    calc = Calculadora()
    calc.introducir_digito(2)
    calc.introducir_operador('+')
    calc.introducir_digito(3)
    calc.calcular()
    assert calc.valor_actual() == 5, "La suma 2 + 3 debería ser 5"

def probar_resta():
    calc = Calculadora()
    calc.introducir_digito(5)
    calc.introducir_operador('-')
    calc.introducir_digito(2)
    calc.calcular()
    assert calc.valor_actual() == 3, "La resta 5 - 2 debería ser 3"

if __name__ == "__main__":
    probar_suma()
    probar_resta()
    print("Todas las pruebas pasaron correctamente")

