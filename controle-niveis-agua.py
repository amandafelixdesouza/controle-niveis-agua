from colorama import init, Fore, Style

# Inicializa o colorama para funcionar corretamente no terminal
init(autoreset=True)

# 1. Lista que armazena os níveis e as mensagens de alerta do reservatório
niveis_reservatorio = [
    {"nivel": "Nível 1", "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": "Nível 2", "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": "Nível 3", "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": "Nível 4", "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": "Nível 5", "situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
]

# 2. Função responsável por definir e exibir a cor da mensagem conforme o nível
def verificar_reservatorio(dados):
    print("\n--- MONITORAÇÃO DO RESERVATÓRIO DE ÁGUA ---")
    for item in dados:
        # Exibe no terminal a situação atual com a cor correspondente
        print(item["cor"] + f"{item['nivel']} - Situação: {item['situacao']}")

# 3. Execução da função principal
if __name__ == "__main__":
    verificar_reservatorio(niveis_reservatorio)