# variaveis de contagem
excelente = 0
ruim = 0

# Estrutura de repetição para 10 entrevistados
for i in range(50):
    print(f"\n--- Entrevistado {i + 1} ---")

    # coleta de dados do entrevistado
    nome_entrevistado = input("digite o seu nome: ") 
    idade_entrevistado = input("digite a sua idade: ")

    # coleta de opiniao do entrevistado
    print("1 - EXCELENTE") 
    print("2 - BOM")
    print("3 - RUIM") 
    qual_sua_opiniao_sobre_o_atendimento = input("digite o numero correspondente: ").strip()

    if qual_sua_opiniao_sobre_o_atendimento == "1":
        print("voce avaliou o atendimento como EXCELENTE")
        excelente = excelente + 1

    elif qual_sua_opiniao_sobre_o_atendimento == "2": 
        print("voce avaliou o atendimento como BOM")

    elif qual_sua_opiniao_sobre_o_atendimento == "3":
        print("voce avaliou o atendimento como RUIM")
        ruim = ruim + 1  

# exibiçao dos dados coletados dos entrevistados (FORA do for)
print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de entrevistados que avaliaram o atendimento como EXCELENTE: {excelente}")
print(f"Quantidade de entrevistados que avaliaram o atendimento como RUIM: {ruim}")