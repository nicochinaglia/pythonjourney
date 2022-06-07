print("Olá! Seja bem vindo a cafeteria Starcoffes, o que gostaria de pedir?")
print("1 - Capuccino")
print("2 - Expresso")
print("3 - Mocha")
print("4 - Latte")

coffeMap = [
    { "name": "Capuccino", "preço": 5, "temperatura": "quente" },
    { "name": "Expresso", "preço": 2, "temperatura": "quente" },
    { "name": "Mocha", "preço": 8, "temperatura": "gelado" },
    { "name": "Latte", "preço": 10, "temperatura": "gelado" },
]

resp = int(input("informe o café desejado =)"))

if resp == 1:
    print(coffeMap[0])
elif resp == 2:
    print(coffeMap[1])
elif resp == 3:
    print(coffeMap[2])
elif resp == 4:
    print(coffeMap[3])
else:
    while resp != 1 and 2 and 3 and 4:
        resp = int(input("Por favor selecione um café válido!"))

# for coffe in coffeMap:
#     print(coffe["name"])
  
     

