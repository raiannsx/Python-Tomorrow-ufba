import random

# Lista de palavras para o jogo
palavras = ["python", "java", "javascript", "typescript", "html", "css", "flutter", "django", "react"]

# Função para escolher uma palavra aleatória
def escolher_palavra():
    return random.choice(palavras)

# Função para mostrar a palavra com as letras adivinhadas
def mostrar_palavra(palavra, letras_adivinhadas):
    return "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])

# Função principal do jogo
def jogar_forca():
    print("Bem-vindo ao Jogo da Forca!")
    
    palavra = escolher_palavra()  # Escolhe uma palavra aleatória
    letras_adivinhadas = []  # Lista de letras que o jogador adivinhou
    tentativas = 6  # Número máximo de tentativas

    while tentativas > 0:
        # Exibe a palavra com as letras adivinhadas
        print(f"\nPalavra: {mostrar_palavra(palavra, letras_adivinhadas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras já adivinhadas: {', '.join(letras_adivinhadas)}")

        # Solicita ao jogador uma letra
        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra!")
            continue

        if letra not in palavra:
            tentativas -= 1
            print(f"A letra '{letra}' não está na palavra.")
        else:
            letras_adivinhadas.append(letra)
            print(f"A letra '{letra}' está na palavra!")

        # Verifica se o jogador adivinhou todas as letras
        if all(letra in letras_adivinhadas for letra in palavra):
            print(f"\nParabéns, você venceu! A palavra era '{palavra}'.")
            break

    else:
        print(f"\nVocê perdeu! A palavra era '{palavra}'.")

# Função para reiniciar o jogo
def reiniciar_jogo():
    while True:
        jogar_forca()
        resposta = input("\nVocê quer jogar novamente? (s/n): ").lower()
        if resposta == 'n':
            print("Obrigado por jogar!")
            break
        elif resposta != 's':
            print("Resposta inválida. Por favor, responda com 's' para sim ou 'n' para não.")

# Inicia o jogo
reiniciar_jogo()
