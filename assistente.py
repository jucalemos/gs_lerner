import csv
import json
import os
import time
from datetime import datetime


class Assistente:
    def __init__(self, nome, base):
        self.nome = nome
        self.base = base
        self.historico = []
        self.avaliacoes = []
        self.caminho_historico = "data/historico.json"
        self.caminho_avaliacoes = "data/avaliacoes.json"
        self.carregar_historico()

    def carregar_historico(self):
        os.makedirs("data", exist_ok=True)

        try:
            with open(self.caminho_historico, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            if isinstance(dados, dict):
                self.historico = dados.get("atendimentos", [])
            elif isinstance(dados, list):
                self.historico = dados
            else:
                self.historico = []

        except FileNotFoundError:
            self.historico = []
        except json.JSONDecodeError:
            print("O histórico estava vazio ou corrompido. Um novo será criado.")
            self.historico = []

        try:
            with open(self.caminho_avaliacoes, "r", encoding="utf-8") as arquivo:
                self.avaliacoes = json.load(arquivo)

            if not isinstance(self.avaliacoes, list):
                self.avaliacoes = []

        except (FileNotFoundError, json.JSONDecodeError):
            self.avaliacoes = []

    def salvar_historico(self):
        os.makedirs("data", exist_ok=True)

        dados = {
            "atendimentos": self.historico
        }

        with open(self.caminho_historico, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        with open(self.caminho_avaliacoes, "w", encoding="utf-8") as arquivo:
            json.dump(self.avaliacoes, arquivo, ensure_ascii=False, indent=4)

    def tem_dado_pessoal(self, texto):
        quantidade_digitos = 0

        for caractere in texto:
            if caractere.isdigit():
                quantidade_digitos = quantidade_digitos + 1

        if quantidade_digitos >= 8 or "@" in texto:
            return True

        return False

    def registrar(self, origem, pergunta, id_orientacao, encontrou,
                  ajudou, tentativas, tempo):
        atendimento = {
            "data": datetime.now().isoformat(timespec="seconds"),
            "origem": origem,
            "pergunta": pergunta,
            "id_orientacao": id_orientacao,
            "encontrou": encontrou,
            "ajudou": ajudou,
            "tentativas": tentativas,
            "tempo": tempo
        }

        self.historico.append(atendimento)
        self.salvar_historico()

    def perguntar_sim_nao(self, mensagem):
        while True:
            resposta = input(mensagem).strip().lower()

            if resposta == "s":
                return True
            if resposta == "n":
                return False

            print("Digite apenas s para sim ou n para não.")

    def perguntar(self):
        inicio = time.time()
        tentativas = 0
        ultima_pergunta = ""

        while True:
            pergunta = input("\nDigite sua dúvida (0 para voltar): ").strip()

            if pergunta == "0":
                return

            if pergunta == "":
                print("A pergunta não pode ficar vazia.")
                continue

            if self.tem_dado_pessoal(pergunta):
                print("Atenção: não digite CPF, telefone ou e-mail. Reescreva.")
                continue

            ultima_pergunta = pergunta
            tentativas = tentativas + 1
            resultados = self.base.buscar(pergunta)

            if len(resultados) == 0 or resultados[0][0] < 3:
                print("\nNão encontrei uma orientação com confiança suficiente.")
                print("Tente usar outras palavras ou escolha uma categoria no menu.")

                continuar = self.perguntar_sim_nao(
                    "Deseja tentar escrever a pergunta de outra forma? (s/n): "
                )

                if continuar:
                    continue

                tempo = round(time.time() - inicio, 1)
                self.registrar(
                    "pergunta", ultima_pergunta, None, False,
                    False, tentativas, tempo
                )
                return

            pontos, melhor = resultados[0]

            if pontos >= 6:
                confianca = "ALTA"
            else:
                confianca = "MÉDIA"

            print("\nConfiança da resposta: " + confianca + " (" + str(pontos) + " pontos)")
            melhor.exibir()

            if len(resultados) > 1:
                print("\nOutras orientações que podem ajudar:")
                limite = min(3, len(resultados))

                for indice in range(1, limite):
                    pontos_alternativa, alternativa = resultados[indice]
                    if pontos_alternativa >= 3:
                        print("- " + alternativa.titulo)

            ajudou = self.perguntar_sim_nao(
                "\nEssa orientação respondeu sua dúvida? (s/n): "
            )

            tempo = round(time.time() - inicio, 1)
            self.registrar(
                "pergunta", ultima_pergunta, melhor.id, True,
                ajudou, tentativas, tempo
            )
            return

    def navegar(self):
        inicio = time.time()
        categorias = self.base.categorias()

        if len(categorias) == 0:
            print("Não há categorias cadastradas.")
            return

        while True:
            print("\nCategorias disponíveis:")

            for indice, categoria in enumerate(categorias, start=1):
                print(str(indice) + " - " + categoria)

            print("0 - Voltar")

            escolha = input("Escolha uma categoria: ").strip()

            if escolha == "0":
                return

            if not escolha.isdigit():
                print("Digite o número de uma categoria.")
                continue

            numero = int(escolha)

            if numero < 1 or numero > len(categorias):
                print("Opção fora da lista. Tente novamente.")
                continue

            categoria_escolhida = categorias[numero - 1]
            orientacoes = self.base.por_categoria(categoria_escolhida)

            while True:
                print("\n" + categoria_escolhida)

                for indice, orientacao in enumerate(orientacoes, start=1):
                    print(str(indice) + " - " + orientacao.titulo)

                print("0 - Voltar às categorias")

                escolha_orientacao = input("Escolha uma orientação: ").strip()

                if escolha_orientacao == "0":
                    break

                if not escolha_orientacao.isdigit():
                    print("Digite o número de uma orientação.")
                    continue

                numero_orientacao = int(escolha_orientacao)

                if numero_orientacao < 1 or numero_orientacao > len(orientacoes):
                    print("Opção fora da lista. Tente novamente.")
                    continue

                orientacao = orientacoes[numero_orientacao - 1]
                orientacao.exibir()

                ajudou = self.perguntar_sim_nao(
                    "\nEssa orientação respondeu sua dúvida? (s/n): "
                )

                tempo = round(time.time() - inicio, 1)
                pergunta = "Navegação por categoria: " + orientacao.titulo

                self.registrar(
                    "categoria", pergunta, orientacao.id, True,
                    ajudou, 1, tempo
                )
                return

    def avaliar_facilidade(self):
        while True:
            nota = input(
                "\nDe 1 a 5, qual foi a facilidade de usar o assistente? "
                "(0 para pular): "
            ).strip()

            if nota == "0":
                return

            if nota in ["1", "2", "3", "4", "5"]:
                self.avaliacoes.append(int(nota))
                self.salvar_historico()
                print("Avaliação registrada. Obrigado!")
                return

            print("Digite uma nota de 1 a 5 ou 0 para pular.")

    def indicadores(self):
        total = len(self.historico)

        if total == 0:
            return {
                "total": 0,
                "encontradas": 0,
                "ajudou": 0,
                "tempo_medio": 0,
                "tentativas_media": 0,
                "facilidade_media": 0,
                "sem_solucao": []
            }

        encontradas = 0
        ajudou = 0
        soma_tempo = 0
        soma_tentativas = 0
        sem_solucao = []

        for atendimento in self.historico:
            if atendimento["encontrou"]:
                encontradas = encontradas + 1

            if atendimento["ajudou"]:
                ajudou = ajudou + 1

            soma_tempo = soma_tempo + atendimento["tempo"]
            soma_tentativas = soma_tentativas + atendimento["tentativas"]

            if not atendimento["encontrou"] or not atendimento["ajudou"]:
                sem_solucao.append(atendimento["pergunta"])

        if len(self.avaliacoes) > 0:
            facilidade_media = round(
                sum(self.avaliacoes) / len(self.avaliacoes), 1
            )
        else:
            facilidade_media = 0

        return {
            "total": total,
            "encontradas": round(encontradas / total * 100, 1),
            "ajudou": round(ajudou / total * 100, 1),
            "tempo_medio": round(soma_tempo / total, 1),
            "tentativas_media": round(soma_tentativas / total, 1),
            "facilidade_media": facilidade_media,
            "sem_solucao": sem_solucao
        }

    def mostrar_indicadores(self):
        dados = self.indicadores()

        print("\n===== INDICADORES DO LERNER =====")
        print("Total de atendimentos: " + str(dados["total"]))

        if dados["total"] == 0:
            print("Ainda não existem atendimentos registrados.")
            return

        print("Respostas encontradas: " + str(dados["encontradas"]) + "%")
        print("Atendimentos em que ajudou: " + str(dados["ajudou"]) + "%")
        print("Tempo médio: " + str(dados["tempo_medio"]) + " segundos")
        print("Tentativas por atendimento: " + str(dados["tentativas_media"]))
        print("Facilidade média: " + str(dados["facilidade_media"]) + " de 5")

        print("\nDúvidas sem solução:")
        if len(dados["sem_solucao"]) == 0:
            print("- Nenhuma")
        else:
            for pergunta in dados["sem_solucao"]:
                print("- " + pergunta)

    def exportar_csv(self):
        os.makedirs("data", exist_ok=True)

        campos = [
            "data", "origem", "pergunta", "id_orientacao",
            "encontrou", "ajudou", "tentativas", "tempo"
        ]

        with open(
            "data/atendimentos.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()

            for atendimento in self.historico:
                escritor.writerow(atendimento)

        print("\nArquivo data/atendimentos.csv atualizado.")
