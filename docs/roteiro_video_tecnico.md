# Roteiro do vídeo técnico — PCP

**Duração-alvo:** 6min30s. O limite do enunciado é de 5 a 8 minutos.

**Atenção:** este vídeo é uma demonstração técnica do código, não é o pitch. A gravação deve mostrar a tela com o código legível e o programa rodando. Todos os integrantes precisam falar. A narração deve ser feita pela equipe, sem voz sintética.

## Antes de gravar
- Abra o projeto no editor de código.
- Deixe o terminal visível.
- Execute `python main.py` e confira se a base carrega.
- Deixe o arquivo `data/base_conhecimento.json` aberto para a alteração ao vivo.
- Não mostre dados pessoais de usuários reais.
- Faça o teste obrigatório com pelo menos 3 pessoas de fora da equipe e 10 atendimentos no total antes de apresentar resultados. Não invente indicadores.

## 0:00–0:30 — Equipe, público e problema
**Júlia:** "Somos a equipe do LERNER. Nosso público são moradores e pessoas que circulam por São Paulo. Escolhemos o problema do acesso à informação: orientações de mobilidade, serviços urbanos e sustentabilidade estão distribuídas em diferentes páginas oficiais. Nosso assistente organiza essas informações e mostra a fonte de cada orientação."

## 0:30–1:15 — JSON, dicionários e tuplas
**Erick:** "A base fica em data/base_conhecimento.json. Cada orientação é um dicionário com id, categoria, título, palavras-chave, resposta, documentos, onde, fonte e data de verificação. Quando o programa carrega o arquivo, cada dicionário vira um objeto Orientacao. A busca retorna uma lista de tuplas com a pontuação e o objeto correspondente."

**Mostrar:** um registro completo do JSON e depois o trecho de `carregar()` em `base_conhecimento.py`.

## 1:15–2:05 — Classes, atributos, métodos, self e composição
**Júlia:** "O projeto tem três classes principais. Orientacao guarda os dados de uma orientação e tem o método exibir. BaseConhecimento carrega o JSON, lista categorias e faz a busca. Assistente controla a conversa, registra o histórico, calcula indicadores e exporta o CSV."

**Erick:** "A composição acontece porque o Assistente recebe um objeto BaseConhecimento. A BaseConhecimento guarda uma lista de objetos Orientacao. O parâmetro self permite que os métodos acessem os atributos do próprio objeto."

**Mostrar:** `orientacao.py`, `base_conhecimento.py` e o construtor de `Assistente`.

## 2:05–3:10 — Normalização, pontuação e exemplo real
**Júlia:** "Antes de comparar os textos, a função normalizar deixa tudo em minúsculas, remove acentos e troca pontuação por espaços. Assim, 'Ecoponto' e 'ecoponto' são comparados da mesma forma."

**Erick:** "A regra dá 3 pontos para cada palavra-chave encontrada e mais 1 ponto para cada palavra da pergunta com pelo menos quatro letras que apareça no título. Com 6 pontos ou mais, a confiança é alta; de 3 a 5, é média. Abaixo de 3, o sistema não apresenta uma orientação como resposta."

**Mostrar no terminal:** digitar `Como descartar entulho em um ecoponto?` e apontar os pontos retornados. Explicar a pontuação que realmente aparecer no terminal.

## 3:10–4:20 — Demonstração dos fluxos
**Júlia:** executar e mostrar:
1. Uma pergunta encontrada.
2. Uma pergunta que não está na base, como "onde encontro aula de música gratuita?", e a sugestão de tentar novamente ou navegar por categoria.
3. Uma entrada vazia ou uma opção inválida no menu.
4. Uma entrada fictícia com muitos dígitos, por exemplo `meu telefone é 11111111111`, mostrando o bloqueio. Não use dados reais.
5. Navegação por categoria, entrando em Sustentabilidade e abrindo uma orientação.

**Fala:** "O programa não registra a pergunta quando detecta uma possível informação pessoal. O usuário também pode voltar usando 0 nas telas de navegação."

## 4:20–5:00 — Alteração ao vivo no JSON
**Erick:** "A base pode ser ampliada sem alterar as classes. Vamos adicionar uma palavra-chave a uma orientação e testar uma pergunta que antes não tinha correspondência."

**Demonstração sugerida:**
1. Antes da alteração, pergunte: `onde levo resto de obra pequena?`
2. Abra o registro de Ecopontos no JSON e acrescente `resto de obra pequena` à lista de palavras-chave.
3. Salve o arquivo. Se o programa estiver aberto, encerre e execute novamente para recarregar o JSON.
4. Repita a pergunta e mostre a nova pontuação.

Não apague nem substitua as palavras-chave que já existem.

## 5:00–5:50 — Histórico, CSV e indicadores
**Júlia:** "Cada atendimento válido é salvo em data/historico.json com data, origem, pergunta, id da orientação, resultado, se ajudou, número de tentativas e tempo. As perguntas bloqueadas por possível dado pessoal não entram no histórico."

**Erick:** "Ao sair, o programa pede uma nota de facilidade de 1 a 5 e exporta os atendimentos para data/atendimentos.csv usando csv.DictWriter. Os indicadores mostram taxa de respostas encontradas, taxa em que ajudou, tempo médio, tentativas e dúvidas sem solução."

**Mostrar:** `data/historico.json`, `data/atendimentos.csv` e a opção de indicadores. Para o vídeo final, use os resultados reais do teste com usuários.

## 5:50–6:30 — Decisão técnica, limitação e encerramento
**Júlia:** "Uma decisão técnica foi manter a busca por pontuação e a base em JSON. Assim, conseguimos atualizar as orientações sem reescrever o programa e explicar de onde cada informação veio."

**Erick:** "A principal limitação é que a busca depende das palavras-chave cadastradas e não consulta os serviços em tempo real. Por isso, mostramos a fonte oficial e a data de verificação. O próximo passo é ampliar a base e melhorar as orientações a partir dos testes com usuários."

## Checklist final
- [ ] Vídeo entre 5 e 8 minutos.
- [ ] Os dois integrantes falaram.
- [ ] Código legível e programa em execução.
- [ ] JSON, dicionários e tuplas explicados.
- [ ] Três classes, atributos, métodos, self e composição explicados.
- [ ] Normalização e pontuação demonstradas com uma pergunta real.
- [ ] Pergunta encontrada e não encontrada demonstradas.
- [ ] Entrada inválida e bloqueio de dado pessoal demonstrados.
- [ ] Navegação por categoria demonstrada.
- [ ] Palavra-chave adicionada ao JSON ao vivo e testada.
- [ ] Histórico, CSV e indicadores mostrados.
- [ ] Uma decisão técnica e uma limitação explicadas.
- [ ] Link do vídeo não listado inserido no README.
