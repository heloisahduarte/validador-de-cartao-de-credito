# Validador de Cartão de Crédito

Este projeto é uma aplicação simples em Python capaz de identificar a bandeira de um cartão de crédito (Visa, MasterCard, American Express, etc.) com base no número informado pelo usuário.

## Como funciona

O programa solicita ao usuário o número do cartão de crédito, remove espaços e traços, e utiliza expressões regulares para identificar a bandeira do cartão de acordo com os padrões de cada operadora.

### Bandeiras suportadas

- Visa
- MasterCard
- American Express
- Diners Club
- Discover
- EnRoute
- JCB
- Voyager
- HiperCard
- Aura

### Padrões utilizados

| Bandeira         | Padrão (Regex)                          | Descrição                                         |
|------------------|-----------------------------------------|---------------------------------------------------|
| Visa             | `^4\d{12}(\d{3})?$`                     | Começa com 4, 13 ou 16 dígitos                    |
| MasterCard       | `^5[1-5]\d{14}$`                        | Começa com 51-55, 16 dígitos                      |
| American Express | `^3[47]\d{13}$`                         | Começa com 34 ou 37, 15 dígitos                   |
| Diners Club      | `^3(?:0[0-5]|[68]\d)\d{11}$`            | Começa com 300-305, 36 ou 38, 14 dígitos          |
| Discover         | `^6(?:011|5\d{2})\d{12}$`               | Começa com 6011 ou 65, 16 dígitos                 |
| EnRoute          | `^2(?:014|149)\d{11}$`                  | Começa com 2014 ou 2149, 15 dígitos               |
| JCB              | `^(?:2131|1800|35\d{3})\d{11}$`         | Começa com 2131, 1800 (15 dígitos) ou 35xxx (16)  |
| Voyager          | `^8699\d{11}$`                          | Começa com 8699, 15 dígitos                       |
| HiperCard        | `^(606282|3841)\d{10,12}$`              | Começa com 606282 (16) ou 3841 (13-16 dígitos)    |
| Aura             | `^50\d{14,17}$`                         | Começa com 50, 15 a 18 dígitos                    |

## Como executar

1. Certifique-se de ter o Python instalado.
2. No terminal, navegue até a pasta do projeto:
   ```
3. Execute o arquivo:
   ```
   python index.py
   ```
4. Digite o número do cartão quando solicitado.

## Exemplo de uso

```
Digite o número do cartão: 4111 1111 1111 1111
Bandeira: Visa
```

## Observações

- O programa não valida se o número do cartão é real, apenas identifica a bandeira pelo padrão numérico.
- Para adicionar novas bandeiras, basta incluir um novo bloco `elif` com o padrão desejado na função `identificar_bandeira`.
