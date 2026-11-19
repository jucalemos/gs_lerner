from base_conhecimento import BaseConhecimento
from assistente import Assistente


def main():
    print("======================================")
    print("       LERNER - ASSISTENTE CIDADÃO")
    print("======================================")
    print("Orientações sobre São Paulo, mobilidade e sustentabilidade.")
    print("Este projeto não é um canal oficial da Prefeitura.")

    base = BaseConhecimento("data/base_conhecimento.json")
    carregou = base.carregar()

    if not carregou:
        print("Não foi possível carregar a base. Confira o arquivo JSON.")
        return

    assistente = Assistente("LERNER", base)

    while True:
        print("\nO que você deseja fazer?")
        print("1 - Digitar uma dúvida")
        print("2 - Navegar por categorias")
        print("3 - Ver indicadores")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            assistente.perguntar()
        elif opcao == "2":
            assistente.navegar()
        elif opcao == "3":
            assistente.mostrar_indicadores()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 0.")

    assistente.avaliar_facilidade()
    assistente.exportar_csv()
    assistente.mostrar_indicadores()
    print("\nObrigada por utilizar o LERNER!")


if __name__ == "__main__":
    main()
