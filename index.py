import re

def identificar_bandeira(numero):
    numero = numero.replace(' ', '').replace('-', '')

    if re.match(r'^4\d{12}(\d{3})?$', numero):
        return 'Visa'
    elif re.match(r'^5[1-5]\d{14}$', numero):
        return 'MasterCard'
    elif re.match(r'^3[47]\d{13}$', numero):
        return 'American Express'
    elif re.match(r'^3(?:0[0-5]|[68]\d)\d{11}$', numero):
        return 'Diners Club'
    elif re.match(r'^6(?:011|5\d{2})\d{12}$', numero):
        return 'Discover'
    elif re.match(r'^2(?:014|149)\d{11}$', numero):
        return 'EnRoute'
    elif re.match(r'^(?:2131|1800|35\d{3})\d{11}$', numero):
        return 'JCB'
    elif re.match(r'^8699\d{11}$', numero):
        return 'Voyager'
    elif re.match(r'^(606282|3841)\d{10,12}$', numero):
        return 'HiperCard'
    elif re.match(r'^50\d{14,17}$', numero):
        return 'Aura'
    else:
        return 'Bandeira não identificada'

if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    print("Bandeira:", identificar_bandeira(numero))

"""# Explicação do Código
Este código identifica a bandeira de um cartão de crédito com base no número fornecido. Aqui está uma explicação detalhada de cada parte:

- **import re**: importa o módulo de expressões regulares, usado para identificar padrões nos números dos cartões.

- **def identificar_bandeira(numero):** define uma função que recebe o número do cartão como parâmetro.

- **numero = numero.replace(' ', '').replace('-', '')**: remove espaços e traços do número, facilitando a validação.

- **if/elif re.match(...):** usa expressões regulares para verificar se o número do cartão corresponde a um padrão específico de bandeira.
    - **re.match(r'^4\d{12}(\d{3})?$', numero)**: verifica se o número começa com 4 e tem 13 ou 16 dígitos (Visa).
    - **re.match(r'^5[1-5]\d{14}$', numero)**: verifica se o número começa com 51 a 55 e tem 16 dígitos (MasterCard).
    - **re.match(r'^3[47]\d{13}$', numero)**: verifica se o número começa com 34 ou 37 e tem 15 dígitos (American Express).
    - E assim por diante para outras bandeiras como Diners Club, Discover, JCB, etc.

- **return 'Bandeira'**: se um padrão for encontrado, retorna o nome da bandeira correspondente.

- **else: return 'Bandeira não identificada'**: caso nenhum padrão seja encontrado, retorna que a bandeira não foi identificada.

- **if __name__ == "__main__":** permite que o código seja executado diretamente pelo terminal.
    - Solicita ao usuário o número do cartão e imprime a bandeira identificada.
"""