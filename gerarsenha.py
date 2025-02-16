"""Gerador de senhas: apos gerar, salve-a em uma nuvem"""

import random
import string

def gerar_senha(tamanho=8):
    # Definir os caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gerar a senha aleatória
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha

# Gerar uma senha segura de 8 caracteres ou (pode mudar o valor de tamanho se preferir, apenas mude o número)
senha_gerada = gerar_senha(8)
print("Apos gerar, salve-a em uma nuvem")
print("Senha gerada:", senha_gerada)
