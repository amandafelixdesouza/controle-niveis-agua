from colorama import init, Fore, Style


init(autoreset=True)


niveis_reservatorio = [
    {"nivel": "Nível 1", "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": "Nível 2", "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": "Nível 3", "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": "Nível 4", "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": "Nível 5", "situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
]


def verificar_reservatorio(dados):
    print("\n--- MONITORAÇÃO DO RESERVATÓRIO DE ÁGUA ---")
    for item in dados:
        # Exibe no terminal a situação atual com a cor correspondente
        print(item["cor"] + f"{item['nivel']} - Situação: {item['situacao']}")


if __name__ == "__main__":
    verificar_reservatorio(niveis_reservatorio)
