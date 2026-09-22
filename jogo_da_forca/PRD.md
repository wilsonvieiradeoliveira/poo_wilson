# PRD — Jogo da Forca em Python com POO

## 1. Visão do produto

Criar um jogo da forca para computador, em português, com interface gráfica simples,
legível e acessível. O projeto deve demonstrar programação orientada a objetos de
forma didática, separando as regras do jogo da interface visual.

## 2. Objetivo

Entregar um jogo que permita iniciar e reiniciar partidas, escolher letras por meio
de botões ou teclado, acompanhar visualmente os erros e receber uma mensagem clara
de vitória ou derrota. Os textos principais devem usar fonte grande.

## 3. Público-alvo

- Estudantes iniciantes de Python e programação orientada a objetos.
- Pessoas que desejam jogar uma partida rápida sem instalar bibliotecas externas.

## 4. Escopo da versão 1

### Funcionalidades obrigatórias

- Sortear uma palavra e mostrar uma dica ou categoria.
- Ocultar a palavra com traços e revelar os acertos.
- Aceitar apenas uma tentativa por letra.
- Considerar letras acentuadas equivalentes à letra sem acento para a jogada.
- Exibir letras já utilizadas.
- Exibir o desenho da forca em estágios conforme os erros.
- Encerrar a rodada com vitória ou derrota.
- Revelar a palavra ao perder.
- Permitir iniciar uma nova rodada sem fechar o programa.
- Usar fontes grandes nos elementos principais.
- Permitir jogar usando mouse e teclado físico.

### Fora do escopo inicial

- Jogo on-line ou multijogador em rede.
- Banco de dados, cadastro de usuário ou login.
- Ranking persistente na internet.
- Efeitos sonoros e animações complexas.
- Empacotamento como instalador ou arquivo executável.

## 5. Experiência e interface

A janela será organizada em quatro áreas:

1. Cabeçalho com título, categoria e contador de erros.
2. Área central com o desenho da forca.
3. Palavra escondida em fonte grande e letras já tentadas.
4. Teclado de A a Z e botão `Nova partida`.

Diretrizes visuais:

- Palavra: aproximadamente 32–40 px.
- Botões das letras: aproximadamente 16–20 px, com área confortável para clique.
- Alto contraste, mensagens curtas e janela redimensionável.
- Estados diferentes para letra disponível, correta e incorreta.
- O jogo deve continuar compreensível sem depender apenas de cores.

## 6. Regras propostas

- Cada rodada começa com uma palavra sorteada.
- O jogador pode cometer até 6 erros.
- Uma tentativa correta revela todas as ocorrências da letra.
- Uma tentativa repetida não desconta nova chance.
- A partida termina quando todas as letras forem reveladas ou o limite de erros for
  alcançado.
- Espaços e hífens aparecem desde o início e não precisam ser adivinhados.

## 7. Modelagem orientada a objetos

### `BancoDePalavras`

Responsável por armazenar/carregar palavras e sortear uma entrada com sua categoria.

### `JogoDaForca`

Responsável pelo estado e pelas regras: palavra atual, letras tentadas, erros, acertos,
fim da partida e reinício. Não conhecerá detalhes da interface gráfica.

### `InterfaceJogo`

Responsável pela janela, botões, atalhos de teclado, desenho da forca e atualização
dos textos. Consulta o estado de `JogoDaForca` e envia a ele as jogadas.

Essa divisão permitirá testar as regras sem abrir uma janela.

## 8. Estrutura de arquivos proposta

```text
jogo_da_forca/
├── PRD.md
├── README.md
├── main.py
├── jogo.py
├── interface.py
├── palavras.py
└── tests/
    └── test_jogo.py
```

## 9. Requisitos técnicos

- Python 3.10 ou superior.
- Código e nomes em português, adequado ao contexto didático do repositório.
- Sem acesso à internet durante o jogo.
- Sem dependências externas na opção recomendada com Tkinter.
- Ponto de entrada: `python main.py`.

## 10. Critérios de aceitação

- A janela abre sem erro e os textos principais são facilmente legíveis.
- Cada letra pode ser usada no máximo uma vez por rodada.
- Letras acentuadas são reveladas ao escolher sua versão sem acento.
- Acertos não aumentam o contador de erros.
- Erros avançam exatamente um estágio do desenho.
- Vitória e derrota bloqueiam novas tentativas até uma nova rodada.
- `Nova partida` limpa o estado anterior e sorteia uma palavra.
- As regras centrais possuem testes automatizados.
- O README explica como executar e identifica as classes do projeto.

## 11. Plano de implementação

1. Confirmar as decisões de produto pendentes.
2. Implementar o banco de palavras e a classe de regras.
3. Criar testes automatizados para vitória, derrota, repetição e acentos.
4. Construir a interface visual e os controles de mouse/teclado.
5. Fazer testes de integração e uma revisão visual.
6. Escrever o README com instruções de execução.

## 12. Decisões aprovadas

- **Interface:** Tkinter nativo, sem dependências externas.
- **Palavras:** lista interna de palavras acompanhadas por categorias.
- **Escopo:** versão essencial; dificuldade, placar e sequência de vitórias ficam
  reservados para uma evolução futura.

## 13. Definição de pronto

O projeto estará pronto quando todos os critérios de aceitação forem atendidos, os
testes passarem e uma partida completa puder ser jogada somente com mouse ou somente
com teclado.
