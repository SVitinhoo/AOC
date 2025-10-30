def hex_convert(hex_code: str, conversion: bool=False) -> str:
    
    # um dicionario onde cada letra vale sua representação númerica
    hex_dict = {
        'A': '10', 'B': '11', 'C': '12',
        'D': '13', 'E': '14', 'F': '15'
    }

    # caso conversion seja True ele "inverte" o dicionario ex: '10': 'A', '11': 'B'...
    if conversion:
        hex_dict = {value:key for key, value in hex_dict.items()}

    return hex_dict.get(hex_code)

def convert_base(number:str, base_output: int) -> str:
    result = ""
    number = int(number)
    # o numero vai sofrer uma divisão inteira, e quando ele chegar a zero o loop para
    while number != 0:
        # armazena o resto da divisão do numero pela base selecionada
        digit = number % base_output
        # caso o resto da divisão esteja entre 10 a 15 ele vai converter para o valor hexadecimal correspondente
        if base_output == 16 and digit in (10, 11, 12, 13, 14, 15):
            digit = hex_convert(str(digit), True)
        # concatena em string o resto da divisão
        result += str(digit)
        # aplica a divisão inteira no número
        number //= base_output
    # inverte a string
    return result[::-1]

def conversion_to_decimal(number: str, base_input: int) -> int:
    result = 0
    # armazena na memoria a quantidade de caracteres que há no valor entrada transforma em um número e faz -1
    # exemplo: 102 retorna 2, 1024 retorna 3
    exponent = int(len(number))-1
    for letter in number:
        # caso seja um número hexadecimal ele converte
        if base_input == 16 and letter in "ABCDEF":
            letter = hex_convert(letter)
        # faz a exponenciação da base com o exponte e multiplica pelo número da vez
        result += base_input**exponent * int(letter)
        exponent -= 1
    return result

def error_verificator(number: str, base_input: int) -> bool:
    # cria uma lista com a base de entrada, exemplo: caso a base seja 8 ela criará: [0,1,2,3,4,5,6,7]
    lista = [f"{character}" for character in range(base_input)]
    for char in number:
        # caso uma dos caracteres do valor de entrada seja uma das letras do código hexadecimal, ele converte para sua representação numérica
        if char in ("A", "B", "C", "D", "E", "F"): 
            char = hex_convert(char)
        # caso o caractere não esteja na tupla ele retorna False
        if char not in lista: 
            return False
    return True

print("Bases disponiveis: Binario, Térnario, Quaternário, Octal, Decimal, Hexadecimal [obs: coloque em forma numeral]")
while True:
    print("=="*40)
    base_input = input("Qual base vai ser da entrada ? ").strip()
    # verificação se base de entrada está em uma das bases disponiveis
    if base_input not in ("2","3","4","8","10","16"): 
        print("ERRO, use uma base valída!, exemplo: 8")
        continue
    base_input = int(base_input)

    # verificação se base de saida está em uma das bases disponiveis
    base_output = input("Qual vai ser a base de saida ? ").strip()
    if base_output not in ("2","3","4","8","10","16"):
        print("ERRO, use uma base valída!, exemplo: 16")
        continue
    base_output = int(base_output)
    
    value_input = str(input(f"Digite o valor a ser convertido da base {base_input} -> {base_output}: ").strip().upper())
    # analisa se o valor de entrada esteja de acordo com a base informada
    if error_verificator(value_input, base_input) is False or value_input == "": 
        print("O valor está vazio ou não obedece as regras de nomeclatura da base de entrada!")
        continue

    # caso o valor de entrada seja zero
    if value_input == "0": 
        print(f"Resultado: 0")
        continue
    # verificação caso a base de entrada seja a mesma base de saida
    if base_input == base_output:
        # caso seja ele impreme na tela o valor de entrada
        print(f"Resultado: {value_input}")
        continue
    
    # caso a base de entrada seja diferente de 10 o programa converte o valor de entrada para a base decimal
    if base_input != 10:
        value_input = conversion_to_decimal(value_input, base_input)

    # quando o valor de entrada estiver na base decimal o programa converte o valor de entrada para a base de saida
    result = convert_base(value_input, base_output)
    print(f"Resultado: {result}")

# https://www.convertworld.com/pt/numerais/base-3.html esse site começa a bugar com  números enormes
# https://www.rapidtables.org/pt/convert/number/decimal-to-hex.html