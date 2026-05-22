echo "# sistema-bancario-em-python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/SidneyXavierFilho1/sistema-bancario-em-python.git
git push -u origin main


saldo = float(1000)
historico = []

while True:
    print("\n--- Banco Eletrônico ---")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - histórico")
    print("5 - sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        print(f"\nSeu saldo é: R${saldo}")

    elif opcao == 2:
        valor = float(input("\nQual o valor do depósito: "))

        if valor > 0:
            saldo += valor
            print(f"\nValor depositado, seu saldo agora é de R${saldo:.2f}")
            historico.append(f"Depósito de R${valor:.2f}")

        else:
            print("\nValor inválido")

    elif opcao == 3:
        valor = float(input("\nQuanto deseja sacar?: "))

        if valor <= 0:
            print("\nValor inválido")

        elif valor > saldo:
            print("\nSaldo insuficiente")

        elif valor <= saldo:
            saldo -= valor
            print(f"\nSaque realizado! Seu saldo agora é de: R${saldo:.2f}")
            historico.append(f"Saque de R${valor:.2f}")

        else:
            print("Saldo insuficiente")

    elif opcao == 4:
        print("\n--- HISTÓRICO DE MOVIMENTAÇÃO ---")
        if len(historico) == 0:
            print("Nenhuma operação foi feita")

        else:
            for item in historico:
                print(item)

    elif opcao == 5:
        print("\nSaindo...")
        break

    else:
        print("\nOpção inválida")



