# Jogo da Forca

Jogo da forca com interface gráfica em Tkinter, textos grandes e regras organizadas
com programação orientada a objetos. Não é necessário instalar bibliotecas externas.

## Como executar

É necessário ter Python 3.10 ou superior instalado. No terminal, entre nesta pasta,
ative o ambiente virtual e execute:

```powershell
.\.venv\Scripts\Activate.ps1
python .\main.py
```

Escolha uma letra clicando no teclado da tela ou pressionando uma letra no teclado
físico. Você pode errar até seis vezes. O botão **Nova partida** sorteia outra palavra.

## Organização das classes

- `BancoDePalavras`, em `palavras.py`: guarda e sorteia palavras com categorias.
- `JogoDaForca`, em `jogo.py`: controla regras e estado da rodada.
- `InterfaceJogo`, em `interface.py`: monta a janela e traduz ações do usuário em
  jogadas.

## Como executar os testes

Na pasta `jogo_da_forca`, com o ambiente virtual ativado, execute:

```powershell
python -m unittest discover -s tests -v
```

As regras são testadas sem abrir a interface gráfica.
