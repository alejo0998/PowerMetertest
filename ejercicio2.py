import json

repetidos = [1,2,3,"1","2","3",3,4,5]

r = [1,"5",2,"3"]

d_str = '{"valor":125.3,"codigo":123}'

#1. Genere una lista con los valores no repetidos de la lista ‘repetidos’.
#2. Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
#3. Transforme ‘d_str’ en un diccionario.


no_repetidos = list(set([int(s) for s in repetidos]))

print(no_repetidos)

valores_comun = list(set([int(s) for s in r]) & set([int(s) for s in repetidos]))

print(valores_comun)

diccionario = json.loads(d_str)

print(diccionario)


#Supongo que habria que pasar todo a int, para quedarme con los no repetidos, por eso converti toda la lista a int