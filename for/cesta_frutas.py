#Cria uma lista
fruitBasket = ['laranja', 'maçã', 'banana', 'amora', 'melancia', 'manga', 'morango']
print(fruitBasket)

#Percorre a lista de frutas e imprime cada fruta
for fruit in fruitBasket:
    print(fruit)

#Percorre a lista de frutas e concateca suco de com cada fruta
for fruit in fruitBasket:
    print("suco de", fruit)

#Percorre cada fruta e imprime apenas as que começam com a letra m
for fruit in fruitBasket:
    if fruit.startswith("m"):
        print(fruit)
    else:
        print("")