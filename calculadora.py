def calculadora():
    try:
        num1 = float(input("Introduce el primer número"))
        num2 = float(input("Introduce el segundo número"))
        operacion = input("Elige una operacion(+, -, *, /): ")
        
        if operacion  =="+":
            resultado = num1 + num2
            print(f"El resultado de {num1} + {num2} es: {resultado}")

        elif operacion == "-":
            resultado = num1 - num2
            print(f"El resultado de {num1} - {num2} es: {resultado}")

        elif operacion == "*":
            resultado = num1 - num2
            print(f"El resultado de {num1} * {num2} es: {resultado}")

        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de {num1} / {num2} es: {resultado}")
            else:
                print("Error: No se puede dividir por cero.")
            
        else:
            print("Operacíon no válida. Por favor, elige entre+, -, *, /.")
    
    except ValueError:
        print("Errór: Entrada no válida. Por favor, introduce un número.")
calculadora()

