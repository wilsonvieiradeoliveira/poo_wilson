# Semana 05 — Mini-projeto 1: Arena de Personagens

Semana de laboratório: nenhum conteúdo novo, só montar as peças das semanas 1 a 4 num
projeto completo, versionado em commits ao longo dos dias.

## Mini-projeto 1: Arena de Personagens

`arena.py` traz um menu em loop para criar personagens, listá-los e colocá-los para
batalhar. A classe `Personagem` guarda nome (parâmetro), vida fixa em 100 e ataque com
valor padrão (15); a batalha escolhe dois lutadores pelo número da listagem e alterna
os ataques até um dos dois cair, anunciando o vencedor.

| Aula | Meta | Commit |
|---|---|---|
| 1 — Fundação | Classe `Personagem` completa + menu com Criar e Sair | `Projeto: classe e opção criar` |
| 2 — Listar e proteger | Listagem numerada (1, 2, 3...) + validações (lista vazia, opção inválida) | `Projeto: listagem e validações` |
| 3 — A batalha | Escolha dos lutadores (com o `-1` do índice) + loop de combate + vencedor | `Projeto: batalha funcionando` |
| 4 — Caça-bugs e extras | Placar visual da vida + roteiro de 5 testes rodado | `Projeto: extra do placar visual + roteiro de testes validado` |
| 5 — Entrega | Este README | — |

## Roteiro de testes (rodado antes da entrega)

- [x] Teste 1 — Listar com a arena vazia → mensagem amigável, sem erro.
- [x] Teste 2 — Criar 3 personagens e listar → numeração 1, 2, 3 com nome e vida.
- [x] Teste 3 — Opção 9 no menu → avisa e volta ao menu, sem travar.
- [x] Teste 4 — Batalha entre 2 escolhidos → vida caindo por rodada e vencedor anunciado.
- [x] Teste 5 — Batalha invertendo os ataques → o outro lutador vence.

Validações extras cobertas na batalha: escolher o mesmo personagem duas vezes e
digitar um número fora da lista, além do aviso ao tentar batalhar com menos de 2
personagens criados.

## Extra escolhido

Placar visual da vida a cada rodada, com barras `#`/`-` (`barra_vida()`), em vez do
dano aleatório sugerido na apostila: manter o dano ligado a `self.ataque` (determinístico)
era necessário para o Teste 5 — invertendo quem tem o maior ataque, o resultado
precisa mudar de forma previsível, o que um dano aleatório puro comprometeria.

## Decisões de projeto

- A vida de um personagem não é restaurada automaticamente entre batalhas — a
  listagem mostra a vida *atual*, então quem perde uma luta continua com a vida
  reduzida até ser criado outro personagem ou reiniciar o programa.
- `max(0, vida)` é usado em toda exibição (listagem, status e placar) para nunca
  mostrar vida negativa, mesmo que o atributo interno passe de 0 no último golpe.
