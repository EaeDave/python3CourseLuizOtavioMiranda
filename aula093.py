# Try, except, else e finally
string = 'David'  # str
print(isinstance(string, str))
try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print('Dividiu por zero.')
    print(e)
    print(e.__class__.__name__)
except NameError:
    print('Uma variável não está definida.')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')


print('CONTINUAR')
