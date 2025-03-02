def calculadora(): #def serve para definir parametros no codigo para deixa-lo mais organizado
  while True:     #while True serve para repetir o codigo
    num1 = float(input("Digite o primeiro número: "))
    op = input("Digite o operador mtemático: ")
    num2 = float(input("Digite o segundo número: "))

    if op == '+':
        resultado = num1 + num2
        print("{} {} {} = {}" .format(num1, op, num2, resultado))
        
    elif op == '-':
        resultado = num1 - num2
        print("{} {} {} = {}" .format(num1, op, num2, resultado))
        
    elif op == '/':
        resultado = num1 / num2
        print("{} {} {} = {}" .format(num1, op, num2, resultado))
              
    elif op == '*':
        resultado = num1 * num2
        print("{} {} {} = {}" .format(num1, op, num2, resultado))
        
    else:
        print("Por favor, digite um operador válido.")
    break
calculadora() #aqui eu fechei o def ou seja finalizei uma função e para evitar repetiçoes posso chamar o def novamente  




