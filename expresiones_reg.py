import re

texto='''Hola mundo
Me gusta Python!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercer numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123
Caracteres especiales permitidos: \.,-_+\*@$#%&"
'''

#buscar el primer numero emparejamiento
print(re.search(r'\d',texto, flags=re.M))#I

#buscar todos los emparejamientos
print(re.findall(r'\d',texto))