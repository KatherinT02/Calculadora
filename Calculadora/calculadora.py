def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

try:
    x= float(input("Ingrese el primer numero: "))
    y= float(input("Ingrese el segundo numero: "))

    print("Suma:", sumar(x, y))
    print("Resta:", restar(x, y))
    print("Multiplicacion:", multiplicar(x, y))
    print("Division:", dividir(x, y))

except ValueError:
    print("Error: Debe ingresar solo numeros.")

except ZeroDivisionError as e:
    print("Error:", e)
