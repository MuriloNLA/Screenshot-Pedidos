# Screenshot Automatico por Numero de Pedido

Script Python que aguarda um atalho de teclado, solicita o numero do pedido e tira um print da tela, salvando o arquivo automaticamente na pasta correta com o nome padronizado — sem precisar usar "Salvar como" ou organizar manualmente.

---

## Problema Resolvido

O processo de registrar prints de pedidos exigia tirar o screenshot, abrir o Explorer, navegar ate a pasta certa e salvar o arquivo com o nome correto. Com o script rodando em segundo plano, basta pressionar o atalho, digitar o numero do pedido e o arquivo ja fica salvo e organizado.

---

## Funcionalidades

- Fica rodando em segundo plano aguardando o atalho configurado (padrao: F8)
- Solicita o numero do pedido via terminal
- Cria automaticamente a pasta do pedido se nao existir
- Salva o print com nome padronizado: `Simulador_NumeroPedido.png`
- Detecta se ja existe um print para o pedido e pergunta se deve sobrescrever
- Contagem regressiva para dar tempo de colocar a janela desejada em foco
- Oferece atalho para abrir a pasta no Explorer apos salvar
- Instala as dependencias automaticamente se nao estiverem presentes

---

## Tecnologias

| Biblioteca | Uso |
|---|---|
| `pyautogui` | Captura de tela |
| `keyboard` | Registro do atalho de teclado global |
| `Pillow` | Salvamento da imagem |

---

## Instalacao

As dependencias sao instaladas automaticamente na primeira execucao. Para instalar manualmente:

```bash
pip install pyautogui Pillow keyboard
```

---

## Configuracao

No inicio do arquivo, ajuste as variaveis conforme necessario:

```python
PASTA_RAIZ        = r"C:\Users\usuario\Downloads\Pedidos\Fotos Pedidos"
AGUARDAR_SEGUNDOS = 3
ATALHO            = "f8"
```

---

## Uso

```bash
python print_simulador.py
```

O script fica rodando em segundo plano. Ao pressionar o atalho:

1. O terminal abre solicitando o numero do pedido
2. Uma contagem regressiva da tempo para colocar a janela em foco
3. O print e tirado e salvo automaticamente em `PASTA_RAIZ\NumeroPedido\Simulador_NumeroPedido.png`

---

## Estrutura de pastas gerada

```
Fotos Pedidos/
    69897/
        Simulador_69897.png
    69821/
        Simulador_69821.png
```

---

## O que eu melhoraria

- Interface grafica (GUI) para substituir o terminal
- Suporte a captura de janela especifica ao inves da tela inteira
- Historico dos prints tirados na sessao
- Configuracao via arquivo `.ini` sem precisar editar o codigo
