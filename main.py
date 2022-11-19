print("================CALCULADORA================\n")
n1 = int(input("Digite o primeiro número: "))
func = str(input("Função: "))
n2 = int(input("Digite o segundo número: "))

if func == '*':
    print( n1 * n2)
elif func == '/':
    print( n1 / n2)
elif func == '+':
    print( n1 + n2)
elif func == '-':
    print( n1 - n2)
else:
    print("função inválida")