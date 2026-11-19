# LERNER — Assistente do Cidadão

Projeto acadêmico da Global Solution 2026.2, desenvolvido em Python.

O LERNER reúne orientações públicas de São Paulo em um assistente de terminal. A proposta conecta informações sobre mobilidade, serviços urbanos e sustentabilidade.

> O LERNER é um projeto acadêmico independente. Não é um canal oficial da Prefeitura de São Paulo e não substitui os canais públicos de atendimento.

## Integrantes
- Júlia Lemos Souza — 569089
- Erick Yu Xiang Li — 569305

## Público e problema
O público são moradores e pessoas que circulam pela cidade de São Paulo. Informações sobre transporte, serviços urbanos, descarte correto e uso de energia ficam distribuídas em diferentes páginas. O assistente organiza orientações iniciais e apresenta as fontes consultadas.

## O que o programa faz
- Carrega uma base de conhecimento em JSON.
- Organiza cada orientação em objetos da classe `Orientacao`.
- Usa as classes `BaseConhecimento` e `Assistente`, com composição.
- Pesquisa perguntas em texto livre com normalização e pontuação.
- Permite navegar por categorias.
- Apresenta uma análise de consumo, custos e economia para iluminação pública, incluindo uma alternativa com energia solar.
- Bloqueia perguntas com oito ou mais dígitos ou com o caractere @. Essa verificação é simples e não identifica todos os tipos possíveis de dado pessoal.
- Registra atendimentos, calcula indicadores e exporta os registros para CSV.

## Categorias da base atual
- Mobilidade
- Serviços urbanos
- Sustentabilidade

A base contém 12 orientações. Cada registro possui id, categoria, título, palavras-chave, resposta, documentos, onde, fonte e data de verificação.

## Como executar
É necessário ter Python 3 instalado. O projeto utiliza apenas bibliotecas que já fazem parte do Python, então não precisa de `requirements.txt`.

```bash
python main.py
```

No menu, escolha a opção 4 para abrir a análise de energia da iluminação pública. O programa utiliza `data/base_conhecimento.json` e `data/analise_energia.json`. Durante a execução, cria ou atualiza os arquivos de histórico, avaliações e CSV na pasta `data/`.

## Estrutura atual
```
gs_lerner/
├── README.md
├── main.py
├── orientacao.py
├── base_conhecimento.py
├── assistente.py
├── energia.py
├── data/
│   ├── base_conhecimento.json
│   ├── analise_energia.json
│   ├── historico.json
│   ├── avaliacoes.json
│   ├── atendimentos.csv
│   ├── historico_teste_simulado.json
│   └── avaliacoes_teste_simuladas.json
└── tests/
    └── teste_basico.py
```

## Regra de pontuação
- +3 pontos para cada palavra-chave da orientação encontrada na pergunta;
- +1 ponto para cada palavra da pergunta com pelo menos 4 letras que também apareça no título;
- 6 pontos ou mais: confiança alta;
- de 3 a 5 pontos: confiança média;
- menos de 3 pontos: orientação não encontrada.

A busca retorna uma lista de tuplas com a pontuação e o objeto da orientação, em ordem decrescente.

## Classes e composição
- `Orientacao`: representa um registro da base e exibe a orientação.
- `BaseConhecimento`: carrega o JSON, lista categorias, filtra e pontua orientações.
- `Assistente`: controla a conversa, registra o histórico, calcula indicadores e exporta CSV.
- `AnaliseEnergia`: carrega as premissas energéticas, calcula consumo/custo e apresenta a comparação.

A composição segue esta estrutura: `Assistente` possui uma `BaseConhecimento`, que possui uma lista de objetos `Orientacao`.

## Sustentabilidade — iluminação pública de São Paulo

A necessidade estudada é fornecer iluminação noturna às ruas e espaços públicos, com menor consumo de energia e avaliação de alternativas renováveis. O estudo compara três cenários para um ponto de luz.

### Dados técnicos e premissas
O Guia para Iluminação Pública do Inmetro/PUCRS (2021) apresenta um exemplo laboratorial com:
- Luminária a vapor de sódio: potência total de 310 W (lâmpada + reator) e fluxo luminoso de 19.900 lm.
- Luminária LED: potência total de 120 W (driver + módulo) e fluxo luminoso de 18.500 lm.

Os fluxos são próximos, mas não idênticos. O guia ressalta que a escolha real precisa considerar o projeto luminotécnico e a classificação da via, não apenas a potência.

Para a simulação, foram adotadas 12 horas de funcionamento por dia e 365 dias por ano. A tarifa de referência é a B4a: TUSD de R$ 259,83/MWh + TE de R$ 174,33/MWh = R$ 434,16/MWh, ou R$ 0,43416/kWh. A página da Enel informa vigência a partir de 04/07/2026. A Nota Técnica 009/2021 da Controladoria Geral do Município identifica a B4a como tarifa aplicável à iluminação pública.

### Cálculo por ponto de luz
Fórmula do consumo anual:

`Consumo (kWh/ano) = Potência (W) ÷ 1.000 × 12 horas/dia × 365 dias`

`Custo anual = Consumo anual × R$ 0,43416/kWh`

| Cenário | Consumo anual | Custo anual estimado da energia da rede |
|---|---:|---:|
| Vapor de sódio, 310 W | 1.357,80 kWh | R$ 589,50 |
| LED conectado à rede, 120 W | 525,60 kWh | R$ 228,19 |
| LED solar, carga de 120 W | 525,60 kWh de energia necessária; 0 kWh comprados da rede no cenário idealizado | R$ 0,00 de energia comprada da rede no cenário idealizado |

A troca do exemplo de sódio pelo LED conectado à rede reduz o consumo calculado em 832,20 kWh por ano por ponto, ou 61,29%. A economia estimada na conta é de R$ 361,31 por ponto ao ano.

No cenário solar, a luminária continua precisando de 525,60 kWh por ano, mas essa energia seria fornecida pelo painel fotovoltaico e pela bateria. O valor zero representa apenas a energia comprada da rede, supondo que o sistema solar consiga atender toda a carga. Não significa que a energia seja gratuita: o equipamento solar tem investimento, manutenção e componentes que precisam ser substituídos.

### Viabilidade e impactos
- LED conectado à rede: aproveita a infraestrutura elétrica existente e reduz o consumo em relação ao exemplo de vapor de sódio.
- LED solar autônomo: pode ser interessante em locais sem rede elétrica ou em ampliações onde levar cabos seria caro. Em ruas já atendidas pela rede, o custo inicial, a bateria, a manutenção e a proteção dos equipamentos precisam ser avaliados antes de decidir.
- Impactos ambientais: LED reduz a energia consumida no cenário comparado. A energia solar é renovável durante a operação, mas painéis e baterias também exigem materiais, fabricação, manutenção e descarte correto.

Não foi encontrado um orçamento comparável e específico para instalar um sistema solar de 120 W em São Paulo. Por isso, o repositório não inventa preço de compra nem calcula payback. O custo mostrado é o custo estimado de energia da rede, não o custo total de propriedade.

### Histórico municipal
- Até julho de 2021, a SP Regula informou que 541 mil pontos haviam sido remodelados ou ampliados com LED, equivalentes a 88,5% do parque, com economia de 52% no consumo energético da cidade.
- Em maio de 2022, o Tribunal de Contas do Município registrou 613 mil luminárias substituídas e mais de 99% da rede modernizada.

Esses são marcos históricos publicados nas datas indicadas, não números atuais de 2026.

### Limitações
A potência e o fluxo luminoso são exemplos técnicos de laboratório, não um inventário das luminárias atuais de São Paulo. O uso de 12 horas por noite é uma premissa simplificadora. A tarifa é uma referência B4a; a cobrança efetiva depende do enquadramento e das condições de faturamento. O cenário solar não dimensiona painel, bateria ou autonomia. Não foram calculadas emissões de carbono nem impactos de ciclo de vida. A análise não substitui projeto luminotécnico profissional nem a verificação da norma aplicável.

## Testes simulados e testes reais
Os arquivos `data/historico_teste_simulado.json` e `data/avaliacoes_teste_simuladas.json` contêm exemplos fictícios, autorizados pela equipe, para demonstrar o formato dos registros e exercitar a leitura de resultados. Eles ficam separados do histórico real e estão identificados como simulação. Não são entrevistas ou testes realizados com pessoas reais e não cumprem, por si só, a validação solicitada pelo professor.

O enunciado pede testes com usuários, com registro das situações testadas, comentários e ajustes realizados. Essa etapa ainda precisa ser feita com pessoas reais. Não registrar nomes nem dados pessoais desnecessários.

## Indicadores
O programa calcula o percentual de perguntas com orientação encontrada, o percentual de atendimentos em que a orientação ajudou, o tempo médio, a média de tentativas, a média das avaliações de facilidade e as dúvidas sem solução.

## Fontes
- SP Regula — História da Iluminação Pública: https://prefeitura.sp.gov.br/web/spregula/w/iluminacao_publica/historia/312
- Tribunal de Contas do Município — Iluminação Pública e Crimes: https://observatorio.tcm.sp.gov.br/Urbanismo/216553/167271
- Inmetro/PUCRS — Guia para Iluminação Pública, volume 1 (2021): https://www.gov.br/inmetro/pt-br/centrais-de-conteudo/publicacoes/cartilhas/guia-ip-vol1.pdf
- Enel São Paulo — Tarifas de energia elétrica: https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html
- Controladoria Geral do Município — Nota Técnica 009/2021: https://www.prefeitura.sp.gov.br/cidade/secretarias/upload/controladoria_geral/NotaT%C3%A9cnica_009_2021_vfinal.pdf
- Prefeitura de Ferraz de Vasconcelos — Termo de Referência de iluminação solar: https://ferrazdevasconcelos.sp.gov.br/web/wp-content/uploads/2025/07/TR-CE13-EDITAL-41.pdf

## Testes locais
```bash
python -m unittest discover -s tests
```
