import json


class AnaliseEnergia:
    def __init__(self, caminho="data/analise_energia.json"):
        self.caminho = caminho
        self.dados = {}

    def carregar(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                self.dados = json.load(arquivo)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            print("Não foi possível carregar os dados da análise energética.")
            return False

    def calcular(self, potencia_w):
        premissas = self.dados["premissas"]
        horas = premissas["horas_por_dia"]
        dias = premissas["dias_por_ano"]
        tarifa = premissas["tarifa_b4a_reais_por_kwh"]

        consumo_anual = potencia_w / 1000 * horas * dias
        custo_anual = consumo_anual * tarifa

        return consumo_anual, custo_anual

    def mostrar_analise(self):
        if len(self.dados) == 0 and not self.carregar():
            return

        print("\n===== ANÁLISE DE ENERGIA: ILUMINAÇÃO PÚBLICA =====")
        print("Estudo de caso: São Paulo - um ponto de luz")
        print("Premissa de funcionamento: 12 horas por dia, durante 365 dias.")
        print("Tarifa de referência B4a: R$ 0,43416 por kWh.")
        print("Os valores são estimativas por ponto, não a conta real da Prefeitura.")

        resultados = {}

        for alternativa in self.dados["alternativas"]:
            consumo, custo = self.calcular(alternativa["potencia_w"])

            if alternativa["id"] == "led_solar":
                custo_rede = 0
                consumo_rede = 0
                print("\n" + alternativa["nome"])
                print("Carga elétrica da luminária: " + str(alternativa["potencia_w"]) + " W")
                print("Energia anual necessária: " + str(round(consumo, 2)) + " kWh")
                print("Energia comprada da rede no cenário solar idealizado: 0 kWh")
                print("Custo anual de energia da rede no cenário: R$ 0,00")
                print("Economia estimada na conta em relação ao LED ligado à rede: R$ " +
                      str(round(resultados["led_rede"]["custo"], 2)))
                resultados[alternativa["id"]] = {
                    "consumo": consumo_rede,
                    "custo": custo_rede
                }
            else:
                print("\n" + alternativa["nome"])
                print("Potência total: " + str(alternativa["potencia_w"]) + " W")
                print("Consumo anual estimado: " + str(round(consumo, 2)) + " kWh")
                print("Custo anual estimado: R$ " + str(round(custo, 2)))
                resultados[alternativa["id"]] = {
                    "consumo": consumo,
                    "custo": custo
                }

        sodio = resultados["sodio"]
        led = resultados["led_rede"]
        economia_kwh = sodio["consumo"] - led["consumo"]
        economia_reais = sodio["custo"] - led["custo"]
        economia_percentual = economia_kwh / sodio["consumo"] * 100

        print("\n===== COMPARAÇÃO SÓDIO x LED NA REDE =====")
        print("Energia economizada por ponto/ano: " + str(round(economia_kwh, 2)) + " kWh")
        print("Redução estimada do consumo: " + str(round(economia_percentual, 2)) + "%")
        print("Economia estimada por ponto/ano: R$ " + str(round(economia_reais, 2)))
        print("\nPara simular uma quantidade de pontos, digite um número inteiro.")
        quantidade = input("Quantidade de luminárias (0 para voltar): ").strip()

        if quantidade.isdigit() and int(quantidade) > 0:
            total = int(quantidade)
            print("Economia anual estimada para " + str(total) + " pontos: R$ " +
                  str(round(economia_reais * total, 2)))
            print("Energia economizada por ano: " +
                  str(round(economia_kwh * total, 2)) + " kWh")

        print("\nHistórico público usado como contexto:")
        for registro in self.dados["historico_publico"]:
            print("- " + registro["data"] + ": " + registro["descricao"])

        print("\nLimitações importantes:")
        for limitacao in self.dados["limitacoes"]:
            print("- " + limitacao)

        print("\nFontes:")
        for fonte in self.dados["fontes"]:
            print("- " + fonte["nome"] + ": " + fonte["url"])
