# LERNER — Assistente do Cidadão

Projeto acadêmico da Global Solution 2026.2, desenvolvido em Python.

O LERNER reúne orientações públicas de São Paulo em um assistente de terminal. A proposta conecta informações sobre mobilidade, serviços urbanos e sustentabilidade.

> O LERNER é um projeto acadêmico independente. Não é um canal oficial da Prefeitura de São Paulo e não substitui os canais públicos de atendimento.

## Integrantes
- Júlia Lemos Souza — [preencher RM]
- Erick Yu Xiang Li — [preencher RM]

## Público e problema
O público são moradores e pessoas que circulam pela cidade de São Paulo. Informações sobre transporte, serviços urbanos e descarte correto ficam distribuídas em diferentes páginas. O assistente organiza orientações iniciais e apresenta a fonte de cada informação.

## O que o programa faz
- Carrega uma base de conhecimento em JSON.
- Organiza cada orientação em objetos da classe `Orientacao`.
- Usa as classes `BaseConhecimento` e `Assistente`, com composição.
- Pesquisa perguntas em texto livre com normalização e pontuação.
- Permite navegar por categorias.
- Bloqueia perguntas com oito ou mais dígitos ou com o caractere @. Essa verificação é simples e não identifica todos os tipos possíveis de dado pessoal.
- Registra atendimentos, calcula indicadores e exporta os registros para CSV.

## Categorias da base atual
- Mobilidade
- Serviços urbanos
- Sustentabilidade

A base inicial contém 11 orientações. Cada registro possui id, categoria, título, palavras-chave, resposta, documentos, onde, fonte e data de verificação.

## Como executar
É necessário ter Python 3 instalado. O projeto utiliza apenas bibliotecas que já fazem parte do Python, então não precisa de `requirements.txt`.

```bash
python main.py
```

O programa utiliza o arquivo `data/base_conhecimento.json`. Durante a execução, cria ou atualiza os arquivos de histórico, avaliações e CSV na pasta `data/`.

## Estrutura atual
```
gs_lerner/
├── README.md
├── main.py
├── orientacao.py
├── base_conhecimento.py
├── assistente.py
├── data/
│   ├── base_conhecimento.json
│   ├── historico.json
│   ├── avaliacoes.json
│   └── atendimentos.csv
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

A composição segue esta estrutura: `Assistente` possui uma `BaseConhecimento`, que possui uma lista de objetos `Orientacao`.

## Indicadores
O programa calcula o percentual de perguntas com orientação encontrada, o percentual de atendimentos em que a orientação ajudou, o tempo médio, a média de tentativas, a média das avaliações de facilidade e as dúvidas sem solução.

## Fontes
As orientações da base foram organizadas a partir de páginas de serviços públicos. Como regras, horários e canais podem mudar, o usuário deve consultar a fonte antes de tomar decisões. A data registrada no JSON precisa ser confirmada pela equipe sempre que o conteúdo for revisado.

## Sustentabilidade — etapa em desenvolvimento
A base atual contém orientações sobre descarte correto, coleta seletiva, Ecopontos e compostagem. Para concluir a integração com a disciplina de Sustentabilidade, ainda precisamos acrescentar a análise energética exigida no enunciado, com dados e premissas identificados, comparação de alternativas e recomendações integradas ao assistente. Essa etapa ainda não está concluída.

## Testes com usuários — pendente
A validação precisa ser realizada com pelo menos 3 pessoas de fora da equipe e 10 atendimentos no total, conforme o enunciado. Não foram inseridos resultados fictícios neste repositório.

Depois dos testes, registrar os resultados reais: participantes, atendimentos, percentual de respostas encontradas, percentual de respostas úteis, tempo médio, tentativas, avaliação de facilidade e melhorias realizadas. Não registrar nomes ou dados pessoais dos participantes.

## Limitações atuais
- A busca utiliza regras e palavras-chave; não é inteligência artificial generativa.
- O programa responde apenas ao conteúdo cadastrado no JSON.
- Não consulta serviços em tempo real nem abre solicitações em nome do cidadão.
- A verificação de dados pessoais é básica e pode não reconhecer todos os casos.
- A base inicial não cobre todos os bairros, serviços ou situações da cidade.
- A análise energética da disciplina de Sustentabilidade ainda precisa ser desenvolvida e integrada.

## Testes locais
```bash
python -m unittest discover -s tests
```
