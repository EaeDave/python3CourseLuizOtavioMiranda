# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

try:
    import sys
    sys.path.append(r"C:\Users\David\Documents\Python")  # Adicionando um novo
    import modulo_python
    print("Deu certo!")
except ModuleNotFoundError:
    ...

import aula097_m
from aula097_m import variavel_modulo

# print("Este módulo se chama", __name__)
print(aula097_m.variavel_modulo)
print(variavel_modulo)

# Mostra todos os caminhos dos módulos carregados pelo python
print(*sys.path, sep='\n')
