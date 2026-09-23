# Semana 07 — Trabalho prático: Lojinha com classe Produto (10 pts)

Segunda semana de produção do bimestre: a classe `Produto` construída aqui parte do
`06_loja.py` da semana 6 (que já tinha `__preco` como property) e vai direto para o
Projeto Integrador em Flask.

## Trabalho: Lojinha com classe Produto

`loja.py` traz um menu em loop para cadastrar produtos, listar o catálogo, vender,
repor estoque e sair. A classe `Produto` guarda nome (parâmetro) e `__preco`/`__estoque`
protegidos por `@property`, ambos recusando valores negativos; `vender(qtd)` valida
quantidade e estoque suficiente devolvendo `True`/`False`, e `repor(qtd)` valida apenas
a quantidade — cada recusa imprime uma mensagem própria explicando o motivo.

| Aula | Meta | Commit |
|---|---|---|
| 1 — Fundação | Classe `Produto` com `__preco`/`__estoque` protegidos + `exibir()` formatado | `Trabalho: classe Produto com properties` |
| 2 — vender() e repor() | Os dois métodos completos, com mensagens distintas para cada recusa | `Trabalho: vender e repor com validações` |
| 3 — O menu da lojinha | Cadastrar, listar, vender, repor e sair integrados, na arquitetura da Arena | `Trabalho: menu da lojinha completo` |
| 4 — Caça-bugs e extras | Roteiro de 5 testes rodado + `valor_total_do_estoque()` | `Trabalho: extra valor_total_do_estoque + roteiro de testes validado` |
| 5 — Entrega | Este README | `Trabalho: README da semana 7 com o diário do trabalho` |

## Roteiro de testes (rodado antes da entrega)

- [x] Teste 1 — Listar com o catálogo vazio → mensagem amigável, sem erro.
- [x] Teste 2 — Cadastrar 3 produtos e listar → numeração com nome, preço (`R$ x.xx`) e estoque.
- [x] Teste 3 — Cadastrar com preço negativo → bloqueado pela property, com aviso (produto entra com preço 0).
- [x] Teste 4 — Vender mais do que o estoque → recusado com a mensagem do motivo.
- [x] Teste 5 — Repor e vender em sequência → estoque atualizando certo nas duas operações.

Validações extras cobertas: vender/repor com o catálogo vazio, opção inválida no menu
e número de produto fora da lista — nenhuma delas trava o programa.

## Extra escolhido

`valor_total_do_estoque()`: soma preço × estoque de todos os produtos do catálogo. Foi
o extra indicado na apostila como "o mais útil para o Integrador" — o sistema em Flask
vai precisar exatamente dessa conta para exibir o valor do estoque, então adiantar essa
função aqui evita reescrevê-la do zero mais tarde.

## Decisões de projeto

- Assim como os setters de `vida`/`ataque` da Arena (semana 6), os setters de `preco` e
  `estoque` **ignoram silenciosamente** valores negativos (só avisam e mantêm o valor
  anterior) — mesmo padrão pedido na apostila, sem lançar exceção.
- Em `vender(qtd)`, o teste `qtd > self.__estoque` acontece **antes** de qualquer
  alteração no estoque, então uma venda recusada nunca deixa o estoque negativo.
- `repor(qtd)` não devolve `True`/`False` como `vender(qtd)` — a apostila só exige o
  retorno para a venda, porque é o caso em que quem chamou (o menu) precisa distinguir
  "aconteceu" de "recusado"; repor só tem um motivo de recusa (quantidade inválida), já
  avisado na própria mensagem.
- `escolher_produto()` reaproveita `listar_catalogo()` antes de pedir o número — mesma
  arquitetura de `escolher_lutadores()` da Arena, incluindo o `-1` na hora de indexar
  `catalogo`.

## Pergunta de ouro (para a conferência)

**Por que `self.preco = preco` no `__init__`, sem os dois underscores?** Porque atribuir
por `self.preco` (sem `__`) passa pelo **setter** da property, que valida o valor antes
de gravar em `self.__preco`. Se o `__init__` escrevesse direto em `self.__preco`, o
preço inicial escaparia da validação e um `Produto("X", -10)` seria criado com preço
negativo — a mesma regra vale para `self.estoque = estoque`.

## Autoavaliação da semana

Pela rubrica desta apostila, os critérios pontuados foram: classe `Produto` protegida
(3 pts), `vender()`/`repor()` corretos (3 pts), menu completo sem travar (2 pts) e
Git + GitHub com o mínimo de 4 commits distribuídos (2 pts) — todos cobertos pelo
`loja.py` e pelo histórico de commits desta pasta.
