# Mini-projeto 1 — Arena de Personagens (10 pontos)

Lançado na Semana 4 (Aula 4), a entregar ao fim da Semana 5.

## Especificação

- Menu em loop: `1` Criar personagem (nome e ataque), `2` Listar personagens (com status), `3` Batalha, `4` Sair.
- Classe `Personagem` com `__init__` (vida fixa 100, ataque com valor padrão).
- Batalha: escolher dois personagens da lista e simular a luta em loop até ter um vencedor.

## Distribuição dos pontos

- 3 pts — Classe `Personagem` correta (construtor, vida fixa, métodos funcionando).
- 3 pts — Menu completo funcionando sem travar (inclusive com lista vazia).
- 2 pts — Batalha entre os escolhidos com vencedor anunciado.
- 2 pts — Git + GitHub: mínimo 4 commits com mensagens claras + push.

## Estado atual

`arena.py` é o esqueleto criado na Semana 4: classe `Personagem` com `__init__` e o menu completo (criar, listar, batalhar, sair) já rodando. `FICHA_MODELAGEM.md` traz a modelagem feita na oficina da Aula 5, pendente apenas da validação presencial em dupla.

Extras (dano aleatório, cura, vida máxima) ficam para depois de fechar os itens básicos.
