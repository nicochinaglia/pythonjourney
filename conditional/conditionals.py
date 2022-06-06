#Challenge: 2 numbers and compare if the first number is the same, higher ow lower with the second number.

numberOne = int(input("Informe um valor:\n"))
numberTwo = int(input("Informe o segundo valor:\n"))

if numberTwo > numberOne:
    print("O segundo valor é maior que o primeiro valor")
elif numberTwo < numberOne:
    print("O segundo valor é menor que o primeiro valor")
else:
    print("Os valor são iguais!!")