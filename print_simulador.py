# print_simulador.py
# Aguarda um atalho de teclado e tira um print da tela,
# salvando na pasta correta com o nome do pedido informado.
#
# Dependencias (instaladas automaticamente):
#     pyautogui, Pillow, keyboard
#
# Uso:
#     python print_simulador.py

import subprocess
import sys
import os
import time


def instalar(pacote):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pacote],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

for pacote in ["pyautogui", "Pillow", "keyboard"]:
    try:
        __import__(pacote if pacote != "Pillow" else "PIL")
    except ImportError:
        print(f"Instalando {pacote}...")
        instalar(pacote)

import pyautogui
import keyboard


# ---------------------------------------------------------------------------
# CONFIGURACAO
# ---------------------------------------------------------------------------

PASTA_RAIZ       = r"C:\Users\usuario\Downloads\Pedidos\Fotos Pedidos"
AGUARDAR_SEGUNDOS = 3
ATALHO           = "f8"

# ---------------------------------------------------------------------------


def tirar_print():
    os.system("cls")
    print("=" * 45)
    print("   Print Automatico de Pedidos")
    print("=" * 45)

    numero_pedido = input("\nDigite o numero do pedido: ").strip()

    if not numero_pedido:
        print("Numero do pedido nao pode ser vazio.")
        return

    for c in r'\/:*?"<>|':
        numero_pedido = numero_pedido.replace(c, "_")

    pasta_pedido = os.path.join(PASTA_RAIZ, numero_pedido)
    if not os.path.exists(pasta_pedido):
        os.makedirs(pasta_pedido)
        print(f"Pasta criada: {pasta_pedido}")

    nome_arquivo     = f"Simulador_{numero_pedido}.png"
    caminho_completo = os.path.join(pasta_pedido, nome_arquivo)

    if os.path.exists(caminho_completo):
        sobrescrever = input(f"\nJa existe um print para o pedido '{numero_pedido}'. Sobrescrever? (s/n): ").strip().lower()
        if sobrescrever != "s":
            print("Operacao cancelada.")
            input("\nPressione Enter para fechar...")
            return

    print(f"\nVoce tem {AGUARDAR_SEGUNDOS} segundos para colocar a janela desejada em foco...")
    for i in range(AGUARDAR_SEGUNDOS, 0, -1):
        print(f"  {i}...")
        time.sleep(1)

    print("Tirando print...")
    screenshot = pyautogui.screenshot()
    screenshot.save(caminho_completo)

    print(f"\nPrint salvo com sucesso!")
    print(f"   Arquivo: {nome_arquivo}")
    print(f"   Pasta:   {pasta_pedido}")

    abrir = input("\nAbrir a pasta para conferir? (s/n): ").strip().lower()
    if abrir == "s":
        subprocess.Popen(f'explorer "{pasta_pedido}"')

    input("\nPressione Enter para fechar...")


def main():
    print("=" * 45)
    print("   Print Automatico de Pedidos")
    print(f"   Atalho: {ATALHO.upper()}")
    print("=" * 45)
    print(f"\nAguardando o atalho [{ATALHO.upper()}] para tirar o print...")
    print("Feche esta janela para encerrar.\n")

    keyboard.add_hotkey(ATALHO, tirar_print)
    keyboard.wait()


if __name__ == "__main__":
    main()
