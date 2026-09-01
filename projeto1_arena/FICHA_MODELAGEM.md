# Ficha de modelagem — Personagem (Mini-projeto 1: Arena de Personagens)

## Atributos (atributo → origem)

| Atributo | Origem | Observação |
|---|---|---|
| `nome` | parâmetro (obrigatório) | cada personagem nasce com o seu nome, quem cria decide |
| `vida` | fixo (100) | regra do jogo: todo personagem nasce com 100, não é escolha de quem cria |
| `ataque` | parâmetro com padrão (15) | tem um valor comum, mas quem cria pode informar outro |

Não há atributo de classe na versão atual do `Personagem` — todo dado varia de objeto para objeto.

## Métodos (nome → o que recebe → o que devolve/faz)

| Método | Recebe | Devolve / faz |
|---|---|---|
| `atacar(alvo)` | outro `Personagem` | não devolve nada; subtrai `self.ataque` de `alvo.vida` |
| `esta_vivo()` | nada | devolve `True`/`False` conforme `self.vida > 0` |
| `status()` | nada | não devolve nada; imprime nome, vida, ataque e se está vivo |

## Fluxo do menu

```
1 Criar personagem
  -> pede nome e ataque (Enter = padrão 15)
  -> cria um Personagem e guarda na lista

2 Listar personagens
  -> lista vazia? avisa e volta ao menu
  -> senão, mostra o status (via status()) de cada um, numerado

3 Batalha
  -> menos de 2 personagens? avisa e volta ao menu
  -> escolhe o 1º e o 2º personagem pelo índice da listagem
  -> restaura a vida dos dois para 100 (a arena "cura" antes da luta)
  -> loop: os dois se atacam alternadamente até um deles não estar mais vivo
  -> anuncia o vencedor

4 Sair
  -> encerra o loop do menu
```

## Validação em dupla

Colega que validou: **______________________ (preencher e assinar em aula)**

> Espaço reservado para a validação presencial pedida na Aula 5: troque esta ficha com
> um colega e confirme se ele conseguiria programar a classe e o menu só lendo o que
> está escrito acima.
