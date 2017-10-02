print('========================================')
print('===      VERIFICADOR DE DESCONTO     ===')
print('=================V1.0===================')

valor = float(input("Digite o valor do produto: "))

print("----ESCOLHA A FORMA DE PAGAMENTO----")
print("A vista no dinheiro:(1)")
print("A vista no cartao:  (2)")
print("Parcelado até 2x:   (3)")
print("Parcelado 3x ou +   (4)")
opcao = int(input(" "))

if opcao == 1:
    result = valor-((valor/100)*10)
    print("O valor total é R${}" .format(result))
elif opcao == 2:
    result = valor - ((valor / 100) * 5)
    print("O valor total é R${}".format(result))
elif opcao == 3:
    result = valor/2
    print("Você pagará 2x de R${}".format(result))
elif opcao == 4:
    parcela = int(input("Deseja dividir em quantas vezes? "))
    result = valor + ((valor / 100) * 20)
    valor_parcela = result / parcela
    print("Você irá pagar {}x de  R${}".format(parcela, valor_parcela))
    print("Valor do juros por mês: R${}" .format((valor/100)*20/parcela))
    print("Valor total: R${}" .format(result))
else:
    print("Opção invalida! ")
