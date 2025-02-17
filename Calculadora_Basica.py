# Calculadora basica
# Operaciones: SUMA, RESTA, MULTIPLICACIÓN, DIVISION, MÓDULO, SUMATORIA, FACTORIAL.

def calculadora():
    while True:
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicacion")
        print("4.Division")
        print("5.Modulo")
        print("6.Sumatoria")
        print("7.Factorial")
        print("8.Salir")

        opcion = input("Ingresa una opcion: ")

        if opcion == "8":
            print("nos vemos")
            break

        num1 = int(input("ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))

        if opcion == "1":
            resultado = num1 + num2 
            print('el resultado de la suma es: ', resultado)

        elif opcion == "2":
            resultado = num1 - num2
            print('el resultado de la resta es: ', resultado)

        elif opcion == "3":
            resultado = num1 * num2
            print("El resultado de la multiplicación es:", resultado)
        
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 // num2 
                print('el resultado de la division es: ', resultado)
            else:
                print('no se puede dividir por cero')

        elif opcion == "5":
            resultado = num1 % num2
            print('el resultado del modulo es: ', resultado)
        
        elif opcion == "6":
            resultado = sum(range(int(num1), int(num2)+1))
            print('el resultado de la sumatoria es: ', resultado)
        
        elif opcion == "7":
            resultado = 1
            for i in range(1, int(num1)+1):
                resultado *= i 
            print('el resultado del factorial es: ', resultado)

        else:
            print("opcion invalida. Intente de nuevo")

calculadora()