# Quando o módulo solicitante importar tudo utilizando *
# Só será importado o que foi explicitamente declarado
# Por exemplo:
# from aula099_package import modulo *

__all__ = [
    "variavel",
]

variavel = "David"


def soma_do_modulo(x, y):  # Essa função não será importada ao usar o *
    return x + y
