"""Se o número for múltiplo de 3, imprime Fizz.
Se o número for múltiplo de 5, imprime Buzz
Se o número for múltiplo de 3 E 5, imprime FizzBuzz
Se não for nenhum, imprime o próprio número"""

i = int(input(("Digite o número: ")))
if (i%3 == 0 and i%5 == 0):
    print("FizzBuzz")
elif (i%5 == 0):
    print("Buzz")
elif (i%3 == 0):
    print("Fizz")
else:
    print(i)
