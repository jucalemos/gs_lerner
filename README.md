# LERNER — Assistente do Cidadão

Projeto acadêmico da Global Solution 2026.2 — Pensamento Computacional e Automação com Python.

O LERNER reúne orientações públicas de São Paulo em um assistente simples de terminal. Nesta etapa, o foco é aproximar o cidadão de informações oficiais sobre mobilidade, serviços urbanos e sustentabilidade.

> O LERNER é um projeto acadêmico independente. Não é um canal oficial da Prefeitura de São Paulo e não substitui os canais públicos de atendimento.

## Integrantes
- [Preencher nome e RM do integrante 1]
- [Preencher nome e RM do integrante 2]

## Público e problema
O público são moradores e pessoas que circulam pela cidade de São Paulo. Informações sobre transporte, zeladoria e descarte correto de resíduos ficam distribuídas em diferentes páginas. O assistente organiza orientações iniciais, apresenta a fonte oficial e informa a data em que a equipe conferiu cada conteúdo.

## O que o programa faz
- Carrega uma base de conhecimento JSON.
- Organiza cada orientação em objetos da classe `Orientacao`.
- Usa as classes `BaseConhecimento` e `Assistente`, com composição.
- Pesquisa perguntas em texto livre com normalização e pontuação.
- Permite navegar por categorias.
- Recusa entradas com possível dado pessoal (8 ou mais dígitos ou @).
- Registra atendimentos sem guardar perguntas bloqueadas.
- Calcula indicadores e exporta os atendimentos para CSV.

## Categorias da base
- Mobilidade
- Serviços urbanos
- Sustentabilidade

A base inicial contém 11 orientações. Cada registro tem os campos obrigatórios do enunciado: id, categoria, título, palavras-chave, resposta, documentos, onde, fonte e verificado_em.

## Como executar
É necessário ter Python 3 instalado. Não há bibliotecas externas.

```bash
python main.py
```

O programa cria ou atualiza os arquivos de histórico e CSV na pasta `data/`.

## Estrutura
```
gs_lerner/
├── README.md
├── main.py
├── orientacao.py
├── base_conhecimento.py
├── assistente.py
├── requirements.txt
├── data/
│   ├── base_conhecimento.json
│   ├── historico.json
│   ├── avaliacoes.json
│   └── atendimentos.csv
├── docs/
│   ├── sustentabilidade.md
│   ├── slides_pitch.md
│   ├── roteiro_pitch.md
│   ├── roteiro_video_tecnico.md
│   └── entrega_fiap.txt
└── tests/
    └── teste_basico.py
```

## Regra de pontuação
- +3 pontos para cada palavra-chave da orientação encontrada na pergunta;
- +1 ponto para cada palavra da pergunta com pelo menos 4 letras que também apareça no título;
- 6 pontos ou mais: confiança ALTA;
- de 3 a 5 pontos: confiança MÉDIA;
- menos de 3 pontos: orientação não encontrada.

A busca devolve uma lista de tuplas `(pontos, orientacao)`, em ordem decrescente. O programa exibe a melhor correspondência e até duas alternativas.

## Classes e composição
- `Orientacao`: representa um registro da base e exibe a orientação.
- `BaseConhecimento`: carrega o JSON, lista categorias, filtra e pontua orientações.
- `Assistente`: conversa com o cidadão, registra histórico, calcula indicadores e exporta CSV.

A composição segue a estrutura: `Assistente` possui uma `BaseConhecimento`, que possui uma lista de objetos `Orientacao`.

## Indicadores
O programa calcula percentual de perguntas com orientação encontrada, percentual de atendimentos em que a orientação ajudou, tempo médio, média de tentativas, média da nota de facilidade (1 a 5) e dúvidas sem solução.

## Fontes oficiais
As orientações foram preparadas a partir de páginas da Prefeitura de São Paulo e serviços municipais. A data de conferência registrada na base é 18/11/2026. Como páginas e regras públicas podem mudar, o usuário deve abrir a fonte antes de tomar decisões.

- SP156 — canais de atendimento: https://prefeitura.sp.gov.br/web/inovacao/w/acesso_a_informacao/350229
- Bilhete Único Idoso e Pessoa com Deficiência: https://prefeitura.sp.gov.br/web/mobilidade/w/bu-idoso-e-pcd
- Iluminação pública: https://prefeitura.sp.gov.br/web/spregula/w/iluminacao_publica/renovar/4603
- Avaliação de poda ou remoção de árvores: https://prefeitura.sp.gov.br/w/servico/poda-ou-remocao-de-arvores-ou-vegetacao-em-parques
- Ecopontos e descarte: https://prefeitura.sp.gov.br/sp-mais-limpo
- Coleta seletiva: https://coleta.prefeitura.sp.gov.br/
- Cata-Bagulho: https://prefeitura.sp.gov.br/web/secretaria_executiva_de_limpeza_urbana/w/noticias/284163
- Pátios de compostagem: https://prefeitura.sp.gov.br/web/secretaria_executiva_de_limpeza_urbana/w/patiosdecompostagem

## Relação com os ODS
- ODS 11 — Cidades e Comunidades Sustentáveis: acesso a informações de mobilidade e serviços urbanos.
- ODS 12 — Consumo e Produção Responsáveis: separação de recicláveis, ecopontos e compostagem.
- ODS 13 — Ação Contra a Mudança Global do Clima: incentivo a práticas urbanas com menor impacto ambiental.

Essa relação é uma associação temática feita pela equipe, não uma certificação ou medição de impacto.

## Integração com outras disciplinas
O LERNER é o projeto comum da Global Solution. A base de PCP pode receber, em etapas futuras, informações produzidas na modelagem matemática e em Computer Science. Nesta entrega, a busca por pontuação continua sendo implementada localmente, como exige a disciplina.

## Teste com usuários — PENDENTE
O enunciado exige pelo menos 3 pessoas de fora da equipe e 10 atendimentos ou mais. Não foram inseridos resultados fictícios neste repositório.

Depois de realizar o teste, preencher: número de participantes, total de atendimentos, resposta encontrada (%), ajudou (%), tempo médio, média de tentativas, facilidade média (1 a 5), dúvidas sem solução e melhoria feita a partir do teste.

Não registrar nomes, CPFs, telefones, e-mails ou outras informações pessoais dos participantes.

## Limitações
- A busca é baseada em regras e palavras-chave; não é um modelo de inteligência artificial.
- O programa só responde ao conteúdo cadastrado no JSON.
- O assistente não consulta serviços em tempo real e não abre solicitações em nome do cidadão.
- As informações precisam ser revisadas quando os órgãos públicos atualizarem suas páginas.
- A base inicial é uma seleção de orientações e não cobre todos os bairros, serviços ou situações da cidade.

## Vídeo técnico
Link do vídeo não listado: [inserir link após gravar]

O roteiro obrigatório está em `docs/roteiro_video_tecnico.md`. O vídeo deve ter entre 5 e 8 minutos, mostrar o código e o programa funcionando, e contar com a participação de todos os integrantes. A narração deve ser feita pela própria equipe.

## Testes locais
```bash
python -m unittest discover -s tests
```
