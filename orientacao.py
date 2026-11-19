class Orientacao:
    def __init__(self, dados):
        self.id = dados["id"]
        self.categoria = dados["categoria"]
        self.titulo = dados["titulo"]
        self.palavras_chave = dados["palavras_chave"]
        self.resposta = dados["resposta"]
        self.documentos = dados["documentos"]
        self.onde = dados["onde"]
        self.fonte = dados["fonte"]
        self.verificado_em = dados["verificado_em"]

    def exibir(self):
        print("\n" + self.titulo + " [" + self.categoria + "]")
        print(self.resposta)

        print("\nDocumentos:")
        if len(self.documentos) == 0:
            print("- A página consultada não lista documentos específicos.")
            print("- Confira a fonte oficial antes de iniciar a solicitação.")
        else:
            for documento in self.documentos:
                print("- " + documento)

        print("\nOnde: " + self.onde)
        print("Fonte: " + self.fonte)
        print("Informação conferida em: " + self.verificado_em)
        print("Aviso: este assistente NÃO é um canal oficial.")
