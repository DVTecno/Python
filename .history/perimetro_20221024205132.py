

print(""" Calcular el área y perímetro
      de un rectángulo
      y de un círculo.  """)
alto = float(input("indique el alto rectángulo:"))
ancho = float(input("indique el ancho del rectángulo:"))
area=alto*ancho
perimetro=2*(alto+ancho)
print(f"El valor del área del rectángulo es: {area}")
print(f"El valor del perímetro del rectángulo es: {perimetro}")
pi=3.1416
radio = float(input("indique el radio del círculo:"))
area=pi*radio**2
perimetro=area

