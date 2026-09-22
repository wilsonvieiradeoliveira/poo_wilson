# Semana 06 — Encapsulamento

Esconder os dados do objeto atrás de `__atributo` e controlar o acesso por
`@property`, para as regras do jogo (vida, ataque, saldo, preço...) morarem
num lugar só — a classe — em vez de espalhadas pelo código que usa o objeto.

| Arquivo | Aula | Conteúdo |
|---|---|---|
| [`01_s6_ex1.py`](01_s6_ex1.py) | 1 | Exercício 1 — as 3 trapaças no `Personagem` sem cadeado (`heroi.vida = 999999`, `vilao.ataque = 0`, `heroi.vida = -50`) |
| [`02_arena_v2.py`](02_arena_v2.py) | 1 a 4 | Exercícios 2, 3, 4 e 5 + Missão 1: `arena_v2.py` evoluindo até a Arena blindada (`__vida`/`__ataque` como `@property`, `atacar()` com `max(0, ...)`, teste de trapaça automático) |
| [`03_s6_mini_aula2_aluno.py`](03_s6_mini_aula2_aluno.py) | 2 | Mini-desafio — `Aluno` com `@property` de `nota` validando 0 a 100 |
| [`04_s6_ex6_perfil.py`](04_s6_ex6_perfil.py) | 3 | Exercício 6 — `Perfil` com `__seguidores` como `@property`, recusando negativos |
| [`05_s6_ex7_contabancaria.py`](05_s6_ex7_contabancaria.py) | 4 | Exercício 7 + Missão 2 — `ContaBancaria` com saldo somente-leitura, `depositar`/`sacar` e menu de teste |
| [`06_loja.py`](06_loja.py) | 3 e 5 | Mini-desafio da aula 3 + esqueleto do trabalho da semana 7 — `Produto` com `__preco` protegido |

## Exercício 1 — o que acontece na batalha sem cadeado

Rodando `01_s6_ex1.py` com o `Personagem` igual ao da semana 5 (vida e ataque
públicos):

- As 3 trapaças funcionam sem nenhum aviso ou erro — o Python aceita
  qualquer valor atribuído a `heroi.vida` e `vilao.ataque`.
- `heroi.vida = 999999` deixa o herói praticamente imortal.
- `vilao.ataque = 0` faz `atacar()` descontar zero de dano: o vilão vira
  inofensivo.
- `heroi.vida = -50` deixa a vida negativa, o que não devia nem existir.

## Exercício 2 — o que quebra ao trocar `vida` por `__vida`

Copiando `arena.py` para `arena_v2.py` e trocando `self.vida` por
`self.__vida` (sem mais nada), quebra tudo que acessa `vida` de fora da
classe:

- `listar_personagens()` e `barra_vida()` — usam `p.vida` / `lutador.vida`
  diretamente e passam a estourar `AttributeError`.
- `atacar()` e `esta_vivo()` também quebram, porque estão *dentro* da
  classe mas ainda escritos como `alvo.vida -= self.ataque` e
  `self.vida > 0` — o nome dela mudou, e o Python "esconde" `__vida`
  renomeando por trás dos panos (name mangling), então nem o código interno
  antigo encontra mais o atributo pelo nome de sempre.

## Mini-desafio — Aula 1

**Pergunta:** trancamos a vida com `__`, mas agora nem o placar consegue lê-la. O que precisaríamos para resolver?

**Resposta:** precisamos de um jeito de *ler* o valor escondido sem abrir
mão do cadeado — um método que devolve `self.__vida` para quem pergunta de
fora, mas continua sendo o único caminho de acesso. Isso é exatamente o que
o `@property` faz: por fora parece um atributo comum (`heroi.vida`), por
dentro é um método que pode validar antes de deixar ler ou escrever.

## Mini-desafio — Aula 4 (pergunta de design)

**Pergunta:** por que `saldo` tem *getter* mas não tem *setter*, enquanto a `vida` do personagem tem os dois?

**Resposta:** porque são duas naturezas de dado diferentes. `vida` é um
valor que faz sentido *atribuir diretamente* de vez em quando (ex.: curar o
personagem, resetar para uma nova batalha) — por isso tem setter, só que com
validação (0 a 100). Já `saldo` de uma conta bancária nunca deveria ser
"atribuído" do nada: ele só pode *mudar por uma operação com regra própria*
(depositar exige valor positivo; sacar exige ter saldo suficiente). Dar um
setter livre para `saldo` permitiria pular essas regras (`conta.saldo =
999999`), então a única forma seguro de deixá-lo somente-leitura por fora é
não criar o setter — quem quiser mudar o saldo é obrigado a passar por
`depositar()`/`sacar()`.

## Teste de trapaça documentado (Arena blindada)

As mesmas 3 trapaças do Exercício 1, repetidas em `02_arena_v2.py` depois do
encapsulamento (função `teste_de_trapaca()`, chamada automaticamente ao
rodar o arquivo):

| Trapaça | Antes (semana 5) | Depois (Arena blindada) |
|---|---|---|
| `heroi.vida = 999999` | vida vira 999999, herói imortal | setter de `vida` recusa (`0 <= nova <= 100` é falso) → vida continua 100 |
| `vilao.ataque = 0` | ataque vira 0, vilão inofensivo | setter de `ataque` recusa (`1 <= novo <= 50` é falso) → ataque continua 15 |
| `heroi.vida = -50` | vida vira -50, sem sentido | setter de `vida` recusa (`0 <= nova <= 100` é falso) → vida continua 100 |

Como o `__vida` e o `__ataque` só podem ser alterados através das
`@property`, e as duas properties só aceitam valores dentro da faixa
válida, as 3 trapaças da aula 1 não têm mais efeito nenhum.

## Pergunta de ouro (para a arguição oral)

**O que é encapsulamento?** É esconder os dados internos de um objeto
(`__atributo`) e controlar todo acesso a eles por métodos — para que as
regras de validação fiquem concentradas num lugar só dentro da classe, em
vez de espalhadas (ou esquecidas) em cada trecho de código que usa o
objeto.

**Quando usar `property` sem setter?** Quando o dado só deve mudar através
de uma operação com regra própria, nunca por atribuição direta — como o
`saldo` de uma `ContaBancaria`, que só muda por `depositar()`/`sacar()`, ou
um `total_criados`/ID gerado automaticamente que ninguém de fora deveria
poder reescrever.

## Checklist de autoavaliação da semana

- [x] Sei explicar encapsulamento com a analogia do caixa eletrônico.
- [x] Sei usar `__` para proteger um atributo e sei o que acontece ao
      acessá-lo de fora (`AttributeError`, por causa do name mangling).
- [x] Sei escrever getter e setter com validação — e explicar por que a
      validação importa (é o que impede as trapaças da aula 1).
- [x] Sei converter get/set para `@property` e evitar o `RecursionError` do
      setter (regra de ouro: dentro do setter, sempre mexer em
      `self.__atributo`, nunca em `self.atributo`).
- [x] Sei quando usar `property` sem setter (somente leitura) — caso
      `ContaBancaria`.

## Decisões de projeto

- Os setters de `vida` e `ataque` **ignoram silenciosamente** valores fora
  da faixa (não lançam exceção) — é o comportamento pedido na apostila
  (`if 0 <= nova <= 100: self.__vida = nova`), então uma trapaça bloqueada
  simplesmente mantém o valor anterior, sem quebrar o programa.
- `atacar()` usa `alvo.vida = max(0, alvo.vida - self.__ataque)` — o
  `max(0, ...)` garante que o valor passado para o setter de `vida` nunca
  seja negativo, então o dano sempre "passa" pela validação e a vida nunca
  fica abaixo de 0. Isso tornou desnecessário o `max(0, ...)` que existia
  em `barra_vida()`/`status()` na versão da semana 5.
- `06_loja.py` guarda só o mini-desafio da aula 3 (`Produto` com `__preco`).
  `__estoque`, `vender(qtd)`, `repor(qtd)` e o menu completo da lojinha
  ficam para o trabalho da semana 7, que vale 10 pts e importa este mesmo
  código.

## Próximo passo (semana 7)

Trabalho da lojinha (10 pts): completar `Produto` com `__estoque`
protegido, `vender(qtd)`/`repor(qtd)` validando quantidade e estoque, e um
menu (cadastrar, listar catálogo, vender, repor, sair) — partindo do
`06_loja.py` desta semana.
