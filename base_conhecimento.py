import json
from orientacao import Orientacao


ACENTOS = {
    "á": "a", "à": "a", "ã": "a", "â": "a",
    "é": "e", "ê": "e", "í": "i",
    "ó": "o", "õ": "o", "ô": "o",
    "ú": "u", "ç": "c"
}


def normalizar(texto):
    texto = texto.lower().strip()

    for letra, troca in ACENTOS.items():
        texto = texto.replace(letra, troca)

    for sinal in "?!.,;:()":
        texto = texto.replace(sinal, " ")

    return " " + " ".join(texto.split()) + " "


class BaseConhecimento:
    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []

    def carregar(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            if not isinstance(dados, list):
                print("A base de conhecimento precisa ser uma lista.")
                return False

            self.orientacoes = []

            for item in dados:
                self.orientacoes.append(Orientacao(item))

            return True

        except FileNotFoundError:
            print("Arquivo da base não encontrado: " + self.caminho)
            return False
        except json.JSONDecodeError:
            print("O arquivo JSON está com algum erro de formatação.")
            return False
        except (KeyError, TypeError):
            print("Existe um registro incompleto na base de conhecimento.")
            return False

    def categorias(self):
        lista = []

        for orientacao in self.orientacoes:
            if orientacao.categoria not in lista:
                lista.append(orientacao.categoria)

        lista.sort()
        return lista

    def por_categoria(self, categoria):
        lista = []

        for orientacao in self.orientacoes:
            if orientacao.categoria == categoria:
                lista.append(orientacao)

        return lista

    def pontuar(self, pergunta, orientacao):
        pergunta_normalizada = normalizar(pergunta)
        titulo_normalizado = normalizar(orientacao.titulo)
        pontos = 0

        for palavra_chave in orientacao.palavras_chave:
            chave_normalizada = normalizar(palavra_chave)

            if chave_normalizada in pergunta_normalizada:
                pontos = pontos + 3

        palavras = pergunta_normalizada.strip().split()
        palavras_unicas = set(palavras)

        for palavra in palavras_unicas:
            if len(palavra) >= 4:
                if " " + palavra + " " in titulo_normalizado:
                    pontos = pontos + 1

        return pontos

    def buscar(self, pergunta):
        resultados = []

        for orientacao in self.orientacoes:
            pontos = self.pontuar(pergunta, orientacao)
            resultados.append((pontos, orientacao))

        resultados.sort(key=lambda item: item[0], reverse=True)
        return resultados
